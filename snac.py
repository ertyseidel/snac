#SASS Non-Api Compiler
# (SNAC)

#THIS IS TERRIBLE CODE AND YOU SHOULD FEEL BAD FOR USING IT

import http.client, urllib.request, urllib.parse, sys, re

if(len(sys.argv) != 3):
    print("Usage: python snac.py filetocompile.sass filetowrite.css")
    exit(1)

try:
    infile = open(sys.argv[1])
    params = urllib.parse.urlencode({
        'syntax' : 'sass',
        'input' : infile.read()
    })
except IOError:
    print('Error: ' + sys.argv[1] + 'is not a valid file.')
    exit(1)
infile.close()
    
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = http.client.HTTPConnection("sass-lang.com:80")
conn.request("POST", "/try.html",
             params, headers)
response = conn.getresponse()
print (response.status, response.reason)
responsestring = response.read()
#OH GOD IT BURNS
strtowrite = re.search(b"<pre class='result'>(.*)</pre>", responsestring)
strtowrite = re.sub(b"&#x000A;", b"\r\n", strtowrite.group(1))
#THIS IS BLASPHEMY
outfile = open(sys.argv[2], "wb")
outfile.write(strtowrite)
outfile.close()
conn.close()
