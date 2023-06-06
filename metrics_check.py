import paramiko
import psutil

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="20.39.212.45", username="azureuser", password="@zureuser123", port=22)

#stdin, stdout, stderr = ssh_client.exec_command(command="sudo apt update")
#output = stdout.read().decode("utf-8")
#error = stderr.read().decode("utf-8")
#print("Output: ", output)
#print("Error: ", error)

# CPU usage
cpu_percent = psutil.cpu_percent()

# Memory usage
mem = psutil.virtual_memory()
mem_total = mem.total
mem_used = mem.used
mem_percent = mem.percent

# Disk usage
disk = psutil.disk_usage('/')
disk_total = disk.total
disk_used = disk.used
disk_percent = disk.percent

print('cpu_percent: ', cpu_percent)
print('mem_total: ', mem_total)
print('mem_used: ', mem_used)
print('mem_percent: ', mem_percent)
print('disk_total: ', disk_total)
print('disk_used: ', disk_used)
print('disk_percent: ', disk_percent)

threshold = 1

if mem > threshold:
    True
else:
    False


ssh_client.close()
