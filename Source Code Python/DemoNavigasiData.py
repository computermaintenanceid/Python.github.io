#!/usr/bin/python3

#########################################################
# Nama file: DemoNavigasiData.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class MainForm(QWidget):
   
   recordNumber = 0
   
   def __init__(self):
      super().__init__()      
      self.model = QSqlTableModel()
      self.model.setTable('phonebook')
      self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
      self.model.select()
      self.setupUi()
      self.firstButtonClick()
      
   def setupUi(self):
      self.resize(250, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo Navigasi Data pada QSqlTableModel')
      
      self.idLabel = QLabel('ID')
      self.idEdit = QLineEdit()
      self.nameLabel = QLabel('Nama')
      self.nameEdit = QLineEdit()
      self.phoneLabel = QLabel('No. HP')
      self.phoneEdit = QLineEdit()
      
      grid = QGridLayout()
      grid.addWidget(self.idLabel,0,0)
      grid.addWidget(self.idEdit,0,1)
      grid.addWidget(self.nameLabel,1,0)
      grid.addWidget(self.nameEdit,1,1)
      grid.addWidget(self.phoneLabel,2,0)
      grid.addWidget(self.phoneEdit,2,1)      
      
      self.firstButton = QPushButton('|<')
      self.prevButton = QPushButton('<')
      self.nextButton = QPushButton('>')
      self.lastButton = QPushButton('>|')
      
      hbox = QHBoxLayout()
      hbox.addWidget(self.firstButton)
      hbox.addWidget(self.prevButton)
      hbox.addWidget(self.nextButton)
      hbox.addWidget(self.lastButton)
      hbox.addStretch()
      
      layout = QVBoxLayout()
      layout.addLayout(grid)
      layout.addLayout(hbox)
      layout.addStretch()
      self.setLayout(layout)
      
      self.firstButton.clicked.connect(self.firstButtonClick)
      self.prevButton.clicked.connect(self.prevButtonClick)
      self.nextButton.clicked.connect(self.nextButtonClick)
      self.lastButton.clicked.connect(self.lastButtonClick)
   
   def setData(self):
      record = self.model.record(MainForm.recordNumber)
      self.idEdit.setText(str(record.value('id')))
      self.nameEdit.setText(str(record.value('nama')))
      self.phoneEdit.setText(str(record.value('nohp')))
      	  
   def firstButtonClick(self):
      MainForm.recordNumber = 0
      self.setData()      

   def prevButtonClick(self):
      if MainForm.recordNumber == 0: return
      MainForm.recordNumber -= 1
      self.setData()

   def nextButtonClick(self):
      if MainForm.recordNumber == self.model.rowCount()-1: return
      MainForm.recordNumber += 1
      self.setData()

   def lastButtonClick(self):
      MainForm.recordNumber = self.model.rowCount()-1
      self.setData()

if __name__ == '__main__':
   a = QApplication(sys.argv)

   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('testdb')
   if not db.open():
      print('ERROR: ' + db.lastError().text())
      sys.exit(1)

   form = MainForm()
   form.show()
   
   a.exec_()
