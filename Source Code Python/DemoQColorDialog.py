#!/usr/bin/python3

#########################################################
# Nama file: DemoQColorDialog.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):

   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(500, 450)
      self.move(300, 300)
      self.setWindowTitle('Demo QColorDialog')
      
      self.textEdit = QTextEdit()
      
      self.colorButton = QPushButton('Warna')
      hbox = QHBoxLayout()
      hbox.addWidget(self.colorButton)
      hbox.addStretch()
                        
      layout = QVBoxLayout()
      layout.addWidget(self.textEdit)
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.colorButton.clicked.connect(self.colorButtonClick)

   def colorButtonClick(self):
      color = QColorDialog.getColor(Qt.black, self, 'Pilih warna')      
      if color:
         self.textEdit.setTextColor(color)

if __name__ == '__main__':
   a = QApplication(sys.argv)

   form = MainForm()
   form.show()
   
   a.exec_()
