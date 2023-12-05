import customtkinter

class MsgBox(customtkinter.CTkToplevel):
    def ok_btn_cmd(self):
        self.destroy()
        
    def __init__(self, msg :str, **kwargs):
        super().__init__(**kwargs)
        self.title("Notice")
        self.geometry("250x150")
        self.resizable(False,False)
        self.grid_columnconfigure(0, weight=1)

        self.msg_label = customtkinter.CTkLabel(self, text=msg)
        self.msg_btn_ok = customtkinter.CTkButton(self, state="enabled", text="OK", command=self.ok_btn_cmd)
        self.msg_label.grid(row=0, padx=10, pady=10, sticky="nsew")
        self.msg_btn_ok.grid(row=1, padx=10, pady=10, sticky="nsew")
