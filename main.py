#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap

from uis.main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Generate QR Code")
        self.setWindowIcon(QtGui.QIcon("./icons/qr-scan.png"))
        self.ui.pushButton.clicked.connect(self.generate_qr_code)

    def generate_qr_code(self):
        from datetime import datetime
        _str = self.ui.lineEdit.text()
        _file_name = str(datetime.now().time()) + ".png"
        img = qrcode.make(_str)
        img.save(_file_name)
        self.open_qr_code(_file_name)

    def open_qr_code(self, file_name):
        pixmap = QPixmap(file_name)
        self.ui.label.setPixmap(pixmap.scaled(669, 431))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
