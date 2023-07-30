#!/usr/bin/python


class SubnetOptions:
    def __init__(self) -> None:
        self.name = ""


class VpcOptions:
    def __init__(self) -> None:
        pass


class Vpc:
    def __init__(self, vpc_options) -> None:
        self.vpc_options = vpc_options

    def create_subnet(self):
        pass

    def print_vpc_options(self):
        pass


if __name__ == "__main__":
    subnet_options = SubnetOptions()
