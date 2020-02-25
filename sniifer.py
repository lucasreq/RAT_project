#!/usr/bin/env python3

from scapy.all import *
from datetime import datetime
import time
import datetime
import sys

interface = 'eth0'
filter_bpf = "host 77.207.68.147"

# ------ SELECT/FILTER MSGS
def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
# ------ SELECT/FILTER DNS MSGS
    try:
        if DNSQR in pkt: #and pkt.dport == 53:
        # queries
           print ('[**] Detected DNS QR Message at: ' + pkt_time)
           data = pkt.show([Raw])
           f = open('dns_req.txt', "a")
           f.write("<----------------------- PACKET :" + pkt_time + " --------------------------->\n")
           for i in data:
               dataReq = str(i)
               f.write(dataReq)
               

# f.close()
           # 
        elif DNSRR in pkt:# and pkt.sport == 53:
        # responses
           print ('[**] Detected DNS RR Message at: ' + pkt_time)
           pkt.show([Raw])
 # 
    except:
        pass
    

# ------ START SNIFFER
paquets = sniff(filter=filter_bpf,iface=interface,  prn=select_DNS)

#print(f"\n[*] Some useful Raw data: {paquets.show()}")

#f = open('dns_req.txt', "w")
# for i in data:
#     test = str(i)
#     f.write(test)
#     print(test)

# f.close()