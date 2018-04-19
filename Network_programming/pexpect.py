import pexpect
child = pexpect.spawn ('telnet 192.168.112.1)
child.expect ('Name .*: ')
child.sendline ('root')
child.expect ('Password:')
child.sendline ('noah@example.com')
child.expect ('ftp> ')
child.sendline ('ls /tmp/files/')
child.expect ('ftp> ')
print child.before # Read the results of the Output.    
child.interact()       # Get the control back to User.
