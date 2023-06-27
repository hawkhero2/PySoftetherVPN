#!/usr/bin/env python3

import sys
from PySide6 import QtCore, QtWidgets, QtGui 

# from libs.main_window import Main


# # TODO check for session token connection ( maybe refresh token)

# main = Main()
# main.mainloop()

class MainThread(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hey A", "Hey B"]

        self.button = QtWidgets.QPushButton(text="test button")
        self.text = QtWidgets.QLabel(text="Test Label")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText("text from button function")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])        

    widget = MainThread()
    widget.resize(400,300)
    widget.show()

    sys.exit(app.exec())
    