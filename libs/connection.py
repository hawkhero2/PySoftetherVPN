#!/usr/bin/env python3
import json
import subprocess
import customtkinter

settings_file:dict = json.load(open("libs/settings.json"))
window_size = settings_file.get("window_size")

class Connection(customtkinter.CTkToplevel):

    def create_connection(self):
        vpn_name :str  = settings_file["vpn_name"]
        # subprocess.run(f"vpncmd /client localhost /cmd accountcreate {self.account.get()}", shell=True)
        # subprocess.run(f"vpncmd /client localhost /cmd accountPassword {self.password.get()}", shell=True) 
        # TODO look into the following command
        # TODO use this full command instead of above one. AccountCreate represents the connection name

        if(self.connection_name.get() != "" and self.account.get() !="" and self.password.get() != "" and self.vpn.get() !=""):
            #  TODO split command into multiple inputs to terminal
            
            subprocess.run(f"vpncmd /client localhost /cmd accountcreate {self.connection_name.get()} /server {self.vpn.get()} /username {self.account.get()} /nicname {settings_file.get('vpn_name')}", shell=True)
        else:
            def msg_window_close():
                msg_window.destroy()

            msg_window = customtkinter.CTkToplevel()
            msg_window.title("Error")
            msg_window.geometry("300x150")
            msg_window.resizable(False, False)
            msg_txt = customtkinter.CTkLabel(msg_window, text="Fill in the forms")
            msg_ok = customtkinter.CTkButton(msg_window, state="enabled", text="OK", command=msg_window_close)
            msg_txt.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
            msg_ok.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

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
