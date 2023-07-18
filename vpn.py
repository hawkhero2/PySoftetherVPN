#!/usr/bin/env python3

import json
import subprocess
from libs.main_window import Main


# TODO check for session token connection ( maybe refresh token)

# run command to start softether vpn, vpnclient start
subprocess.run("vpnclient start", shell=True)

# settings:dict = json.load(open("libs/settings.json"))
# connection:dict = settings.get("connection")
# connection_name = connection.get("name")
# main = Main()
# main.mainloop()
output = subprocess.run(f"vpncmd /client localhost /cmd accountlist", shell=True, capture_output=True)
print(f"This is the output of the command : {output}")
print(f"--------------")
converted_output = output.stdout.decode().splitlines(True)
print(f"This is the stdout:{converted_output}")

print(len(converted_output))
subprocess.run("vpnclient stop", shell=True)

# from index 13 starts the accountlist table
print(converted_output[13])


# subprocess.call("vpnclient start", stdout="logs.txt")
# class MainThread(QtWidgets.QWidget):
#     # Playing around with PySide
#     def __init__(self):
#         super().__init__()

#         self.button_connect = QtWidgets.QPushButton(text="test button")
#         self.button_disconnect = QtWidgets.QPushButton(text="Disconnect")
#         # self.servers = QtWidgets.Q
#         self.text = QtWidgets.QLabel(text="Test Label")
#         self.edit = QtWidgets.QLineEdit()
#         self.layout = QtWidgets.QVBoxLayout(self)

#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.edit)
#         self.layout.addWidget(self.button_connect)
        
#         self.button_connect.clicked.connect(self.magic)


#     @QtCore.Slot()
#     def magic(self):
#         self.text.setTex(self.edit)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])        

#     widget = MainThread()
#     widget.resize(400,300)
#     widget.show()

#     sys.exit(app.exec())
    