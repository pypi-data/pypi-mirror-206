output "project_id" {
  value = var.project_id
}

output "name" {
  value = scaleway_vpc_private_network.main.name
}

output "zone" {
  value = scaleway_vpc_public_gateway.main.zone
}

output "type" {
  value = scaleway_vpc_public_gateway.main.type
}

output "ip_id" {
  value = scaleway_vpc_public_gateway_ip.main.id
}

output "wan_ip" {
  value = scaleway_vpc_public_gateway_ip.main.address
}

output "private_network_id" {
  value = scaleway_vpc_private_network.main.id
}

output "gateway_network_id" {
  value = scaleway_vpc_gateway_network.main.id
}

output "lan_name" {
  value = var.lan_name
}

output "lan_subnet" {
  value = var.lan_subnet
}

output "lan_address" {
  value = scaleway_vpc_public_gateway_dhcp.dhcp01.address
}

output "lan_low" {
  value = scaleway_vpc_public_gateway_dhcp.dhcp01.pool_low
}

output "lan_high" {
  value = scaleway_vpc_public_gateway_dhcp.dhcp01.pool_high
}

output "bastion_port" {
  value = scaleway_vpc_public_gateway.main.bastion_port
}

output "tf_state" {
  value = var.tf_state
}

output "processed_at" {
  value = timestamp()
}
