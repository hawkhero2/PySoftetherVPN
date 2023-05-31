#!/usr/bin/env python3

import os
import tkinter
import customtkinter
import json
import main_window
import settings_window

from typing import Optional, Tuple, Union

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def get_conn_status():
    status : bool = True
    return status

connection_status : bool = get_conn_status()

nic_name = ""

credentials = {
    "acc":"",
    "pw":""
}

settings = json.load()