#!/usr/bin/python3

#########################################################
# Nama file: DemoQFileCopy.py
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
      self.setWindowTitle('Demo QFile.copy()')
      
      self.label1 = QLabel('Nama file sumber')
      self.sourceFileEdit = QLineEdit()
      self.label2 = QLabel('Nama file tujuan')
      self.destFileEdit = QLineEdit()            
      self.copyButton = QPushButton('Salin File')
      hbox = QHBoxLayout()
      hbox.addStretch()
      hbox.addWidget(self.copyButton)
            
      layout = QVBoxLayout()
      layout.addWidget(self.label1)
      layout.addWidget(self.sourceFileEdit)
      layout.addWidget(self.label2)
      layout.addWidget(self.destFileEdit)
      layout.addStretch()
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.copyButton.clicked.connect(self.copyButtonClick)
      
   def copyButtonClick(self):
      if len(self.sourceFileEdit.text().strip()) == 0 or \
         len(self.destFileEdit.text().strip()) == 0:
         QMessageBox.critical(self, 'Kesalahan',
           'Nama file sumber dan tujuan harus diisi.')
         return
      if not QFile.exists(self.sourceFileEdit.text()):
         return
      # menyalin file menggunakan QFile
      sourceFile = self.sourceFileEdit.text()
      destFile = self.destFileEdit.text()      
      if QFile.copy(sourceFile, destFile):
         QMessageBox.information(self, 'Informasi',
           'File berhasil disalin.')
      else:
         QMessageBox.information(self, 'Informasi',
           'File gagal disalin.')

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
