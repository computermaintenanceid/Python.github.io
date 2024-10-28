#!/usr/bin/python3

#########################################################
# Nama file: DemoQCheckBox1.py
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
      self.resize(300, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QCheckBox')
      
      self.label = QLabel()
      self.label.setText('Nama file:')
      
      self.fileName = '/home/budi/pyqt/DemoQCheckBox1.py'
      
      self.lineEdit = QLineEdit(self.fileName)
      self.fullPathCheck = QCheckBox()
      self.fullPathCheck.setText('Nama file disertai path lengkap')
      self.fullPathCheck.setChecked(True)
            
      layout = QVBoxLayout()
      layout.addWidget(self.label)
      layout.addWidget(self.lineEdit)
      layout.addWidget(self.fullPathCheck)      
      layout.addStretch()
      self.setLayout(layout)
      
      self.fullPathCheck.clicked.connect(self.fullPathCheckClick)
      
   def fullPathCheckClick(self):
      if self.fullPathCheck.isChecked():
         self.lineEdit.setText(self.fileName)
      else:
         import ntpath
         s = ntpath.basename(self.fileName)
         self.lineEdit.setText(s)

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
