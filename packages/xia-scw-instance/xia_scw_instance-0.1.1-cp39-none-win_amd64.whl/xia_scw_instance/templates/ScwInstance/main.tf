locals {
  wan_ip = try(var.vpc_details.wan_ip, null)
  ssh_hosts = try(concat([var.vpc_details.lan_address], var.ssh_hosts), [])
  bastion_port = try(var.vpc_details.bastion_port, null)
  private_network_id = try(var.vpc_details.private_network_id, null)
  gateway_network_id = try(var.vpc_details.gateway_network_id, null)
}

data "scaleway_instance_image" "my_image" {
  name = var.image
  zone = var.zone
}

resource "scaleway_instance_server" "instance" {
  name  = var.name
  zone  = var.zone
  type  = var.type
  image = data.scaleway_instance_image.my_image.id
  tags  = var.tags
  state = var.state == "maintenance" ? "started" : var.state
}


data "scaleway_vpc_public_gateway" "main" {
  zone = var.zone
  name = var.vpc_name
}

resource "scaleway_instance_private_nic" "service_nic" {
  count              = (var.state != "stopped" && length(var.lan_ip) > 0) ? 1 : 0
  zone               = var.zone
  server_id          = scaleway_instance_server.instance.id
  private_network_id = local.private_network_id
}

resource "time_sleep" "wait_5_seconds_after_service_nic" {
  count           = (var.state != "stopped" && length(var.lan_ip) > 0) ? 1 : 0
  depends_on      = [scaleway_instance_private_nic.service_nic]
  create_duration = "5s"
}

resource scaleway_vpc_public_gateway_dhcp_reservation main {
  count = (var.state != "stopped" && length(var.lan_ip) > 0) ? 1 : 0

  zone               = var.zone
  gateway_network_id = local.gateway_network_id
  mac_address        = scaleway_instance_private_nic.service_nic[0].mac_address
  ip_address         = var.lan_ip
  depends_on         = [time_sleep.wait_5_seconds_after_service_nic]
}

locals {
  ufw_ssh = length(local.ssh_hosts) > 0 && var.state != "maintenance" ? [
  for ip in local.ssh_hosts : "ufw allow from ${ip} to any port 22 proto tcp"
  ] : [
    "ufw allow ssh"
  ]
  ufw_commands = flatten([
  for rule in var.forwards : [
  for ip in rule.allowed_ips : "ufw allow from ${ip} to any port ${rule.lan_port} proto ${rule.protocol}"
  ]
  ])
}

resource scaleway_vpc_public_gateway_pat_rule service_pat {
  for_each = { for i, item in var.forwards : i => item if contains(keys(item), "wan_port") && item.wan_port != null }

  zone         = var.zone
  gateway_id   = data.scaleway_vpc_public_gateway.main.id
  private_ip   = var.lan_ip != "" && var.lan_ip != null ? var.lan_ip : "192.0.0.1"
  private_port = each.value["lan_port"]
  public_port  = contains(keys(each.value), "wan_port") && each.value["wan_port"] != null ? each.value["wan_port"] : 59999
  protocol     = each.value["protocol"]
  depends_on   = [scaleway_vpc_public_gateway_dhcp_reservation.main]
}

resource "null_resource" "ufw_status" {
  count = (var.state != "stopped" && length(var.lan_ip) > 0) ? 1 : 0

  triggers = {
    ssh_status = jsonencode(local.ufw_ssh)
    app_status = jsonencode(local.ufw_commands)
  }

  provisioner "remote-exec" {
    inline = concat(
      ["ufw --force reset"],
      local.ufw_ssh,
      local.ufw_commands,
      ["ufw --force enable"]
    )

    connection {
      type        = "ssh"
      user        = "root"
      private_key = file(var.ssh_private_key)
      host        = var.lan_ip

      bastion_host        = local.wan_ip
      bastion_port        = local.bastion_port
      bastion_user        = "bastion"
      bastion_private_key = file(var.ssh_private_key)

      timeout = "5m"   # Maximum time to wait for the connection to become available
    }
  }

  depends_on = [scaleway_vpc_public_gateway_dhcp_reservation.main]
}

