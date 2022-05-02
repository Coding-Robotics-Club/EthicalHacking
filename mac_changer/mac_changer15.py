#!/usr/bin/env python

import subprocess
import optparse
import re

# This function gets an argument from the terminal, especially options and their values.
def get_arguments():
	parser = optparse.OptionParser() #created an instance for a object 
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac",help=" New MAC Address")
	(options, arguments) = parser.parse_args() #parse_args() returns two values: options, an object containing 
                                               #values for all of your options
	#check if any of the options are missing
	if not options.interface: # if the interface option is missing
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new_mac: # if the mac address if missing
		parser.error("[-] Please specify a new mac, use --help for more info.")
	return options # options contain value of -i and value of -m (eg: eth0, 00:11:22:33:44:55)

#get interface and new mac address as an argument and change mac address of the interface.
def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"]) #shut down interface
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) # change MAC Address
	subprocess.call(["ifconfig", interface, "up"])   #restart interface 

# get interface ("eth0") and filters the mac address based on the rule supplied.
def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface]) #capturing the result of "ifconfig eth0"
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) #filter result with rules to capture only the MAC address
	if mac_address_search_result: #if the search results found then return the filtered value, i.e : MAC address Values.
		return mac_address_search_result.group(0) #group(0) is the first search result
	else:
		print("[-] Could not read the MAC address")

#calling functions 
options = get_arguments() #captured values are stored in options.
current_mac = get_current_mac(options.interface) # option.interface holds "eth0"
print("Current MAC = " + str(current_mac)) #printing mac address of "eth0" (str - convert byteObject to string).

#change the mac address
change_mac(options.interface, options.new_mac) #option.interface = eth0 & option.new_mac hold new mac supplied in the terminal by the by user
current_mac = get_current_mac(options.interface) # Recheck and obtained the MAC Address after changing it.

#check if the new current mac is same as the one supplied by the user.
if current_mac == options.new_mac: #options.new_mac contains the MAC address supplied in the terminal by the user.
	print("[+] MAC address was successfully changed to " + current_mac)
else:
	print("[-] MAC address did not get changed")
