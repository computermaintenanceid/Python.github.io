#!/usr/bin/python3

#########################################################
# Nama file: SQLExecutor.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class MainForm(QWidget):  
   def __init__(self):
      super().__init__()      
      self.setupUi()
      
   def setupUi(self):
      self.resize(450, 400)
      self.move(300, 300)
      self.setWindowTitle('SQL Executor')
      
      self.label1 = QLabel('Tulis perintah SQL pada kotak di bawah ini')
      self.sqlTextEdit = QTextEdit()
      
      vbox1 = QVBoxLayout()
      vbox1.addWidget(self.label1)
      vbox1.addWidget(self.sqlTextEdit)
      
      self.emptyLabel = QLabel('')
      self.executeButton = QPushButton('&Eksekusi')
      
      vbox2 = QVBoxLayout()
      vbox2.addWidget(self.emptyLabel)
      vbox2.addWidget(self.executeButton)
      vbox2.addStretch()
      
      hbox = QHBoxLayout()
      hbox.addLayout(vbox1)
      hbox.addLayout(vbox2)
      
      self.label2 = QLabel('Hasil query')
      self.tableView = QTableView()
      self.label3 = QLabel('Log')
      self.logList = QListWidget()
            
      layout = QVBoxLayout()
      layout.addLayout(hbox)
      layout.addWidget(self.label2)
      layout.addWidget(self.tableView)
      layout.addWidget(self.label3)
      layout.addWidget(self.logList)
      self.setLayout(layout)
      
      self.executeButton.clicked.connect(self.executeButtonClick)
   
   def executeButtonClick(self):
      specialCommands = ['SHOW','DESC','DESCRIBE','SELECT']
      sql = self.sqlTextEdit.document().toPlainText()
      
      # memeriksa apakah sql diawali oleh
      # salah satu anggota dari specialCommands atau tidak
      idx = sql.index(' ')
      firstCommand = sql[:idx];
      isSpecialCommand = firstCommand.upper() in specialCommands

      if isSpecialCommand:              # jika ya
         model = QSqlQueryModel()
         model.setQuery(sql)            
         self.tableView.setModel(model)
         self.tableView.show()
      else:                             # jika tidak
         query = QSqlQuery()
         query.exec_(sql)

      self.logList.addItem(sql)

if __name__ == '__main__':
   a = QApplication(sys.argv)

   db = QSqlDatabase.addDatabase('QMYSQL')
   db.setHostName('localhost')
   db.setDatabaseName('testdb')
   db.setUserName('root')
   db.setPassword('root')

   if not db.open():
      print('ERROR: ' + db.lastError().text())
      sys.exit(1)

   form = MainForm()
   form.show()
   
   a.exec_()
