from controller import ENDPOINT, SERVER, LOCAL

hostname = "localhost"

ENDPOINT.bond_info(hostname, 8086)
LOCAL.version()
LOCAL.whoami()
