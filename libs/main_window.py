import json
import subprocess
import customtkinter
from libs.settings_window import Settings
from libs.CTkTable import *

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")

# TODO Implement grids
# TODO Use subprocess instead of os.system, to catch output of terminal(catch_output=true)
# TODO Figure out managing outputs from subprocess calls/runs
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("VPN")
        self.geometry(window_size)
        self.resizable(False,False)

        self.settings_file = json.load(open("libs/settings.json"))
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
        # self.connections_view = TableFrame()
        
        self.values = [["test","test2","test3"],
                       ["test","test2","test3"]
            ]

        self.frame = customtkinter.CTkFrame(self, width = 250, height = 150)
        self.frame.place(relx = 0.1, rely = 0.1)
        self.table = CTkTable(self.frame, row = 4 , column = 3, values=self.values )
        self.table.pack(expand=True, fill="both")
        self.settings_window : customtkinter.CTkToplevel = None
    
    def settings_open(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = Settings()
            self.settings_window.focus()
        else:
            if self.settings_window.state() == "withdrawn":
                self.settings_window.deiconify()
        

    def button_disconnect_vpn(self):
        # os.system("vpnclient stop >/dev/null 2>&1")
        print("terminating connection...")

    def button_connect_vpn(self):
        # WIP
        subprocess.run("vpnclient start", capture_output = True)
        print("connecting vpnclient...")