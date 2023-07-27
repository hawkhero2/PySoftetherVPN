#!/usr/bin/env python3

import json
import subprocess
from libs.main_window import Main

# TODO check for session token connection ( maybe refresh token)

# run command to start softether vpn, vpnclient start
# output = subprocess.run("vpnclient stop", shell=True, capture_output=True)
# if output.stdout.decode().splitlines()[0] == "SoftEther VPN Client service has not yet been started.":
#     subprocess.run("vpnclient start", shell=True)
# output = subprocess.run(f"ip a | grep vpn", shell=True, capture_output=True)
# if output.returncode == 0:
#     print(output.stdout.decode())

# settings:dict = json.load(open("libs/settings.json"))
# connection:dict = settings.get("connection")
# connection_name = connection.get("name")


main = Main()
main.mainloop()

# output = subprocess.run(f"vpncmd /client localhost /cmd accountlist", shell=True, capture_output=True)
# print(f"This is the output of the command : {output}")
# print(f"--------------")
# converted_output = output.stdout.decode().splitlines(True)
# print(f"This is the stdout:{converted_output}")


# with open("logs.txt", "a") as f:
#     f.writelines(converted_output)
# print(len(converted_output))
# subprocess.run("vpnclient stop", shell=True)
