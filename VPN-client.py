#!/usr/bin/env python3

# import sys
# from PySide6 import QtCore, QtWidgets, QtGui

from libs.main_window import Main


# TODO check for session token connection ( maybe refresh token)

main = Main()
main.mainloop()

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
    