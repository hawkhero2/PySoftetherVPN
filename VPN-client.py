#!/usr/bin/env python3

from libs.main_window import Main
from cryptography.fernet import Fernet
import json

settings_file : dict = json.load(open("libs/settings.json"))
pw_input : str = "testpw"


# TODO check for session token connection ( maybe refresh token)


main = Main()
main.mainloop()