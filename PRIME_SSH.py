#PRIME SSH paramiko
import paramiko
import sys

host = 'IP'
username = ‘USERNAME'
port = 22
password = ‘PASSWORD’
command = ‘show clock\n'
command2 =  'exit\n'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, port=port)
print('Logged in Prime. . .\n')
stdin, stdout, stderr = client.exec_command( 'password ', get_pty=True)
stdin.write(command)
stdin.write(command2)
print(stdout.readline())
stdin.flush()
for line in stdout:
    print (line.strip('\n'))
#print (client.get_transport().is_active())

#client.close()
#print ('Connection closed. . .\n')
