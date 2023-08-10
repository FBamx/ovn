#!/usr/bin/python

from dataclasses import dataclass


@dataclass
class Subnet:
    default: bool
    vpc: str
    protocol: str
    cidr_block: str
    gateway: str
    exclude_ips: list
    provider: str
    enable_dhcp: bool
    dhcp_options: str


@dataclass
class Vpc:
    static_routes: list
    policy_routes: list
    vpc_peerings: list
    enable_external: bool


if __name__ == "__main__":
    subnet = Subnet(
        default=False,
        vpc="23",
        protocol="ipv4",
        cidr_block="10.10.10.0/24",
        gateway="10.10.10.1",
        exclude_ips=["10.10.10.1"],
        provider="10.10.10.2",
        enable_dhcp=True,
        dhcp_options="dhcp",
    )
    print(repr(subnet))
