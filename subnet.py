import subprocess


class OvnCreateError(Exception):
    def __init__(self, ErrorInfo) -> None:
        super().__init__(self)
        self.error_info = ErrorInfo

    def __str__(self) -> str:
        return self.error_info


def create_subnet():
    pass


def format_subnet():
    pass


def validate_subent():
    pass


def check_subnet_conflict():
    pass


# create logical switch and patch to router
def create_logical_switch_and_patch_to_router(
    ls_name: str,
    lr_name: str,
    cidr_bolck: str,
    exclude_ips: str,
    gateway: str,
    mac: str,
) -> None:
    try:
        create_logical_switch(ls_name, lr_name, cidr_bolck, exclude_ips)
        create_logical_router_port(ls_name, lr_name, gateway, mac)
        create_port_patch_to_router(
            ls_name,
            lr_name,
            f"{ls_name}-patch-{lr_name}",
            f"{lr_name}-patch-{ls_name}",
        )
    except Exception as e:
        raise e


# create logical switch
def create_logical_switch(
    ls_name: str, lr_name: str, cidr_bolck: str, exclude_ips: str
) -> None:
    # TODO:need log to record
    status, output = subprocess.getstatusoutput(
        "ovn-nbctl ls-add {0}-{1} -- set logical_switch {0}-{1} external_ids:vendor={2} other_config:subnet={3} other_config:exclude_ips={4}".format(
            lr_name, ls_name, "FusionCompute", cidr_bolck, exclude_ips
        )
    )
    if not status:
        print(f"create logical switch {lr_name}-{ls_name} success...")
    else:
        raise OvnCreateError(output)


# create logical switch port patch to router
def create_port_patch_to_router(
    ls_name: str, lr_name: str, lsp_name: str, lrp_name: str) -> None:
    status, output = subprocess.getstatusoutput(
        f"ovn-nbctl lsp-add {lr_name}-{ls_name} {lsp_name} -- set logical_switch_port {lsp_name} type=router addresses=router options:router-port={lrp_name}"
    )
    if not status:
        print("create switch port patch to router success...")
    else:
        raise OvnCreateError(output)


# create logical router port
def create_logical_router_port(
    ls_name: str, lr_name: str, gateway: str, mac: str
) -> None:
    # TODO:need log to record

    # WARN: create logical router
    status, output = subprocess.getstatusoutput(f"ovn-nbctl lr-add {lr_name}")
    if not status:
        print(f"create logical router {lr_name} success...")
    else:
        raise OvnCreateError(output)

    # create logical router port
    router_port = "{0}-patch-{1}".format(lr_name, ls_name)
    status, output = subprocess.getstatusoutput(
        f"ovn-nbctl lrp-add {lr_name} {router_port} {mac} {gateway}"
    )
    if not status:
        print(f"create logical router {router_port} success...")
    else:
        raise OvnCreateError(output)


if __name__ == "__main__":
    try:
        create_logical_switch_and_patch_to_router(
            "subnet1",
            "vpc1",
            "10.10.10.0/24",
            "10.10.10.1..10.10.10.2",
            "10.10.10.1",
            "52:54:00:c1:68:50",
        )
    except Exception as e:
        print(e)
