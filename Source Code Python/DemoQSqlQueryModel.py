#!/usr/bin/python3

#########################################################
# Nama file: DemoQSqlQueryModel.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()      
      self.model = QSqlQueryModel()
      self.model.setQuery('SELECT nama, nohp FROM phonebook')
      self.setupUi()      
      
   def setupUi(self):
      self.resize(350, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QSqlQueryModel')
      
      self.tableView = QTableView()
      self.tableView.setModel(self.model)
      self.tableView.show()     
      
      layout = QVBoxLayout()
      layout.addWidget(self.tableView)
      self.setLayout(layout)

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
