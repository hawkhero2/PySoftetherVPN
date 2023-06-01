import os
import customtkinter
import tkinter
from settings_window import Settings

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x250")
        self.title("VPN")
        self.resizable(False,False)
        # self.set_appearance_mode("System")
        # self.set_default_color_theme("blue")

        self.settings_window : customtkinter.CTkToplevel = None

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
    
    def settings_open(self):
        # self.settings_window.iconify()
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = Settings(self)
        else:
            self.settings_window.focus()
        self.withdraw()

    def button_disconnect_vpn(self):
        cfg_file = open("softether-vpn-client/vpn_config")
        for itm in cfg_file:
            print(itm.split("=\\n"))
        
        # os.system("vpnclient stop >/dev/null 2>&1")
        print("terminating connection...")

    def button_connect_vpn(self):
        os.system("sudo vpnclient start")
        print("connecting vpnclient...")