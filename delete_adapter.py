#!/usr/bin/env python3

import subprocess

vpn_name = input("Type name of the VPN Adapter to be deleted")

output = subprocess.run(f"ip a | grep vpn_{vpn_name}", shell=True, capture_output=True)
print(output.returncode)

if output.returncode == 0:
    subprocess.run(f"echo There is no vpn adapter with that name")
else:
    output = subprocess.run(f"sudo ip link delete vpn_{vpn_name}", shell=True, capture_output=True)
    print(output.stdout.decode())
print(output.stdout.decode())