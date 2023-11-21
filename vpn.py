#!/usr/bin/env python3

import json
import subprocess
from libs.main_window import Main

# to run vpnclient start without error: sudo chmod -R 777 /usr/libexec

# run command to start softether vpn, vpnclient start

output = subprocess.run("vpnclient start", shell=True, capture_output=True)

if(output.stdout.splitlines()[0]=="SoftEther VPN Client service has been already started."):
    subprocess.run("vpnclient stop", shell=True)
    subprocess.run("vpnclient start", shell=True)
else:
    subprocess.run("vpnclient start", shell=True)

main = Main()
main.mainloop()

subprocess.run("vpnclient stop", shell=True)
