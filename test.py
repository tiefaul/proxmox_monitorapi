import os
from proxmoxer import ProxmoxAPI
from dotenv import load_dotenv

load_dotenv()

proxmox = ProxmoxAPI(os.getenv("IP"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), verify_ssl=False)

print(proxmox.nodes('dellr620').hardware.usb.get())