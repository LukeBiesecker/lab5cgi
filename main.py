#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()

angle = data.getvalue('anglein')
zero = data.getvalue('Zero')
data = {"anglein":angle, "Zero":zero}

with open('steppercontrol.txt', 'w') as f:
  json.dump(data,f)

print("Content-type: text/html\n\n")
print('<html>')
print('<form action="/cgi-bin/steppercontrol.py" method="POST">')


print('<input type="submit" value="Submit">')
print('<input type="submit" value="Zero">')
print('</form>')
print('</html>')

from urllib.request import urlopen
from urllib.parse import urlencode

import time

api = "VT53I8JRWLSWVBXK"   # Enter your API key

while True:
  params = {
    "api_key":api,
    1: angle,
    2: angle}
  params = urlencode(params)   # put dict data into a GET string

  # add "?" to URL and append with parameters in GET string:
  url = "https://api.thingspeak.com/update?" + params
  try:
    response = urlopen(url)      # open the URL to send the request
  except Exception as e:
    print(e)