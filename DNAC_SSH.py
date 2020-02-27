#DNAC SSH with paramiko
# coding=utf-8
import paramiko

host = 'IP'
username = 'maglev' 
port = 2222
password = 'PASSWORD'
command = 'magctl appstack status \n'

command = 'magctl appstack status \n'
command1 = 'logout \n'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, port=port)
print('Logged in DNAC. . .\n')
stdin, stdout, stderr = client.exec_command(command, get_pty=True)
stdin.write(command1)
stdin.flush()
for line in stdout:
    print (line.strip('\n'))
#client.close()
