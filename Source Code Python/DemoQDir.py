#!/usr/bin/python3

#########################################################
# Nama file: DemoQDir.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      self.directory = QDir()
      
   def setupUi(self):
      self.resize(400, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QDir')
      
      self.groupBox1 = QGroupBox('Membuat Direktori')
      self.label1 = QLabel('Nama direktori yang akan dibuat')
      self.newDirEdit = QLineEdit()                  
      self.createButton = QPushButton('Buat Direktori')
      vbox1 = QVBoxLayout()
      vbox1.addWidget(self.label1)
      vbox1.addWidget(self.newDirEdit)
      hbox1 = QHBoxLayout()
      hbox1.addStretch()
      hbox1.addWidget(self.createButton)
      vbox1.addLayout(hbox1)
      self.groupBox1.setLayout(vbox1)
      
      self.groupBox2 = QGroupBox('Mengubah Nama Direktori')
      self.label2 = QLabel('Nama direktori lama')
      self.oldDirNameEdit = QLineEdit()
      self.label3 = QLabel('Nama direktori baru')
      self.newDirNameEdit = QLineEdit()                  
      self.renameButton = QPushButton('Ubah Nama Direktori')
      vbox2 = QVBoxLayout()
      vbox2.addWidget(self.label2)
      vbox2.addWidget(self.oldDirNameEdit)
      vbox2.addWidget(self.label3)
      vbox2.addWidget(self.newDirNameEdit)
      hbox2 = QHBoxLayout()
      hbox2.addStretch()
      hbox2.addWidget(self.renameButton)
      vbox2.addLayout(hbox2)
      self.groupBox2.setLayout(vbox2)
          
      self.groupBox3 = QGroupBox('Menghapus Direktori')
      self.label4 = QLabel('Nama direktori yang akan dihapus')
      self.dirNameEdit = QLineEdit()                  
      self.removeButton = QPushButton('Hapus Direktori')
      vbox3 = QVBoxLayout()
      vbox3.addWidget(self.label4)
      vbox3.addWidget(self.dirNameEdit)
      hbox3 = QHBoxLayout()
      hbox3.addStretch()
      hbox3.addWidget(self.removeButton)
      vbox3.addLayout(hbox3)
      self.groupBox3.setLayout(vbox3)
            
      layout = QVBoxLayout()
      layout.addWidget(self.groupBox1)
      layout.addWidget(self.groupBox2)
      layout.addWidget(self.groupBox3)
      self.setLayout(layout)
      
      self.createButton.clicked.connect(self.createButtonClick)
      self.renameButton.clicked.connect(self.renameButtonClick)
      self.removeButton.clicked.connect(self.removeButtonClick)
      
   def createButtonClick(self):
      if len(self.newDirEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori harus diisi.')
         self.newDirEdit.setFocus()
         return
      if self.directory.exists(self.newDirEdit.text()):
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori sudah ada.')
         self.newDirEdit.setFocus()
         return
      # membuat direktori
      dirName = self.newDirEdit.text()
      if self.directory.mkdir(dirName):
         QMessageBox.information(self, 'Informasi',
           'Direktori "%s" telah dibuat.' % dirName)
      else:
         QMessageBox.information(self, 'Informasi',
           'Direktori gagal dibuat.')

   def renameButtonClick(self):
      if len(self.oldDirNameEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori lama harus diisi.')
         self.oldDirNameEdit.setFocus()
         return
      if len(self.newDirNameEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori baru harus diisi.')
         self.newDirNameEdit.setFocus()
         return
      if not self.directory.exists(self.oldDirNameEdit.text()):
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori tidak ditemukan.')
         self.oldDirNameEdit.setFocus()
         return
      # mengubah nama direktori
      oldDirName = self.oldDirNameEdit.text()
      newDirName = self.newDirNameEdit.text()
      if self.directory.rename(oldDirName, newDirName):
         QMessageBox.information(self, 'Informasi',
           'Direktori "%s" telah diubah menjadi "%s".' % 
           (oldDirName, newDirName))
      else:
         QMessageBox.information(self, 'Informasi',
           'Nama direktori gagal diubah.')

   def removeButtonClick(self):
      if len(self.dirNameEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori harus diisi.')
         self.dirNameEdit.setFocus()
         return
      if not self.directory.exists(self.dirNameEdit.text()):
         QMessageBox.critical(self, 'Kesalahan',
           'Nama direktori tidak ditemukan.')
         self.dirNameEdit.setFocus()
         return
      # menghapus direktori
      dirName = self.dirNameEdit.text()
      if self.directory.rmdir(dirName):
         QMessageBox.information(self, 'Informasi',
           'Direktori "%s" telah dihapus.' % dirName)
      else:
         QMessageBox.information(self, 'Informasi',
           'Direktori gagal dihapus.')

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
