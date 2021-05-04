import requests
import urllib.request, urllib.error, urllib.parse
import json
longitude="87.9739"
latitude="25.3176"
url="http://www.7timer.info/bin/astro.php?lon={0}&lat={1}&ac=0&unit=metric&output=json&tzshift=0".format(longitude,latitude)
response = urllib.request.urlopen(url)
webContent = response.read()
#print(webContent)
datadictionary=json.loads(webContent)
print(datadictionary)
for key in datadictionary.keys():
    print(key)
