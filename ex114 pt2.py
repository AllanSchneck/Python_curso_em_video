import urllib.request
import urllib

try:
    site = urllib.request.urlopen('https://www.brivia.com.br/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo ok')
    print(site.read())
