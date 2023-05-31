import os
import customtkinter


def check_creds(creds : customtkinter.CTk):
    creds.iconify()
    vpn_status.withdraw()

def button_disconnect_vpn():
    cfg_file = open("softether-vpn-client/vpn_config")
    for itm in cfg_file:
        print(itm.split("=\\n"))
    
    # os.system("vpnclient stop >/dev/null 2>&1")
    print("terminating connection...")

def button_connect_vpn():
    os.system("sudo vpnclient start")
    print("connecting vpnclient...")

vpn_status = customtkinter.CTk()

vpn_status.geometry("500x250")
vpn_status.title("VPN")
vpn_status.resizable(False,False)


disconnect_btn = customtkinter.CTkButton(vpn_status, 
                                         text = "Disconnect",  
                                         command = button_disconnect_vpn)

disconnect_btn.place(relx = 0.65, rely = 0.8)
creds_btn = customtkinter.CTkButton(vpn_status, 
                                    text = "Settings", 
                                    command = check_creds)
connect_btn = customtkinter.CTkButton(vpn_status, 
                                      text = "Connect",
                                      command = button_connect_vpn)
connect_btn.place(relx = 0.35, rely = 0.8)
creds_btn.place(relx = 0.05, rely = 0.8)
