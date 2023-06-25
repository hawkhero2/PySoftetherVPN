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
       
        self.grid_columnconfigure(0, weight=1)
        
        self.connection_list =self.get_connections()
        self.option_menu = customtkinter.CTkOptionMenu(self, width = 150, height = 34, 
                                                    values = self.connection_list, 
                                                    command = self. select_connection)

        self.option_menu.grid(column = 0, sticky = "ew")

    def get_connections(self):
        connections = setting_file.get("connections") 
        return connections
        
    def select_connection(self, choice):
        pass


class LowerFrame(customtkinter.CTkFrame):
    def settings_call(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = Settings()
            self.settings_window.focus()
        else:
            if self.settings_window.state() == "withdrawn":
                self.settings_window.deiconify()
        
    
    def connect_button_cmd(self):
        pass
    
    def disconnect_con(self):
        pass   
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.connect_button =  customtkinter.CTkButton(self, text = "Connect", command = self.connect_button_cmd)
        self.connect_button.grid(row = 0, column = 1, padx = 10, pady = 10 , sticky = "ew")

        self.disconect_button = customtkinter.CTkButton(self, text="Disconnect", command=self.disconnect_con)
        self.disconect_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.settings_button = customtkinter.CTkButton(self, text = "Settings", command = self.settings_call)
        self.settings_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "ew" )
        
 
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
        self.upper_frame = TopFrame(self)
        self.lower_frame = LowerFrame(self)
        self.upper_frame.grid(row = 0)
        self.lower_frame.grid(row = 1) 
        # self.settings_file = json.load(open("libs/settings.json"))
        # self.disconnect_btn = customtkinter.CTkButton(self, 
        #                                         text = "Disconnect",  
        #                                         command =self.button_disconnect_vpn)

       # self.disconnect_btn.place(relx = 0.65, rely = 0.8)

        # self.disconnect_btn.grid( row=2 , padx = 20, pady = 20)
        # self.connection_list =self.get_connections()
        # self.option_menu = customtkinter.CTkOptionMenu(self, width = 150, height = 34, 
        #                                                values = self.connection_list, 
        #                                                command = self. select_connection)
        # self.settings = customtkinter.CTkButton(self, 
        #                                     text = "Settings", 
        #                                     command = self.settings_open)
        # self.connect_btn = customtkinter.CTkButton(self, 
        #                                     text = "Connect",
        #                                     command = self.button_connect_vpn)
        self.settings_window : customtkinter.CTkToplevel = None
    