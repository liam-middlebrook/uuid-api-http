import os
from csh_uuid_http import app
from csh_uuid_http.ldap import ldap_init

app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
ldap_init(app)

if __name__ == '__main__':
    app.run(host=app.config['IP'], port=app.config['PORT'])

application = app
