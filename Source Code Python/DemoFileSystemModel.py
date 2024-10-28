#!/usr/bin/python3

#########################################################
# Nama file: DemoQFileSystemModel.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      
      self.dirModel = QFileSystemModel()
      self.dirModel.setFilter(QDir.NoDotAndDotDot |
                              QDir.AllDirs)
      self.dirModel.setRootPath('/')
      
      self.fileModel = QFileSystemModel()      
      self.fileModel.setFilter(QDir.NoDotAndDotDot |
                               QDir.AllDirs |
                               QDir.Files)
      
      self.setupUi()
      
   def setupUi(self):
      self.resize(600, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QFileSystemModel')
      
      self.treeView = QTreeView()        
      self.treeView.setModel(self.dirModel)
      for i in range(1,4):
         self.treeView.hideColumn(i)
      self.treeView.setColumnWidth(0, 120)
      self.treeView.setHeaderHidden(True)
      
      self.listView = QListView()
      self.listView.setModel(self.fileModel)      
      
      self.splitter = QSplitter(self)
      self.splitter.setOrientation(Qt.Horizontal)
      self.splitter.addWidget(self.treeView)
      self.splitter.addWidget(self.listView)    
                  
      layout = QHBoxLayout()
      layout.addWidget(self.splitter)
      self.setLayout(layout)
      
      self.treeView.clicked.connect(self.treeViewItemClick)
      
   def treeViewItemClick(self):
      index = self.treeView.currentIndex()
            
      currentPath = \
        self.dirModel.fileInfo(index).absoluteFilePath()
      self.listView.setRootIndex(
        self.fileModel.setRootPath(currentPath)
      )

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
