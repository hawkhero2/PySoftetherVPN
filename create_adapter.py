#!/usr/bin/env python3

import json
import subprocess

settings_file : dict = json.load(open("libs/settings.json"))

adapter_name = input("Input name of the adapter to be created : ")
sys_vp_list = subprocess.run(f"ip a | grep {adapter_name}", shell=True, capture_output=True)
sys_vp_list = sys_vp_list.stdout.decode()

if adapter_name != "" and adapter_name != settings_file["vpn_name"]:
    subprocess.run(f"sudo vpnclient start", shell=True)
    subprocess.run(f"echo Attempting to create VPN Adapter using the name: {adapter_name}", shell=True)
    output = subprocess.run(f"vpncmd /client localhost /cmd niccreate {adapter_name}", shell=True, capture_output=True)
    
    if output.returncode == 0:
        print(f"return code : {output.returncode}")
        print("Successfully created VPN Adapter")
        print("Writting name to settings")
        settings_file["vpn_name"] = adapter_name 
        json_obj = json.dumps(settings_file, indent=5)

        with open("libs/settings.json", "w") as outfile:
            outfile.write(json_obj)
        print("VPN Adapter name saved to libs/settings.json")

    if output.returncode == 30:
        subprocess.run(f"echo There is a vpn created with that name already", shell=True)
        subprocess.run(f"echo Rerun the script again with a different adapter name than: {adapter_name}", shell=True)

else:
    subprocess.run(f"echo VPN Adapter name already existent", shell=True)