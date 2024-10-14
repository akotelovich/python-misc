from itertools import product
import socket
import string
import whois


"""
returns all possible 2letter subdomains in specific TLD with the following data:
xx.lv:ip.add.re.ss
xy.lv:NA

"""

tld="lv"
nl = ['0','1','2','3','4','5','6','7','8','9'] + list(string.ascii_lowercase)
c = product(nl, repeat=2)

for i in list(c):
    d = ''.join(i) + "." + tld
    try:
        t = socket.gethostbyname_ex(d)
        print (d +":" + ','.join(t[2]))
    except Exception:
        print (d + ":NA")
