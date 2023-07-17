import json
import subprocess
import customtkinter

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")

# TODO Implement grids
# TODO Refactor Settings class into Connection Settings?
class Connection(customtkinter.CTkToplevel):
        def __init__(self):
            super().__init__()
            
            self.title("Create Connection")
            self.geometry(window_size)
            self.resizable(False, False)
            self.server_gateway = customtkinter.CTkEntry(self, 
                                                         placeholder_text = "107.0.0.1")
            self.server_gateway.place()

# class Nic(customtkinter.CTkToplevel):
#     def __init__(self):
#         super().__init__()

#         self.title("Virtual Adapter Name")
#         self.geometry(window_size)
#         self.resizable(False, False)

#         self.nic_input = customtkinter.CTkEntry(self, 
#                                                 placeholder_text="Virtual Adapter Name",)

#     def create_btn(self):
#         nic_name =  self.nic_input.get()
#         subprocess.call("vpncmd /CLIENT localhost /CMD NicCreate "+nic_name)

class Settings(customtkinter.CTkToplevel):
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

    def create_nic(self):
        pass

    def save(self):
        # print("You connected " + acc_input.get())
        setting_file.__setitem__("acc",self.acc_input.get())
        self.settings_file.__setitem__("pw", self.pwd_input.get())

        print("your login settings_file are: acc:"+
            self.settings_file.get("acc")+
            " with the password: "+self.settings_file.get("pw"))
        self.withdraw()
