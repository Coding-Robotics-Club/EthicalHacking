#!/usr/bin/env python

import subprocess

#using python3 input from the user

interface = input("interface > ")

new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface +  " down", shell=True)
subprocess.call("ifconfig " + interface +  " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +  " up", shell=True)



