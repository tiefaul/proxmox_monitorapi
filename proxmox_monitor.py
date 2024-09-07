#! Python3

import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI
# import argparse

# load the .env file
load_dotenv()

# ----Create ArgumentParser object----
# parse = argparse.ArgumentParser()

# ----Add a new argument (password) to the parser (help is a parameter that specifies a help message)----
# parse.add_argument("--password", help='your an idiot')


# ----Add a new argument (password) to the parser (help is a parameter that specifies a help message)----
# parse.add_argument("--password", help='your password')

# ----Parse the command line argument and store them in the args object----
# arguments = parse.parse_args()

# ----Retrieve the value of the --password argument from the args object and store it in password variable----
# password = arguments.password

proxmox = ProxmoxAPI(os.getenv("IP"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), verify_ssl=False)

# print(proxmox.nodes.get())
# print("")
# print(proxmox.nodes("dellr620").lxc.get())

    
for nodes in proxmox.nodes.get():
    print('{0}:'.format(nodes['node']))
    for container in proxmox.nodes(nodes['node']).lxc.get():
        print('{0}. {1} => {2}'.format(container['vmid'], container['name'], container['status']))