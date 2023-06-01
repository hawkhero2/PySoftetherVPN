#!/usr/bin/env python3

import os
import tkinter
import customtkinter
import json
import main_window
import settings_window


# settings = settings_window.Settings()
main = main_window.Main()


def get_conn_status():
    status : bool = True
    return status

connection_status :  bool = get_conn_status()

nic_name = ""

credentials = {
    "acc":"",
    "pw":""
}

# settings.save(credentials=credentials)
# settings = json.load()

main.mainloop()