#addr="108.162.198.171"
import sys
addr = sys.argv[1]
url="https://www.countryipblocks.net/search_ip.php?search_ip=%s"


import requests
from BeautifulSoup import BeautifulSoup as B


h=requests.get(url % addr).text 
#h=open('_test.txt').read()
tdiv=B(h).find("div", {"id": "contentBody"})
#print dir(tdiv)

#children = tdiv.findChildren()
#for child in children:
#    print child
##
#print tdiv

#CIDR: 180.178.32.0/19"

import re

#IP Address assigned to: HONG KONG
m=re.search("IP Address assigned to: (?P<country>[A-Za-z\s]+).*CIDR\: (?P<cidr>[0-9\.\/]+)",str(tdiv)).groupdict()
if m:
    print "//",m['country']
    print m['cidr'],";"
