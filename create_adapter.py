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

    splitted_output = output.stdout.decode().splitlines()
    
    error=["",""]
    # Looking for the Error in the stdout
    for line in splitted_output:
        index = 0
        if(line.__contains__("Error code")):
            error[0]=splitted_output[index]
            error[1]=splitted_output[index+1]
        else:
            index=index+1
    
    if (error[0]==""):
        subprocess.run(f"echo Successfully created VPN Adapter", shell=True)
        subprocess.run("Writting name to settings", shell=True)
        settings_file["vpn_name"] = adapter_name 
        json_obj = json.dumps(settings_file, indent=5)

        with open("libs/settings.json", "a") as outfile:
            outfile.write(json_obj)
        subprocess.run(f"echo VPN Adapter {adapter_name} successfully created", shell=True)
        print("VPN Adapter name saved to libs/settings.json")

    if(error[0]!=""):
        subprocess.run(f"There was an error when creating a NIC with the name {adapter_name}", shell=True)

else:
    subprocess.run(f"echo VPN Adapter name already existent", shell=True)