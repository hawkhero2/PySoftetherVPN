#!/usr/bin/env python3

import os
import tkinter
import customtkinter
import json
from main_window import Main
from settings_window import Settings


main = Main
settings = Settings 


def get_conn_status():
    status : bool = True
    return status

connection_status :  bool = get_conn_status()

nic_name = ""

credentials = {
    "acc":"",
    "pw":""
}

settings.save_creds(settings ,credentials=credentials)

# settings = json.load()

main.mainloop( )