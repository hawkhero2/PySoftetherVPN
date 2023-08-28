import json
import subprocess
import customtkinter
from libs.settings_window import Settings
from libs.CTkTable import *
from libs.connection import *

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")

# Pentru a sterge virtual adapter comanda:
# sudo ip link delete <adapter_name>
class Main(customtkinter.CTk):

    def create_connection_window(self):
        if self.connection_window is None or not self.connection_window.winfo_exists():
            self.connection_window = Connection()
            self.connection_window.focus()
        else:
            if self.connection_window.state() == "withdrawn":
                self.connection_window.deiconify()

    def get_vpn_connection_status(self):
        # this should give status of all the exisiting connections
        output = subprocess.run("vpnclient /client localhost /cmd accountlist", shell=True, capture_output=True)
        pass
    
    def get_connection_btn_state(self):
        state=""
        if setting_file["connection_name"] == "":
            state = "enabled"
        else :
            state = "disabled"
        return state
 
    # TODO https://www.youtube.com/watch?v=i2zN1IFKNYU&pp=ygUgc2V0dXAgc29mdGV0aGVyIHZwbiBjbGllbnQgbGludXg%3D
    def set_startup_conn(self):
        # not tested yet
        subprocess.run(f"vpncmd /client accountstartupset", shell=True, capture_output=True)

    def settings_btn(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = Settings()
            self.settings_window.focus()
        else:
            if self.settings_window.state() == "withdrawn":
                self.settings_window.deiconify()
 

    def disconnect(self):
        if(subprocess.run(f"ip a|grep vpn", shell=True)==""):
            print("vpn adapter not created")
            # subprocess.run(f"") 
        else:
            print("vpn adapter already created")

# TODO Check correct network credentials for the vpn 
    def connect(self):
        account = setting_file["acc"]
        vpn = setting_file["vpn_ip"]
        password = setting_file["pw"]
        # not functional
        subprocess.run(f"vpncmd /CLIENT localhost /CMD AccountCreate {account}", shell=True)
        subprocess.run(f"vpncmd /CLIENT localhost /CMD AccountPassword {password}", shell=True)

        # TODO 
        # If connection is accepted then write creds to json.
        # Else display error message window

        setting_file["acc"] = account
        setting_file["vpn-id"] = vpn
        json_obj = json.dumps(setting_file, indent=5)

        with open("libs/settings.json", "w") as outfile:
            outfile.write(json_obj)

    def connections_list_callback(self):
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

        self.settings_window : customtkinter.CTkToplevel = None
        self.connection_window :customtkinter.CTkToplevel = None
        
        self.top_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.bottom_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.connections_label = customtkinter.CTkLabel(self.top_frame, text="Connections")
        self.connections_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.connections = [setting_file["connection_name"]]
        self.connections_list = customtkinter.CTkOptionMenu(self.top_frame, values=self.connections, command=self.connections_list_callback)
        self.connections_list.set(setting_file["connection_name"])
        self.connections_list.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
       
        self.status_label = customtkinter.CTkLabel(self.top_frame, text="Status")
        self.status_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.create_connection_btn = customtkinter.CTkButton(self.top_frame, text="Create Connection", state=self.get_connection_btn_state(), command=self.create_connection_window)
        self.create_connection_btn.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
 
        self.bottom_frame.grid_columnconfigure(2, weight=2)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.settings = customtkinter.CTkButton(self.top_frame, text="Settings", state="disabled", command=self.settings_btn)

        self.output = subprocess.run(f"vpncmd /client localhost /cmd accountlist", shell=True, capture_output=True)
        self.str_output : str = str(self.output.stdout)
        self.check_conn_status = self.str_output.splitlines()

        self.connect_btn = customtkinter.CTkButton(self.bottom_frame, text="Connect", state="enabled",command=self.connect, width=160)
        self.connect_btn.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.disconnect_btn = customtkinter.CTkButton(self.bottom_frame, text="Disconnect", state="disabled", command=self.disconnect, width=160)
        self.disconnect_btn.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
