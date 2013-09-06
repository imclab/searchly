import requests
import simplejson
from searchly.constants import READYFORCE_API_URL


def name_member_search(name):
    payload = simplejson.dumps({
        'limit': 20,
        'verbosity': 'verbose',
        'search': name
    })
    response = simplejson.loads(requests.post(READYFORCE_API_URL + 'member_search', payload).content)
    return response.get('result').get('members')
