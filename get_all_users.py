import ldap3

HOST = "ldap.bluecat.local"
PORT = 3389
USE_SSL = False
GET_INFO = ldap3.NONE

USER = "cn=admin,dc=bluecat,dc=local"
PASSWORD = "Ztdss123$"

server = ldap3.Server(host=HOST, port=PORT, use_ssl=USE_SSL, get_info=GET_INFO)
connection = ldap3.Connection(server, user=USER, password=PASSWORD)
connection.bind()

paged_response = connection.extend.standard.paged_search(
    search_base="dc=bluecat,dc=local",
    search_filter="(objectClass=inetOrgPerson)",
    search_scope=ldap3.SUBTREE,
    attributes=ldap3.ALL_ATTRIBUTES,
    paged_size=1000
)

print("Users of directory: ")
for entry in paged_response:
    print(entry.get("attributes"))