import urllib.request
try:
  url = urllib.request.urlopen("https://www.python.org/")
  content = url.read()
  url.close()
except urllib.error.HTTPError:
  print('url not found')
  exit()

file = open('./python.html','wb')
file.write(content)
file.close()

