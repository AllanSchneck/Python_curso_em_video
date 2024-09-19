import urllib.request
try:
    urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('\033[34mNão foi possível acesar o site Pudim no momento')
else:
    print('\033[33mConsegui entrar')
