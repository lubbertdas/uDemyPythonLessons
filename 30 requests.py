import requests

###### Never use verify=False in production ######
r = requests.get("https://www.google.com/", verify=False)
# 200 - ok
print(r.status_code)

print(r.headers)
print(r.headers["Date"])

# Webpage response:
print(r.text)