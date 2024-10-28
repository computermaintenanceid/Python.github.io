#########################################################
# Nama file: MainForm.py
#########################################################

from PyQt5.QtWidgets import (QWidget, QGridLayout, 
     QLabel, QLineEdit, QPushButton)

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QGridLayout')

      self.label1 = QLabel('Nama')
      self.lineEdit1 = QLineEdit()
      
      self.label2 = QLabel('No. Handphone')
      self.lineEdit2 = QLineEdit()
      
      self.button1 = QPushButton('OK')
      
      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.lineEdit1, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.lineEdit2, 1, 1)
      layout.addWidget(self.button1, 2, 0, 1, 2)
      
      self.setLayout(layout)
