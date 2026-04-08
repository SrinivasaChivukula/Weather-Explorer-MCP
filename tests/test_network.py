import requests, json
url = "https://en.wikipedia.org/api/rest_v1/page/summary/New_York_City"
resp = requests.get(url, timeout=10)
print('status', resp.status_code)
print(resp.text[:200])
