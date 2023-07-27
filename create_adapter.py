#!/usr/bin/env python3

import json
import subprocess

settings_file : dict = json.load(open("libs/settings.json"))

adapter_name = input('Input name of the adapter to be created : ')
if adapter_name != "":
    subprocess.run(f"sudo vpnclient start", shell=True)
    output = subprocess.run(f"sudo vpncmd /client localhost /client niccreate {adapter_name}", shell=True, capture_output=True)
    
    if output.returncode != 0:
        settings_file["vpn_name"] = adapter_name 
        json_obj = json.dumps(settings_file, indent=5)
        with open("libs/settings.json", "w") as outfile:
            outfile.write(json_obj)
    else:
        print(f"The operation failed with the following error : {output.stdout.decode()}")
else:
    print("There is already a vpn created")
