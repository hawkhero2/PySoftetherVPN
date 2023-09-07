#!/usr/bin/env python3

import json
import subprocess
import customtkinter
from libs.msg_box import MsgBox

settings_file:dict = json.load(open("libs/settings.json"))
window_size = settings_file.get("window_size")

class Connection(customtkinter.CTkToplevel):

    def create_connection(self):
        vpn_name :str  = settings_file["vpn_name"]
        inputs = [
            "2\n",
            "localhost\n",
            "accountcreate\n",
            self.connection_name.get()+"\n",
            self.vpn.get()+"\n",
            self.connection_name.get()+"\n",
            self.account.get()+"\n",
            vpn_name+"\n"
            ]

        pw_inputs = [
            "2\n",
            "localhost\n",
            "accountpasswordset\n",
            self.connection_name.get()+"\n",
            self.password.get()+"\n",
            self.password.get()+"\n",
            "standard\n"
            ]

        if(self.connection_name.get() != "" and self.account.get() !="" and self.password.get() != "" and self.vpn.get() !=""):
            command = subprocess.Popen(["vpncmd"], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)

            for value in inputs:
                command.stdin.write(value)
                command.stdin.flush()
            
            out, err = command.communicate()
            error = ("","")
            out = out.splitlines()
            index=0
            for line in out:
                if(line.__contains__("Error code")):
                    error[0] = out[index]              
                    error[1] = out[index+1]
                else:
                    index=index+1

            if(error[0] == ""):
                pw_command = subprocess.Popen(["vpncmd"], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)

                for value in pw_inputs:
                    pw_command.stdin.write(value)
                    pw_command.stdin.flush()
                
                out, err = pw_command.communicate()
                error = ("", "")
                index=0
                for line in out:
                    if(line.__contains__("Error code")):
                        error[0] = out[index]
                        error[1] = out[index+1]
                    else:
                        index=index+1

                if(error[0] == ""):
                    msg_window = MsgBox("Connection successfully created.")
                    self.destroy()
                    
                    settings_file["connection_name"]=self.connection_name.get()
                    settings_file["acc"]=self.account.get()
                    settings_file["pw"]=self.password.get()
                    settings_file["vpn_ip"]=self.vpn.get()
                    
                    json_dump = json.dump(settings_file, indent=5)

                    with open("libs/settings.json", "w") as outfile:
                        outfile.write(json_dump)
                else:
                    msg_window = MsgBox(error[1])
                    with open("/logs.txt", "w") as outfile:
                        outfile.write(error[1])
            else:
                msg_window = MsgBox(error[1])
        else:
            msg_window = MsgBox(msg="Fill in all the fields")

    def __init__(self):
        super().__init__()

        self.title("Create Connection")
        self.geometry(window_size)
        self.resizable(False,False)
 
        # self.base_frame = customtkinter.CTkFrame(self)

        self.connection_name = customtkinter.CTkEntry(self, placeholder_text="Name for connection", width=410)
        self.connection_name.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.account = customtkinter.CTkEntry(self, placeholder_text="Account")
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.password = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.vpn = customtkinter.CTkEntry(self, placeholder_text="VPN IP")
        self.vpn.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )

        self.create_con_btn = customtkinter.CTkButton(self, text="Create",state="enabled", command=self.create_connection)
        self.create_con_btn.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
