#!/usr/bin/env python

import subprocess

#securing your program

interface = input("interface > ")

new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

#subprocess.call("ifconfig " + interface +  " down", shell=True)
#subprocess.call("ifconfig " + interface +  " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface +  " up", shell=True)

#Second  Method

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

