'''
Longest network prefix matching program using Python This utility is useful when one has to find the longest matching prefix for the list of IP address. Pre-requisite for this utility: download and python import module SubnetTree

Usage: longest_prefix_match.py {Input file with list of Prefixes} {Input file with list of IP addresses}
'''

import sys
import re
import SubnetTree
import socket

if len(sys.argv) < 2:
	print "Usage: "+sys.argv[0]+" <Input file with list of Prefixes> <Input file with list of IP addresses>"
	print "Example: "+sys.argv[0]+"prefix_file ipaddress_file"  
	sys.exit()
prefix_file = sys.argv[1]
ip_file = sys.argv[2]

st = SubnetTree.SubnetTree()
for prefix in open(prefix_file).readlines():
	prefix = prefix.strip('\n')	
	if prefix:
		st[prefix] = prefix
st.set_binary_lookup_mode(False)
def pass_ipfile(ip_file):
	for ip in open(ip_file).readlines():
		st.set_binary_lookup_mode(False)
		ip = ip.strip('\n')
		if ip:
			if ip in st:
				st.set_binary_lookup_mode(True)
				print ip,':',st[socket.inet_aton(ip)]
			else:
				print ip,':','No matching prefix found'
def pass_ip(ip):
	if ip in st:
		st.set_binary_lookup_mode(True)
		print ip,':',st[socket.inet_aton(ip)]
	else:
		print ip,':','No matching prefix found'

pass_ipfile(ip_file)
