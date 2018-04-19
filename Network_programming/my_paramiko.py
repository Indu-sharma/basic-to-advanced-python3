import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def noninteractive_paramiko():
    ssh.connect('192.168.112.1', port=22, username='root', password='root@123')
    stdin, stdout, stderr = ssh.exec_command('ls -lrt')
    print(stdout.readlines())
    ssh.close()


def interactive_paramiko():
    """To Make Interactive just use stdin"""

    ssh.connect('192.168.112.1', port=22, username='root', password='root@123')
    stdin, stdout, stderr = ssh.exec_command('ls -lrt')
    stdin.write('yes')
    stdin.write('\n')
    stdin.flush()

    print(stdout.readlines())

    ssh.close()


def channel_paramiko():
    ssh.connect('192.168.112.1', port=22, username='root', password='root@123')
    channel = ssh.invoke_shell()
    channel_data = str()
    while True:
        if channel.recv_ready():
            channel_data += channel.recv(9999)
        else:
            continue
        if channel_data.endswith('root#'):
            channel.send('ls -rlt')
        elif channel_data.endswith('[]?'):
            host = raw_input('Enter the Host:')
            channel.send(host)
            channel.send('\n')
        elif '(Timed Out)' in channel_data:
            channel_data = ''
        elif 'q' in channel_data:
            break
    ssh.close()
