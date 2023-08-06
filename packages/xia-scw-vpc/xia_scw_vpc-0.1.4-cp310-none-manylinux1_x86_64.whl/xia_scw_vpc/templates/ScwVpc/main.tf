resource scaleway_vpc_public_gateway_ip main {
    zone = var.zone
}

resource "scaleway_vpc_public_gateway_dhcp" "dhcp01" {
  zone       = var.zone
  subnet             = var.lan_subnet
  push_default_route = true
  enable_dynamic     = false
  address            = var.lan_address
  pool_high          = var.lan_high
  pool_low           = var.lan_low
}

resource scaleway_vpc_private_network main {
  zone       = var.zone
  name       = var.lan_name
  depends_on = [scaleway_vpc_public_gateway_dhcp.dhcp01]
}

resource scaleway_vpc_public_gateway main {
  zone            = var.zone
  name            = var.name
  type            = var.type
  ip_id           = scaleway_vpc_public_gateway_ip.main.id
  bastion_enabled = true
  bastion_port    = var.bastion_port
  depends_on      = [scaleway_vpc_public_gateway_dhcp.dhcp01]
}

resource scaleway_vpc_gateway_network main {
  zone               = var.zone
  gateway_id         = scaleway_vpc_public_gateway.main.id
  private_network_id = scaleway_vpc_private_network.main.id
  dhcp_id            = scaleway_vpc_public_gateway_dhcp.dhcp01.id
  cleanup_dhcp       = true
  enable_masquerade  = true
  depends_on         = [scaleway_vpc_private_network.main]
}
