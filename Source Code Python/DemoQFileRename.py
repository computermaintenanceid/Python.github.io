#!/usr/bin/python3

#########################################################
# Nama file: DemoQFileRename.py
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
      self.resize(400, 150)
      self.move(300, 300)
      self.setWindowTitle('Demo QFile.rename()')
      
      self.label1 = QLabel('Nama file lama')
      self.oldFileEdit = QLineEdit()
      self.label2 = QLabel('Nama file baru')
      self.newFileEdit = QLineEdit()            
      self.renameButton = QPushButton('Ubah Nama File')
      hbox = QHBoxLayout()
      hbox.addStretch()
      hbox.addWidget(self.renameButton)
            
      layout = QVBoxLayout()
      layout.addWidget(self.label1)
      layout.addWidget(self.oldFileEdit)
      layout.addWidget(self.label2)
      layout.addWidget(self.newFileEdit)
      layout.addStretch()
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.renameButton.clicked.connect(self.renameButtonClick)
      
   def renameButtonClick(self):
      if len(self.oldFileEdit.text().strip()) == 0 or \
         len(self.newFileEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama file lama dan baru harus diisi.')
         return
      if not QFile.exists(self.oldFileEdit.text()):
         return
      # mengubah nama file menggunakan QFile
      oldFile = self.oldFileEdit.text()
      newFile = self.newFileEdit.text()      
      if QFile.rename(oldFile, newFile):
         QMessageBox.information(self, 'Informasi',
           'File "%s" telah diubah menjadi "%s".' %
           (oldFile, newFile))
      else:
         QMessageBox.information(self, 'Informasi',
           'Perubahan nama file gagal dilakukan.')

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
