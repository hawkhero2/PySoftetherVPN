import os
import customtkinter

class Settings(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x250")
        self.title("VPN")
        self.withdraw()
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

    
    def create_nic():
        os.system("vpncmd /")
        pass

    def save(self, credentials : dict):
        # print("You connected " + acc_input.get())
        credentials.__setitem__("acc",self.acc_input.get())
        credentials.__setitem__("pw", self.pwd_input.get())

        print("your login credentials are: acc:"+
            credentials.get("acc")+
            " with the password: "+credentials.get("pw"))
        
