#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
	parser = optparse.OptionParser() #created an instance for a object 
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac",help=" New MAC Address")
	#(options, arguments) = parser.parse_args()
	return parser.parse_args()

def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])




#calling functions
(options, arguments) = get_arguments()

change_mac(options.interface, options.new_mac)




