import json
import subprocess
import customtkinter

settings_file:dict = json.loads(open("libs/settings.json"))
window_size = settings_file.get("window_size")

class Connection(customtkinter.CTkToplevel):
    def create_connection(self):
        subprocess.run(f"vpncmd /client localhost /cmd niccreate vpn")

        if(self.account.get() !="" & self.password.get() !="" & self.vpn.get() !=""):
            subprocess.run(f"vpncmd /client localhost /cmd accountcreate {self.account.get()}")
            subprocess.run(f"vpncmd /client localhost /cmd accountPassword {self.password.get()}") 
        


    def __init__(self):
        super().__init__()

        self.title("Create Connection")
        self.geometry(window_size)
        self.resizable(False,False)
 
        self.base_frame = customtkinter.CTkFrame(self)

        self.account = customtkinter.CTkEntry(self.base_frame, placeholder_text="Account")
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.password = customtkinter.CTkEntry(self.base_frame, placeholder_text="Password", show="*")
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.vpn = customtkinter.CTkEntry(self.base_frame, placeholder_text="VPN IP")
        self.vpn.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )
