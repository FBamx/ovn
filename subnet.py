import subprocess


def create_subnet():
    pass


def format_subnet():
    pass


def validate_subent():
    pass


def check_subnet_conflict():
    pass


def create_logical_switch(
    ls_name: str, lr_name: str, cidr_block: str, gateway: str, need_router=True
) -> None:
    # TODO:need log to record
    status, output = subprocess.getstatusoutput(
        "ovn-nbctl ls-add {0}-{1}".format(lr_name, ls_name)
    )
    if not status:
        print(f"create logical switch {lr_name} success...")
    else:
        print(output)

    if need_router:
        create_router_port(ls_name, lr_name)


def create_router_port(ls_name: str, lr_name: str) -> None:
    # TODO:need log to record

    # create logical router
    status, output = subprocess.getstatusoutput(f"ovn-nbctl lr-add {lr_name}")
    if not status:
        print(f"create logical router {lr_name} success...")
    else:
        print(output)

    # create logical router port
    router_port = "{0}-{1}-port".format(lr_name, ls_name)
    status, output = subprocess.getstatusoutput(
        f"ovn-nbctl lrp-add {lr_name} {router_port} 52:54:00:c1:68:50 10.0.0.1/24"
    )
    if not status:
        print(f"create logical router {router_port} success...")
    else:
        print(output)

    # create logical switch port patch to router
    port_patch_to_router = "{0}-{1}-port".format(ls_name, lr_name)
    status, output = subprocess.getstatusoutput(
        f"ovn-nbctl lsp-add {lr_name}-{ls_name} {port_patch_to_router} -- set logical_switch_port {port_patch_to_router} type=router options:router-port={router_port}"
    )
    if not status:
        print("create switch port patch to router success...")
    else:
        print(output)


if __name__ == "__main__":
    create_logical_switch("subnet1", "vpc1", "10.10.10.10/24", "10.10.10.1")
