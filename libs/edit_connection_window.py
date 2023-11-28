import json
import subprocess
import customtkinter
from libs.error_handle import has_error

class EditConnection(customtkinter.CTkToplevel):
    def save(self):
        setting_file :dict=json.load(open("libs/settings.json"))
        # vpn_name:str = setting_file["vpn_name"]
        inputs = [
            "2\n",
            "localhost\n",
            "AccountUsernameSet\n",
            self.connection_name.get()+"\n",
            self.account.get()+"\n"
            ]

        command=subprocess.Popen(["vpncmd"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)

        for value in inputs:
            command.stdin.write(value)
            command.stdin.flush()

        # TODO check error message
        out = command.communicate()
        out = out.splitlines()

        inputs.clear()

        if(has_error(out) == False):
            with open("logs.txt", "+a") as outfile:
                outfile.write("Account has been successfully updated\n")
        else:
            with open("logs.txt", "+a") as outfile:
                outfile.write("Error while updating account\n")
            pass

        inputs = [
            "2\n",
            "localhost\n",
            "AccountPasswordSet\n",
            self.connection_name.get()+"\n",
            self.password.gaaaaaaaet()+"\n",
            self.password.get()+"\n",
            "standard\n"
            ]

        command=subprocess.Popen(["vpncmd"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)

        for value in inputs:
            command.stdin.write(value)
            command.stdin.flush()
        
        out = command.communicate()
        out = out.splitlines()

        if(has_error(out) == False):
            with open("logs.txt", "+a") as outfile:
                outfile.write("Password has been successfully updated\n")
        else:
            with open("logs.txt", "+a") as outfile:
                outfile.write("Error while updating password\n")

        inputs.clear()

        inputs = [
            "2\n",
            "localhost\n",
            "accountnicset\n",
            self.connection_name.get()+"\n",
            self.nic.get()+"\n"
            ]
        
        command=subprocess.Popen(["vpncmd"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for value in inputs:
            command.stdin.write(value)
            command.stdin.flush()
        out = command.communicate()
        out = out.splitlines()

        if(has_error(out) == False):
            with open("logs.txt", "+a") as outfile:
                outfile.write("NIC has been successfully updated\n")
        else:
            with open("logs.txt", "+a") as outfile:
                outfile.write("Error while updating NIC\n")

        self.withdraw()

    def __init__(self):
        super().__init__()
 
        setting_file : dict = json.load(open("libs/settings.json"))
        window_size = setting_file.get("window_size")
       
        self.title("Settings")
        self.geometry(window_size)
        self.resizable(False,False)

        self.connection_name = customtkinter.CTkEntry(self)
        self.connection_name.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.connection_name.insert(0, f"{setting_file['connection_name']}")

        self.account = customtkinter.CTkEntry(self)
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.account.insert(0, f"{setting_file['acc']}")

        self.password = customtkinter.CTkEntry(self)
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.password.insert(self.password.get())

        self.vpn_ip = customtkinter.CTkEntry(self)
        self.vpn_ip.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )
        self.vpn_ip.insert(0, f"{setting_file['vpn_ip']}")

        self.nic = customtkinter.CTkEntry(self)
        self.nic.grid(row=4,column=0, padx=20, pady=20, sticky="ew" )
        self.nic.insert(0, f"{setting_file['nic']}")

        self.save_btn= customtkinter.CTkButton(self, text="Connect", state="disabled",command=self.save)
        self.save_btn.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

        del setting_file
