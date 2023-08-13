from ovsdbapp.backend.ovs_idl import connection
from ovsdbapp.schema.ovn_northbound import impl_idl

conn = "tcp:172.29.128.100:6641"

# The python-ovs Idl class. Take it from server's database
i = connection.OvsdbIdl.from_server(conn, 'OVN_Northbound')

# The ovsdbapp Connection object
c = connection.Connection(idl=i, timeout=3)

# The OVN_Northbound API implementation object
api = impl_idl.OvnNbApiIdlImpl(c)

try:
    api.ls_add("sw0").execute(check_error=True)
except :
    print("error")
# with api.transaction(check_error=True) as txn:
#     txn.add(api.ls_add("sw1"))
#     txn.add(api.lsp_add("sw1", "sw1-port1"))
#     txn.add(api.lsp_set_addresses("sw1-port1", ["50:54:00:00:00:01 11.0.0.1"]))
#     txn.add(api.lsp_add("sw1", "sw1-port2"))
#     txn.add(api.lsp_set_addresses("sw1-port2", ["50:54:00:00:00:02 11.0.0.2"]))

# for ls_row in api.ls_list().execute(check_error=True):
#     print("uuid: %s, name: %s" % (ls_row.uuid, ls_row.name))
#     for lsp_row in api.lsp_list(switch=ls_row.uuid).execute():
#         print("  uuid: %s, name: %s" % (lsp_row.uuid, lsp_row.name))
