#DNAC SSH with paramiko
# coding=utf-8
import paramiko

host = 'IP'
username = 'maglev' 
port = 2222
password = 'PASSWORD'
command = 'magctl appstack status \n'

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    print('Logged in DNAC. . .\n')
    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    stdin.flush()
    for line in stdout:
        print (line.strip('\n'))

except SSHException:
    client.close()

finally:
    client.close()
    print ('Connection closed. . .\n')
