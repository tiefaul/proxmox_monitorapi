# Proxmox Server Monitoring Script

This Python script monitors CPU and memory usage on a Proxmox server and its LXC containers. It uses the Proxmoxer library to interact with the Proxmox API.

## Features

- Retrieves the node's current CPU and memory usage
- Retrieves the LXC container's CPU and memory usage
- Displays statistics such as:
  - Max CPU and memory capacity
  - Current usage percentages
  - Node and container statuses

## Requirements

- Python 3.x
- Proxmoxer library: ```pip install proxmoxer```
- python-dotenv library: ```pip install python-dotenv```

## Setup

1. Clone the repository or download the script.
2. Install the libraries mentioned above.
3. Create a .env file in the same directory as the script with the following enviornment variables:

```env
IP = <yourIP>
USER = <Your Proxmox username>
PASSWORD = <Your Proxmox password>
```

## Usage

Run the script with Python:

```bash
python proxmox_monitor.py
```

## Example Output

```yaml
Nodes:
node1 => online
  MaxCPU: 8
  MaxMem: 16
  CPU Usage: 23.4 %
  Mem Usage: 12.5%

Containers:
101. container1 => running
  MaxCPU: 2
  MaxMem: 4
  CPU Usage: 10.2%
  Mem Usage: 38.7 %
```

---

This script is designed to be a starting point for monitoring your Proxmox cluster. You can customize this however you would like.
