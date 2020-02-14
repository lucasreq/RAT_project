#!/usr/bin/env python

from scapy.all import *
from uuid import getnode as get_mac

macaddr = hex(get_mac())
#macaddrstr = str(macaddr)
opesys = os.uname()

system = opesys[0]
user = opesys[1]
distrib = opesys[2]

IP_h = "127.0.0.1"

#test = "test:" +' '+macaddr+' '+system+' '+distrib+' '+user

test = [user,macaddr,system,distrib]

def validateIP(s):
	address=s.split('.')
	if len(address)!=4:
		return False
	for x in address:
		if not x.isdigit():
			return False
		i=int(x)
		if i<0 or i>255:
			return False
	return True

if validateIP(IP_h):
	j = 0
	while j < 4:
		send (IP(dst="127.0.0.1") / UDP() / DNS(qd=DNSQR(
        qname="localhost", qtype="A"))/test[j])
		print(opesys[j])
		j+=1
		
    #print(test)

else:
    print("Bad ip")
