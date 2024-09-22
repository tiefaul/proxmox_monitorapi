#! Python3

import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

# load the .env file
load_dotenv()

# Make API Call
proxmox = ProxmoxAPI(os.getenv("IP"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), verify_ssl=False)

# Create percentage calculations for Node
nodeDict = proxmox.nodes.get()[0]
NodeCpuPercentage = float(nodeDict['cpu']) / float(nodeDict['maxcpu']) * 100
NodeRamPercentage = float(nodeDict['mem']) / float(nodeDict['maxmem']) * 100

# Create percentage calculations for lxc container:
lxcDict = proxmox.nodes('dellr620').lxc.get()[0]
lxcCpuPercentage = float(lxcDict['cpu'])
lxcMemPercentage = float(lxcDict['mem']) / float(lxcDict['maxmem']) * 100

for stats in proxmox.nodes.get():
    print('Nodes:')
    print(f'{stats['node']} => {stats['status']}')
    print(f'    MaxCPU: {stats['maxcpu']}')
    print(f'    MaxMem: {stats['maxmem'] // 1024**3}')
    print(f'    CPU Usage: {round(NodeCpuPercentage, 2)} %')
    print(f'    Mem Usage: {round(NodeRamPercentage, 2)} %\n')
    for container in proxmox.nodes(stats['node']).lxc.get():
        print('Containers:')
        print(f'{container['vmid']}. {container['name']} => {container['status']}')
        print(f'    MaxCPU: {container["cpus"]}')
        print(f'    MaxMem: {container["maxmem"] // 1024**3}')
        print(f'    CPU Usage: {round(lxcCpuPercentage, 2)} %')
        print(f'    Mem Usage: {round(lxcMemPercentage, 2)} %')
        
# Add node disk size and lvm disk size