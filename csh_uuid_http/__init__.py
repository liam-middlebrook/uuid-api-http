import random
import requests

from uuid import uuid5
from uuid import NAMESPACE_OID

from flask import Flask

from csh_uuid.ldap import ldap_init
from csh_uuid.ldap import get_uid
from csh_uuid.ldap import get_uuid

app = Flask(__name__)

word_site = "http://svnweb.freebsd.org/" \
            "csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()


@app.route('/uuid/<uid>')
def uid_to_uuid(uid):
    uuid = get_uuid(app, uid)

    if uuid is None:
        return str(uuid5(NAMESPACE_OID, uid))
    return uuid


@app.route('/uid/<uuid>')
def uuid_to_uid(uuid):
    uid = get_uid(app, uuid)

    if uid is None:
        return random.choice(WORDS).lower()
    return uid
