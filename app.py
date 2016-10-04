import os
from csh_uuid_http import app

from csh_ldap import CSHLDAP

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

app.config['LDAP_CONN'] = CSHLDAP(
                            app.config['LDAP_BIND_DN'],
                            app.config['LDAP_BIND_PW'])
if __name__ == '__main__':
    app.run(host=app.config['IP'], port=app.config['PORT'])

application = app
