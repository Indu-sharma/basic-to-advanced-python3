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
for ip in open(ip_file).readlines():
	st.set_binary_lookup_mode(False)
	ip = ip.strip('\n')
	if ip:
		if ip in st:
			st.set_binary_lookup_mode(True)
			print ip,':',st[socket.inet_aton(ip)]
		else:
			print ip,':','No matching prefix found'
