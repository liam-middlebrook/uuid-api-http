import os

# Flask config
DEBUG = False
HOST_NAME = os.environ.get('UUID_HOST_NAME', 'localhost')
APP_NAME = os.environ.get('UUID_APP_NAME', 'csh_uuid')
IP = os.environ.get('UUID_SERVER_IP', '0.0.0.0')
PORT = os.environ.get('UUID_PORT', 8080)

# LDAP config
LDAP_URL = os.environ.get('UUID_LDAP_URL', '')
LDAP_BIND_DN = os.environ.get('UUID_LDAP_BIND', '')
LDAP_BIND_PW = os.environ.get('UUID_LDAP_BINDPW', '')
LDAP_USER_OU = os.environ.get('UUID_LDAP_USER_OU', '')
