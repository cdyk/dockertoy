import http.client
import json

dummy = {
    'foo': 'bar',
    'baz': ['quux', 1, 2, 3]
}

conn = http.client.HTTPConnection("localhost", port=4000)

conn.request('POST', '/', json.dumps(dummy), {'Content-type': 'application/json'})
resp = conn.getresponse()
print(resp.read().decode())
