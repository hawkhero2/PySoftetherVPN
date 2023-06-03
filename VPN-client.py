#!/usr/bin/env python3

from main_window import Main
from cryptography.fernet import Fernet
import json

settings_file : dict = json.load(open("intellexlab-files/settings.json"))
pw_input : str = "testpw"

if settings_file["key"] == "":
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_pw = f.encrypt(bytes(pw_input,"utf-8"))
    print("this is the encrypted password = "+encrypted_pw)
    print()
    settings_file.__setitem__("key", key)
    decrypted_pw = encrypted_pw
    print(settings_file)

# main =Main()
# main.mainloop()