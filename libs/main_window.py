import json
import subprocess
import customtkinter
from libs.settings_window import Settings
from libs.CTkTable import *

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")


class TopFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.connection_list =self.get_connections()
        self.option_menu = customtkinter.CTkOptionMenu(self, width = 150, height = 34, 
                                                    values = self.connection_list, 
                                                    command = self. select_connection)

        self.option_menu.grid(row = 0, column = 0, padx = 10, pady = 10)

    def get_connections(self):
        connections = setting_file.get("connections")        
        return connections
        
    def select_connection(self, choice):
        pass


class LowerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.button = customtkinter.CTkButton(self, width=140, height=70)
        self.button.grid(row = 0, column = 0, padx = 10, pady = 10) 
        

# class TableFrame(customtkinter.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         self.values = [["test","test2","test3"],
#                        ["test","test2","test3"]
#             ]

#         self.table = CTkTable(master=self, row = 4 , column = 3, values=self.values )
#         self.table.pack(expand=True, fill="both")
                

# TODO Implement grids
# TODO Use subprocess instead of os.system, to catch output of terminal(catch_output=true)
# TODO Figure out managing outputs from subprocess calls/runs
class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("VPN")
        self.geometry(window_size)
        self.resizable(False,False)
        self.grid_rowconfigure(2, weight = 1)
        self.upper_frame = customtkinter.CTkFrame(self)
        self.lower_frame = customtkinter.CTkFrame(self)
        
        self.settings_file = json.load(open("libs/settings.json"))
        self.disconnect_btn = customtkinter.CTkButton(self, 
                                                text = "Disconnect",  
                                                command =self.button_disconnect_vpn)

        # self.disconnect_btn.place(relx = 0.65, rely = 0.8)
        self.disconnect_btn.grid( row=2 , padx = 20, pady = 20)
        self.connection_list =self.get_connections()
        self.option_menu = customtkinter.CTkOptionMenu(self, width = 150, height = 34, 
                                                       values = self.connection_list, 
                                                       command = self. select_connection)
        self.settings = customtkinter.CTkButton(self, 
                                            text = "Settings", 
                                            command = self.settings_open)
        self.connect_btn = customtkinter.CTkButton(self, 
                                            text = "Connect",
                                            command = self.button_connect_vpn)
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

    # def get_connections(self):
    #     connections = setting_file.get("connections")        
    #     return connections
        
    # def select_connection(self, choice):
    #     pass

    def button_connect_vpn(self):
        # WIP
        subprocess.run("vpnclient start", capture_output = True)
        print("connecting vpnclient...")