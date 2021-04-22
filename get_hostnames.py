from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.load_host_keys("C:/Users/Admin/.ssh/known_hosts")
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()

client.connect('127.0.0.1',10000, username='admin',password='admin')

# Run a command (execute PHP interpreter)
#client.exec_command('hostname')
stdin, stdout, stderr = client.exec_command('en')
# print(stdout.read())

stdin.write('show running-config')
stdin.channel.shutdown_write()
if stdout.channel.recv_exit_status() == 0:
    print(f'STDOUT: {stdout.read().decode("utf8")}')
else:
    print(f'STDERR: {stderr.read().decode("utf8")}')

stdin.close()
stdout.close()
stderr.close()
client.close()
