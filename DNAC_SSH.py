#DNAC SSH with paramiko
# coding=utf-8
import paramiko
import sys

host = 'IP'
username = 'maglev' 
port = 2222
password = 'PASSWORD'
command = 'maglev package status \n'
command1 = 'GUI_USERNAME \n GUI_PASSOWORD\n'
#command1 = 'magctl appstack status \n'

try:
    client = paramiko.SSHClient()
        #client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname=host, username=username, password=password, port=port)
    print('Logged in DNAC. . .\n')
    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    stdin.write(command1)
    stdin.flush()
    for line in stdout:
        print (line.strip('\n'))

except SSHException:
    client.close()

finally:
    client.close()
    print ('Connection closed. . .\n')

