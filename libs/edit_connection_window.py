import json
import subprocess
import customtkinter

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")

class EditConnection(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        
        self.title("Settings")
        self.geometry(window_size)
        self.resizable(False,False)

        self.account = customtkinter.CTkEntry(self.top_frame, placeholder_text="Account")
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.password = customtkinter.CTkEntry(self.top_frame, placeholder_text="Password", show="*")
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.vpn = customtkinter.CTkEntry(self.top_frame, placeholder_text="VPN IP")
        self.vpn.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )

        self.connect_btn = customtkinter.CTkButton(self.bottom_frame, text="Connect", state="disabled",command=self.connect)
        self.connect_btn.grid(row=3, column=0, padx=20, pady=20, sticky="ew")


    def save(self):
       self.withdraw()
