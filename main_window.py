import os
import customtkinter


class Main(customtkinter.CTk):
    def __init__(self):
        super.__init__()

        self.geometry("500x250")
        self.title("VPN")
        self.resizable(False,False)
                
        self.set_appearance_mode("System")
        self.set_default_color_theme("blue")


        self.disconnect_btn = customtkinter.CTkButton(self, 
                                                text = "Disconnect",  
                                                command =self.button_disconnect_vpn)

        self.disconnect_btn.place(relx = 0.65, rely = 0.8)
        creds_btn = customtkinter.CTkButton(self, 
                                            text = "Settings", 
                                            command = self.check_creds)
        connect_btn = customtkinter.CTkButton(self, 
                                            text = "Connect",
                                            command = self.button_connect_vpn)
        connect_btn.place(relx = 0.35, rely = 0.8)
        creds_btn.place(relx = 0.05, rely = 0.8)
    
    def check_creds(self, creds : customtkinter.CTk):
        creds.iconify()
        self.withdraw()

    def button_disconnect_vpn():
        cfg_file = open("softether-vpn-client/vpn_config")
        for itm in cfg_file:
            print(itm.split("=\\n"))
        
        # os.system("vpnclient stop >/dev/null 2>&1")
        print("terminating connection...")

    def button_connect_vpn():
        os.system("sudo vpnclient start")
        print("connecting vpnclient...")