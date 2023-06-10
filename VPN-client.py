#!/usr/bin/env python3

from libs.main_window import Main
from cryptography.fernet import Fernet
import json


# TODO check for session token connection ( maybe refresh token)

main = Main()
main.mainloop()