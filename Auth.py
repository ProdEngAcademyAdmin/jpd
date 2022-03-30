# import requests

# username = 'adirgali2@gmail.com'
# password = 'P@P@9ol.poi'

# #r = requests.post('https://galipapa.jfrog.io/artifactory/api/security/token',data='username= adirgali2@gmail.com&password= P@P@9ol.poi')

# #r = requests.post("https://galipapa.jfrog.io/artifactory/api/security/token",data={'username': 'adirgali2@gmail.com', 'password': 'P@P@9ol.poi'})

# #curl -s -XPOST -u $username:$password https://galipapa.jfrog.io/artifactory/api/security/token -d "username=$username" -d "scope=member-of-groups:administrators"

# data = {
#     'j_username': 'adirgali2@gmail.com',
#     'j_password': 'P@P@9ol.poi'
# }

# response = requests.post(
#     'https://galipapa.jfrog.io/artifactory/api/security/token',
#     data=data
# )


# print(response.text)
 



# #curl -uadmin:password -XPOST "http://localhost:8081/artifactory/api/security/token" -d "username=johnq" -d "scope=member-of-groups:readers"

# from urllib import response
# import requests
# from requests.auth import HTTPBasicAuth

# r = requests.post('https://galipapa.jfrog.io/artifactory/api/security/token', auth=HTTPBasicAuth('adirgali2@gmail.com', 'P@P@9ol.poi'))

# print(r.text)
#from urllib import response
from distutils.command.config import config
from lib2to3.pgen2 import token
from tkinter import W
import requests
import json

header = {'Content-Type': 'application/x-www-form-urlencoded'}

data = 'username=adirgali2@gmail.com&scope=member-of-groups:administrators'

auth ='adirgali2@gmail.com' , 'P@P@9ol.poi'

r = requests.post('https://galipapa.jfrog.io/artifactory/api/security/token', headers=header, data=data, auth=auth)





f = open("config.txt", "w")

f.write(r)
f.close()


# r.json()

# print(r.text)
