#!/usr/bin/env python3

import json
import subprocess

settings_file : dict = json.load(open("libs/settings.json"))

adapter_name = input('Input name of the adapter to be created : ')
subprocess.run(f"echo You typed {adapter_name} for the vpn adapter name", shell=True)

if adapter_name != "" and adapter_name != settings_file["vpn_name"]:
    output = subprocess.run(f"sudo vpnclient start", shell=True, capture_output=True)
    subprocess.run(f"echo {output.stdout}")
    print("Creating adapter...")
    output = subprocess.run(f"sudo vpncmd /client localhost /client niccreate {adapter_name}", shell=True, capture_output=True)
    
    if output.returncode == 0:
        for line in output.stdout.decode().splitlines():
            subprocess.run(f"echo {line}", shell=True)
            
        settings_file["vpn_name"] = adapter_name 
        json_obj = json.dumps(settings_file, indent=5)
        subprocess.run(f"echo Saving vpn name to settings file")
        with open("libs/settings.json", "w") as outfile:
            outfile.write(json_obj)
    else:
        subprocess.run(f"echo The operation failed with the following error : {output.stdout.decode()}")
else:
    subprocess.run(f"VPN Adapter name already existent", shell=True )

# test = input('Type something: ')
# output = subprocess.run(f"echo {test}", shell=True, capture_output=True)
# print(f"this is what you typed: {output}")