import json
import os
import customtkinter
from libs.settings_window import Settings

# TODO Implement grids
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("VPN")
        self.geometry("500x250")
        self.resizable(False,False)

        self.settings_file = json.load(open("intellexlab-files/settings.json"))
        self.disconnect_btn = customtkinter.CTkButton(self, 
                                                text = "Disconnect",  
                                                command =self.button_disconnect_vpn)

        self.disconnect_btn.place(relx = 0.65, rely = 0.8)
        
        self.settings = customtkinter.CTkButton(self, 
                                            text = "Settings", 
                                            command = self.settings_open)
        self.connect_btn = customtkinter.CTkButton(self, 
                                            text = "Connect",
                                            command = self.button_connect_vpn)
        self.connect_btn.place(relx = 0.35, rely = 0.8)
        self.settings.place(relx = 0.05, rely = 0.8)
        self.settings_window : customtkinter.CTkToplevel = None
    
    def settings_open(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = Settings()
            self.settings_window.focus()
        else:
            if self.settings_window.state() == "withdrawn":
                self.settings_window.deiconify()
        

    def button_disconnect_vpn(self):
        cfg_file = open("softether-vpn-client/vpn_config")
        for itm in cfg_file:
            print(itm.split("=\\n"))
        
        # os.system("vpnclient stop >/dev/null 2>&1")
        print("terminating connection...")

    def button_connect_vpn(self):
        os.system("sudo vpnclient start")
        print("connecting vpnclient...")