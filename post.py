import urllib, urllib2

url = 'http://localhost:5000/welcome'
args = {'name' : 'yash', 'email' : 'yash.girdhar@gmail.com'}
encoded_args = urllib.urlencode(args)
response = urllib2.urlopen(url,encoded_args).read()
print response
