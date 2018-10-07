# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 01:49:30 2018

@author: Abhishek
"""

import faceCheck
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
from datetime import datetime


successful = []
failed = []

app = QApplication([])

window = QWidget()
window.resize(500, 200)

layoutMain = QVBoxLayout()

label = QLabel('Hello World!')
label.setText('Enter your access id below:')
label.setFont(QFont('SansSerif', 16))

box = QLineEdit()
box.setFont(QFont('SansSerif', 16))

button = QPushButton('Submit')
button.setFont(QFont('SansSerif', 16))
def on_button_clicked():
    if(faceCheck.faceCheck(box.text())):
        successful.append(box.text())
        alert = QMessageBox()
        alert.setText('Verification Successful!')
        alert.exec_()
    else:
        failed.append(box.text())
        alert = QMessageBox()
        alert.setText('You are not who you say you are. :(')
        alert.exec_()

button.clicked.connect(on_button_clicked)

layoutMain.addWidget(label)
layoutMain.addWidget(box)
layoutMain.addWidget(button)


window.setLayout(layoutMain)
window.show()
app.exec_()

# logging the attemps for later review
with open('successfulAttempts.json', 'w') as f:
    f.write(str(datetime.now()))
    json.dump(successful, f)
with open('failedAttempts.json', 'w') as f:
    f.write(str(datetime.now()))
    json.dump(failed, f)