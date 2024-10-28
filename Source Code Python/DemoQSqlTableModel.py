#!/usr/bin/python3

#########################################################
# Nama file: DemoQSqlTableModel.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()      
      self.model = QSqlTableModel()
      self.model.setTable('phonebook')
      self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
      self.model.select()
      self.setupUi()      
      
   def setupUi(self):
      self.resize(350, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QSqlTableModel')
      
      self.tableView = QTableView()
      self.tableView.setModel(self.model)
      
      self.addButton = QPushButton('Tambah')
      self.deleteButton = QPushButton('Hapus')    
      
      hbox = QHBoxLayout()
      hbox.addWidget(self.addButton)
      hbox.addWidget(self.deleteButton)
      hbox.addStretch()
      
      layout = QVBoxLayout()
      layout.addWidget(self.tableView)
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.addButton.clicked.connect(self.addButtonClick)
      self.deleteButton.clicked.connect(self.deleteButtonClick)
      	  
   def addButtonClick(self):
      self.model.insertRows(self.model.rowCount(), 1)

   def deleteButtonClick(self):
      indexList = self.tableView.selectionModel().selection().indexes()
      for i in range(len(indexList)):
         index = indexList[i]
         row = index.row()
         self.model.removeRows(row, 1)
      self.model.select()

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
