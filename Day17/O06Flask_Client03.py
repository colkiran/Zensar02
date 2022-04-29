
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + '/getproduct/baverage')

res  = response.json()
for k, info in res.items():
    print(k.upper())
    print("--------")
    for ky, vl in info.items():
        print(ky)
        print("-----")
        for ki, v in vl.items():
            print(ki, "=>", v)
        print("-" * 40)

print("=" * 60)

response= requests.put(BASE + '/getproduct/baverage', data = {'gst': 10} )
res = response.json()

print(res)

print("=" * 60)
response = requests.delete(BASE + '/getproduct/baverage')

res = response.json()
print(res)