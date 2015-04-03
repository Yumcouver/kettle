import urllib2
url = "http://127.0.0.1:8000/v1/raw/0"
audio = open('/Users/Torres/Desktop/L23P2.wav','rb').read()[44:]
request = urllib2.Request(url, data=audio)
response = urllib2.urlopen(request)
print response.read()
