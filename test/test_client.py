import urllib2
url = "http://127.0.0.1:8000/v1/recognize/0"
audio = open('/Users/Torres/Desktop/L33P1.wav','rb').read()
request = urllib2.Request(url, data=audio, headers={'Content-Type':'audio/x-wav'})
response = urllib2.urlopen(request)
print response.read()
