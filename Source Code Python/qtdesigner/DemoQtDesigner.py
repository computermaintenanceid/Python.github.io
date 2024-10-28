#!/usr/bin/python3

#########################################################
# Nama file: DemoQtDesigner.py
#########################################################

import sys

from hello_ui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QDialog):
   def __init__(self, parent=None):
      QDialog.__init__(self, parent)
      self.ui = Ui_Dialog()
      self.ui.setupUi(self)
      self.ui.helloButton.clicked.connect(self.helloButtonClick)

   def helloButtonClick(self):
      QMessageBox.information(self, 'Demo Qt Designer',
         'Hallo %s, apa kabar?' % self.ui.nameEdit.text())

if __name__ == "__main__":
   #QApplication.setStyle('plastique')
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
