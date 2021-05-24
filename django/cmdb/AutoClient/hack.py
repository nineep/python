import requests
import hashlib
import time


current_time = time.time()
app_id = "8kasoimnasodn8687asdfkmasdf"
app_id_time = '%s|%s' % (app_id, current_time)

m = hashlib.md5()
print(m)
m.update(bytes(app_id_time))
authkey = m.hexdigest()

authkey_time = "%s|%s" % (authkey, current_time,)
print(authkey_time)


host_data = {
    'status': True,
    'data': {
        'hostname': 'c1.com',
        'disk': {'status': True, 'data': 'xxx'},
        'mem': {'status': True, 'data': 'xxx'},
        'nic': {'status': True, 'data': 'xxx'},
    }
}

response = requests.post(
    url='http://127.0.0.1:8000/api/asset/',
    json=host_data,
    headers={'authkey': "533c70229db9cf2596047de1fde4d9ad|1492397210.467444"}
)

print(response.text)



