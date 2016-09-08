import os

# Flask config
DEBUG = True
HOST_NAME = 'localhost'
APP_NAME = 'csh_uuid'
IP = '0.0.0.0'
PORT = 6969

# LDAP config
LDAP_URL = 'ldaps://ldap.csh.rit.edu/'
LDAP_BIND_DN = 'cn=account,ou=Apps,dc=csh,dc=rit,dc=edu'
LDAP_BIND_PW = ''
LDAP_USER_OU = 'ou=Users,dc=csh,dc=rit,dc=edu'
