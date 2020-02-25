import paramiko
import sys
import time
import getpass

host = 'IP'
username = 'maglev' 
port = 2222
password = 'MAGLEV_PASSWORD'
command = 'maglev package status \n'
admin_user = 'USERNAME\n'
admin_pass = 'PASSWORD\n'
exit_shell = 'exit \n'
#command1 = 'magctl appstack status \n'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, port=port)
print('Logged in DNAC. . .\n')
remote_conn = client.invoke_shell()
time.sleep(.005)
output = remote_conn.recv(65535)
print output


remote_conn.send(command)
time.sleep(0.5)

#we need a condition because we might need to create a new JWT by inserting GUI creds
if "maglev-1 [main " in remote_conn.recv(1000):
	remote_conn.send(exit_shell)
	time.sleep(0.5)
else:
	remote_conn.send(admin_user)
	time.sleep(0.10)
	remote_conn.send(admin_pass)
	time.sleep(0.5)
	remote_conn.send(exit_shell)
	time.sleep(0.5)

output = remote_conn.recv(65535)
print output

remote_conn.transport.close()