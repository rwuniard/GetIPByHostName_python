import socket

textFile = open('./machinelist.txt')

machine_names = textFile.read().splitlines()
print(machine_names)

for machine_name in machine_names:
    try:
        ip_address = socket.gethostbyname(machine_name)
        print(machine_name + ' ' + ip_address)
    except socket.gaierror:
        print(machine_name + ' host cannot be resolved')

        