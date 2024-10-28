#!/usr/bin/python3

#########################################################
# Nama file: DemoQDirModel.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      
      self.model = QDirModel()
      self.model.setReadOnly(False)
      self.model.setSorting(QDir.DirsFirst | 
                            QDir.IgnoreCase |
                            QDir.Name)            
      
      self.setupUi()
      
   def setupUi(self):
      self.resize(600, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QDirModel')
      
      self.treeView = QTreeView()
      self.treeView.setModel(self.model)
      
      # contoh mengaktifkan direktori tertentu
      index = self.model.index('/home/budi')
      self.treeView.expand(index)
      self.treeView.scrollTo(index)
      self.treeView.setCurrentIndex(index)
      self.treeView.resizeColumnToContents(0)
      
      self.createButton = QPushButton('Buat Direktori')
      self.deleteButton = QPushButton('Hapus')      
      hbox = QHBoxLayout()
      hbox.addStretch()
      hbox.addWidget(self.createButton)
      hbox.addWidget(self.deleteButton)
                  
      layout = QVBoxLayout()
      layout.addWidget(self.treeView)
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.createButton.clicked.connect(self.createButtonClick)
      self.deleteButton.clicked.connect(self.deleteButtonClick)
      
   def createButtonClick(self):
      index = self.treeView.currentIndex()
      if not index.isValid(): return
      
      dialogResult = QInputDialog.getText(self, "Membuat Direktori",
        "Masukkan nama direktori yang akan dibuat:")
      newDirName = dialogResult[0]
      
      if len(newDirName) == 0: return
      
      self.model.mkdir(index, newDirName)

   def deleteButtonClick(self):
      index = self.treeView.currentIndex()
      if not index.isValid(): return
      
      if (self.model.fileInfo(index).isDir()):
         # menghapus direktori
         self.model.rmdir(index)
      else:
         # menghapus file
         self.model.remove(index)

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
