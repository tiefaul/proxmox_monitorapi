#! Python3

import pprint
import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
# import argparse

# load the .env file
load_dotenv()

# ----Create ArgumentParser object----
# parse = argparse.ArgumentParser()

# ----Add a new argument (password) to the parser (help is a parameter that specifies a help message)----
# parse.add_argument("--password", help='your password')

# ----Add a new argument (password) to the parser (help is a parameter that specifies a help message)----
# parse.add_argument("--password", help='your password')

# ----Parse the command line argument and store them in the args object----
# arguments = parse.parse_args()

# ----Retrieve the value of the --password argument from the args object and store it in password variable----
# password = arguments.password

proxmox = ProxmoxAPI(os.getenv("IP"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), verify_ssl=False)

# pprint.pp(proxmox.nodes.get())
# print("")
# pprint.pp(proxmox.nodes('dellr620').lxc.get())

# Create percentage calculations
nodeDictionary = proxmox.nodes.get()[0]
NodeCpuPercentage = float(nodeDictionary['cpu']) / float(nodeDictionary['maxcpu']) * 100
NodeRamPercentage = float(nodeDictionary['mem']) / float(nodeDictionary['maxmem']) * 100
for stats in proxmox.nodes.get():
    print('Nodes:')
    print('{0} => {1} \n\tCPU Usage: {2} % \n\tRAM Usage: {3} %'.format(stats['node'], stats['status'], NodeCpuPercentage, NodeRamPercentage))
    for container in proxmox.nodes(stats['node']).lxc.get():
        print('\t\tContainers:')
        print('\t\t{0}. {1} => {2}'.format(container['vmid'], container['name'], container['status']))