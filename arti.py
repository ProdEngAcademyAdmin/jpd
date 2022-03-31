import requests

#Artifactory ping
url_ping = 'https://galipapa.jfrog.io/artifactory/api/system/ping'


r = requests.get(url_ping)
print(r.text)

#curl -s -H "Authorization: Bearer $Token" https://galipapa.jfrog.io/artifactory/api/storageinfo

#Artifactory storage info

headers = 'Authorization: Bearer {}'
url_