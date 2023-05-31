import os
import customtkinter
import os

creds = customtkinter.CTk() 
creds.geometry("500x250")
creds.title("VPN")
creds.withdraw()

def create_nic():
    os.system("vpncmd /")
    pass

def save_creds(credentials : dict):
    # print("You connected " + acc_input.get())
    credentials.__setitem__("acc", acc_input.get())
    credentials.__setitem__("pw", pwd_input.get())

    print("your login credentials are: acc:"+
          credentials.get("acc")+
          " with the password: "+credentials.get("pw"))
    
    creds.withdraw()
    vpn_status.iconify()

acc_input = customtkinter.CTkEntry(creds, placeholder_text = "account")
acc_input.place(in_ = creds, relx = 0.25, rely = 0.3)

pwd_input = customtkinter.CTkEntry(creds, 
                                   placeholder_text = "password")
pwd_input.place(in_= creds, relx = 0.25, rely = 0.4)


save_btn = customtkinter.CTkButton(master = creds, 
                                 text = "Save", 
                                 command = save_creds)

create_nic_btn = customtkinter.CTkButton(master = creds, 
                                         text = "Create",
                                         command = create_nic)

save_btn.place(relx=0.25, rely=0.6)

creds.resizable(False,False)