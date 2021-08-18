import requests
url = 'http://www.wikipedia.org'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\f *", r.status_code)
h = requests.head(url)
print("Header.")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {
    'User-Agent' : 'Iphone 8'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)