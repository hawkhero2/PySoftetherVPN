import json
import subprocess
import customtkinter
from libs.error_handle import has_error

setting_file : dict = json.load(open("libs/settings.json"))
window_size = setting_file.get("window_size")

class EditConnection(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        
        self.title("Settings")
        self.geometry(window_size)
        self.resizable(False,False)

        self.connection_name = customtkinter.CTkEntry(self)
        self.connection_name.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.connection_name._textvariable="test" # TODO fix this

        self.account = customtkinter.CTkEntry(self)
        self.account.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.account._textvariable="test"

        self.password = customtkinter.CTkEntry(self)
        self.password.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.password._textvariable="test"

        self.vpn = customtkinter.CTkEntry(self)
        self.vpn.grid(row=3,column=0, padx=20, pady=20, sticky="ew" )

        self.nic = customtkinter.CTkEntry(self)
        self.nic.grid(row=4,column=0, padx=20, pady=20, sticky="ew" )
        self.nic._textvariable="test"

        self.save_btn= customtkinter.CTkButton(self, text="Connect", state="disabled",command=self.save)
        self.save_btn.grid(row=5, column=0, padx=20, pady=20, sticky="ew")


    def save(self):
        setting_file :dict=json.load(open("libs/settings.json"))
        vpn_name:str = setting_file["vpn_name"]
        inputs = [
            "2\n",
            "localhost\n",
            "AccountUsernameSet\n",
            self.connection_name.get()+"\n",
            self.account.get()+"\n"
            ]
        command=subprocess.Popen(["vpncmd"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        # TODO check error message

        inputs.clear()

        inputs = [
            "2\n",
            "localhost\n",
            "AccountPasswordSet\n",
            self.connection_name.get()+"\n",
            self.password.get()+"\n",
            self.password.get()+"\n",
            "standard\n"
            ]

        inputs.clear()

        self.withdraw()
