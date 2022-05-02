#!/usr/bin/env python

import subprocess

#using python2 raw_input function

interface = raw_input("interface > ")

new_mac = raw_input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface +  " down", shell=True)
subprocess.call("ifconfig " + interface +  " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +  " up", shell=True)



