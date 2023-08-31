#!/usr/bin/env python3

import subprocess
output = subprocess.run("ip a | grep vpn_", shell=True, capture_output=True)
print(f"Return code : {output.returncode}")
vpn_name = input("Type name of the VPN Adapter to be deleted")

output = subprocess.run(f"ip a | grep vpn_{vpn_name}", shell=True, capture_output=True)
print(output.returncode)
if vpn_name != "":
    if output.returncode == 0:
        subprocess.run(f"echo There is no vpn adapter with that name", shell=True)
else:
    output = subprocess.run(f"sudo ip link delete vpn_{vpn_name}", shell=True, capture_output=True)
    print(output.stdout.decode())
print(output.stdout.decode())