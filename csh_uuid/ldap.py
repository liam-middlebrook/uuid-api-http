import ldap
import ldap.modlist
from ldap.ldapobject import ReconnectLDAPObject

ldap_conn = None


def ldap_init(app):
    app.config['LDAP_CONN'] = ReconnectLDAPObject(app.config['LDAP_URL'])
    app.config['LDAP_CONN'].simple_bind_s(
            app.config['LDAP_BIND_DN'],
            app.config['LDAP_BIND_PW'])


def get_uid(app, uuid):
    if app.config['LDAP_CONN'] is None:
        ldap_init(app)

    ldap_results = app.config['LDAP_CONN'].search_s(
            app.config['LDAP_USER_OU'],
            ldap.SCOPE_SUBTREE,
            "(entryUUID=%s)" % uuid,
            ['uid'])

    if len(ldap_results) != 1:
        return None
    return ldap_results[0][1]['uid'][0].decode('utf-8')


def get_uuid(app, uid):
    if app.config['LDAP_CONN'] is None:
        ldap_init(app)

    ldap_results = app.config['LDAP_CONN'].search_s(
            app.config['LDAP_USER_OU'],
            ldap.SCOPE_SUBTREE,
            "(uid=%s)" % uid,
            ['entryUUID'])

    if len(ldap_results) != 1:
        return None
    return ldap_results[0][1]['entryUUID'][0].decode('utf-8')
