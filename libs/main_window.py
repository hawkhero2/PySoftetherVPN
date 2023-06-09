import json
import subprocess
import customtkinter
from libs.settings_window import Settings
from libs.CTkTable import *

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")


# class TopFrame(customtkinter.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
       
#         self.grid_columnconfigure(0, weight=1)
        
#         self.connection_list =self.get_connections()
#         self.option_menu = customtkinter.CTkOptionMenu(self, width = 150, height = 34, 
#                                                     values = self.connection_list, 
#                                                     command = self. select_connection)

#         self.option_menu.grid(column = 0, sticky = "ew")

#     def get_connections(self):
#         connections = setting_file.get("connections") 
#         return connections
        
#     def select_connection(self, choice):
#         pass


# class LowerFrame(customtkinter.CTkFrame):
#     def settings_call(self):
#         if self.settings_window is None or not self.settings_window.winfo_exists():
#             self.settings_window = Settings()
#             self.settings_window.focus()
#         else:
#             if self.settings_window.state() == "withdrawn":
#                 self.settings_window.deiconify()
        
    
#     def connect_button_cmd(self):
#         pass
    
#     def disconnect_con(self):
#         pass   
    
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight = 1)

#         self.connect_button =  customtkinter.CTkButton(self, text = "Connect", command = self.connect_button_cmd)
#         self.connect_button.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "ew")

#         self.disconect_button = customtkinter.CTkButton(self, text="Disconnect", command=self.disconnect_con)
#         self.disconect_button.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")
        
#         self.settings_button = customtkinter.CTkButton(self, text = "Settings", command = self.settings_call)
#         self.settings_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "ew" )
        
 
# class TableFrame(customtkinter.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         self.values = [["test","test2","test3"],
#                        ["test","test2","test3"]
#             ]

#         self.table = CTkTable(master=self, row = 4 , column = 3, values=self.values )
#         self.table.pack(expand=True, fill="both")
                

# Pentru a sterge virtual adapter comanda:
# sudo ip link delete <adapter_name>
class Main(customtkinter.CTk):

    # TODO https://www.youtube.com/watch?v=i2zN1IFKNYU&pp=ygUgc2V0dXAgc29mdGV0aGVyIHZwbiBjbGllbnQgbGludXg%3D
    def set_startup_conn(self):
        # not tested yet
        subprocess.run(f"vpncmd /client accountstartupset", shell=True, capture_output=True)


    def disconnect(self):
        subprocess.run(f"") 
        pass

# TODO Check correct network credentials for the vpn 
    def connect(self):
        account = self.account.get()
        vpn = self.vpn.get()
        password = self.password.get()
        # not functional
        subprocess.run(f"vpncmd /CLIENT {vpn} /CMD AccountCreate {account}", shell=True)
        subprocess.run(f"vpncmd /CLIENT {vpn} /CMD AccountPassword {password}", shell=True)

        # TODO 
        # If connection is accepted then write creds to json.
        # Else display error message window

        setting_file.__setitem__("acc",account)
        setting_file.__setitem__("vpn-id", vpn)
        json_obj = json.dumps(setting_file, indent=5)
        with open("libs/settings.json", "w") as outfile:
            outfile.write(json_obj)

        print("this is account: " +  self.account.get())
        print("this is password: " + self.password.get())
        pass

    def __init__(self):
        super().__init__()

        self.title("VPN")
        self.geometry(window_size)
        self.resizable(False,False)
        self.top_frame = customtkinter.CTkFrame(self)
        self.bottom_frame = customtkinter.CTkFrame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bottom_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.top_frame.grid_columnconfigure(0, weight=1)
        
        
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.account = customtkinter.CTkEntry(self.top_frame, placeholder_text="Account")
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.password = customtkinter.CTkEntry(self.top_frame, placeholder_text="Password", show="*")
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.vpn = customtkinter.CTkEntry(self.top_frame, placeholder_text="VPN IP")
        self.vpn.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )

        self.connect_btn = customtkinter.CTkButton(self.bottom_frame, text="Connect", command=self.connect)
        self.connect_btn.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.disconnect_btn = customtkinter.CTkButton(self.bottom_frame, text="Disconnect", command=self.disconnect)
        self.disconnect_btn.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
        self.settings_window : customtkinter.CTkToplevel = None
    