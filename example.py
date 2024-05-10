from controller import ENDPOINT, SERVER, LOCAL


ENDPOINT.bond_info("localhost", "8086")
LOCAL.version()
LOCAL.whoami()
