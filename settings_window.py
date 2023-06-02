import os
import string
from typing import Optional, Tuple, Union
import customtkinter

# TODO implement grids
class Nic(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Virtual Adapter Name")
        self.geometry("250x120")
        self.resizable(False, False)

        self.nic_input = customtkinter.CTkEntry(self, 
                                                placeholder_text="Virtual Adapter Name",)

    def create_btn(self):
        nic_name =  self.nic_input.get()
        os.system("vpncmd /CLIENT localhost /CMD NicCreate "+nic_name)

# TODO implement grids
class Settings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        self.title("Settings")
        self.geometry("500x250")
        self.resizable(False,False)

        self.credentials = {
            "acc":"",
            "pw":""
            }
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
        if self.nic_window is None or not self.nic_window.winfo_exists():
            self.nic_window = Nic()
        else:
            self.nic_window.focus()
        
        pass

    def save(self):
        # print("You connected " + acc_input.get())
        self.credentials.__setitem__("acc",self.acc_input.get())
        self.credentials.__setitem__("pw", self.pwd_input.get())

        print("your login credentials are: acc:"+
            self.credentials.get("acc")+
            " with the password: "+self.credentials.get("pw"))
        self.withdraw()        
