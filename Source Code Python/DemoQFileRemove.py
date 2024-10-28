#!/usr/bin/python3

#########################################################
# Nama file: DemoQFileRemove.py
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
      self.resize(400, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QFile.remove()')
      
      self.label1 = QLabel('Nama file yang akan dihapus')
      self.fileEdit = QLineEdit()                  
      self.removeButton = QPushButton('Hapus File')
      hbox = QHBoxLayout()
      hbox.addStretch()
      hbox.addWidget(self.removeButton)
            
      layout = QVBoxLayout()
      layout.addWidget(self.label1)
      layout.addWidget(self.fileEdit)
      layout.addStretch()
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.removeButton.clicked.connect(self.removeButtonClick)
      
   def removeButtonClick(self):
      if len(self.fileEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama file harus diisi.')
         return
      if not QFile.exists(self.fileEdit.text()):
         return
      # menghapus file menggunakan QFile
      fileName = self.fileEdit.text()
      if QFile.remove(fileName):
         QMessageBox.information(self, 'Informasi',
           'File "%s" telah dihapus.' % fileName)
      else:
         QMessageBox.information(self, 'Informasi',
           'File gagal dihapus.')

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
