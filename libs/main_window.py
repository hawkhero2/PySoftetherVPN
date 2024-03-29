import json
import subprocess
from tkinter import StringVar
import customtkinter
from libs.edit_connection_window import EditConnection
from libs.connection import *
# Pentru a sterge virtual adapter comanda:
# sudo ip link delete <adapter_name>
class Main(customtkinter.CTk):
# TODO Look into: https://github.com/SoftEtherVPN/SoftEtherVPN/blob/8cde81215753ad77511af43e904071b506731bc7/src/Mayaqua/Unix.c#L830

    def create_connection_window(self):
        if self.connection_window is None or not self.connection_window.winfo_exists():
            self.connection_window = Connection()
            self.connection_window.focus()
        else:
            if self.connection_window.state() == "withdrawn":
                self.connection_window.deiconify()
    
    def get_edit_btn_state(self)->str:
        state=""
        settings_file=json.load(open("settings.json", encoding="utf-8"))
        if settings_file["connection_name"] == "":
            state = "disabled"
        else:
            state = "enabled"
        return state

    def get_vpn_connection_status(self):
        output = subprocess.run("vpnclient /client localhost /cmd accountlist", shell=True, capture_output=True)
        output = output.stdout.decode().splitlines()

        status_pos = 0
        index = 0
        for line in output:
            if(line.__contains__("Status")):
                status_pos = index
            else:
               index = index+1 

        if(output[status_pos].split("|")[1] != ""):
            self.status_label = output[status_pos].split("|")[1]

    def get_connection_btn_state(self):
        settings_file=json.load(open("settings.json", encoding="utf-8"))
        state=""
        if settings_file["connection_name"] == "":
            state = "enabled"
        else :
            state = "disabled"
        return state
 
    # TODO https://www.youtube.com/watch?v=i2zN1IFKNYU&pp=ygUgc2V0dXAgc29mdGV0aGVyIHZwbiBjbGllbnQgbGludXg%3D
    def set_startup_conn(self):
        # not tested yet
        settings_file=json.load(open("settings.json"))
        subprocess.run(f"vpncmd /client accountstartupset {settings_file}", shell=True, capture_output=True)

    def edit_connection(self):
        if self.edit_connection_window is None or not self.edit_connection_window.winfo_exists():
            self.settings_window = EditConnection()
            self.settings_window.focus()
        else:
            if self.settings_window.state() == "withdrawn":
                self.settings_window.deiconify()
 

    def disconnect(self):
        settings_file = json.load(open("settings.json"))
        connection_name = settings_file["connection_name"]
        subprocess.run(f"vpncmd /client /cmd accountdisconnect {connection_name}", shell=True)

    def connect(self):
        setting_file :dict = json.load(open("settings.json"))
        output = subprocess.run(f"vpncmd /client localhost /cmd accountconnect {setting_file['connection_name']}", shell=True, capture_output=True)
        output = output.stdout.decode().splitlines()

        if(has_error(output)==False):
            msg_window = MsgBox("Connection successfull") 
            self.connect_btn.configure(state="disabled")
            self.disconnect_btn.configure(state="enabled")
            # self.disconnect_btn_state = "enabled"
            # self.disconnect_btn._state = "enabled"
        else:
            msg_window = MsgBox("Connection failed. Check logs.")
            with open("logs.txt", "a") as logsfile:
                logsfile.write(get_error(output))

    def connections_list_callback(self):
        pass
    
#   UI
    def __init__(self):
        super().__init__()

        setting_file : dict = json.load(open("settings.json"))
        window_size = setting_file.get("window_size")

        self.title("VPN")
        self.geometry(window_size)
        self.resizable(False,False)
        self.top_frame = customtkinter.CTkFrame(self)
        self.bottom_frame = customtkinter.CTkFrame(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.edit_connection_window: customtkinter.CTkToplevel = None
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
 
        self.edit_connection_btn = customtkinter.CTkButton(self.top_frame, state=f"", text="Edit Connection", command=self.edit_connection)
        self.edit_connection_btn.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.bottom_frame.grid_columnconfigure(2, weight=2)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.edit_connection_btn= customtkinter.CTkButton(self.top_frame, text="Edit Connection", state=f"{self.get_edit_btn_state()}", command=self.edit_connection)

        self.output = subprocess.run(f"vpncmd /client localhost /cmd accountlist", shell=True, capture_output=True)
        self.str_output : str = str(self.output.stdout)
        self.check_conn_status = self.str_output.splitlines()
 
        self.connect_btn = customtkinter.CTkButton(self.bottom_frame, text="Connect", state="enabled",command=self.connect, width=160)
        self.connect_btn.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.disconnect_btn = customtkinter.CTkButton(self.bottom_frame, text="Disconnect", state="disabled", command=self.disconnect, width=160)
        self.disconnect_btn.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
        del setting_file
