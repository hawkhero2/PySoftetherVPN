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

        self.acc_input = customtkinter.CTkEntry(self, placeholder_text = "account")
        self.acc_input.place(in_ = self, relx = 0.25, rely = 0.3)

        self.pwd_input = customtkinter.CTkEntry(self, 
                                        placeholder_text = "password")
        self.pwd_input.place(in_= self, relx = 0.25, rely = 0.4)
        

        self.save_btn = customtkinter.CTkButton(master = self, 
                                        text = "Save", 
                                        command = self.save)

        self.create_nic_btn = customtkinter.CTkButton(master = self, 
                                                text = "Create",
                                                command = self.create_nic)

        self.save_btn.place(relx=0.25, rely=0.6)

        self.nic_window : customtkinter.CTkToplevel = None
        self.nic_window.place(relx=0.25, rely=0.6)
    
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
