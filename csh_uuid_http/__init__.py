import random
import requests

from uuid import uuid5
from uuid import NAMESPACE_OID

from flask import Flask

app = Flask(__name__)

word_site = "http://svnweb.freebsd.org/" \
            "csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()


@app.route('/uuid/<uid>')
def uid_to_uuid(uid):
    try:
        member = app.config['LDAP_CONN'].get_member(uid, True)
        uuid = member.entryUUID
    except KeyError:
        return str(uuid5(NAMESPACE_OID, uid))

    return uuid


@app.route('/uid/<uuid>')
def uuid_to_uid(uuid):
    try:
        member = app.config['LDAP_CONN'].get_member(uuid, False)
        uid = member.uid
    except KeyError:
        return random.choice(WORDS).lower()

    return uid
