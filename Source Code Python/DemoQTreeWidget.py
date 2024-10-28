#!/usr/bin/python3

#########################################################
# Nama file: DemoQTreeWidget.py
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
      self.resize(400, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QTreeWidget')
      
      self.tree = QTreeWidget()      
      self.tree.setColumnCount(1)
      self.tree.setHeaderHidden(True)
      
      parent1 = self.addTopLevel('Induk 1')
      child1 = self.addChild(parent1, 'Anak 1-1')
      self.addChild(child1, 'Cucu 1-1-1')
      self.addChild(child1, 'Cucu 1-1-2')
      self.addChild(parent1, 'Anak 1-2')
      self.addChild(parent1, 'Anak 1-3')
      
      parent2 = self.addTopLevel('Induk 2')
      self.addChild(parent2, 'Anak 2-1')
      self.addChild(parent2, 'Anak 2-2')
      
      parent3 = self.addTopLevel('Induk 3')
      self.addChild(parent3, 'Anak 3-1')
      self.addChild(parent3, 'Anak 3-2')
      self.addChild(parent3, 'Anak 3-3')
      self.addChild(parent3, 'Anak 3-4')
      
      self.lineEdit = QLineEdit()

      layout = QVBoxLayout()
      layout.addWidget(self.tree)
      layout.addWidget(self.lineEdit)
      self.setLayout(layout)
      
      self.tree.itemClicked.connect(self.treeItemClick)      
      
   def treeItemClick(self):
      item = self.tree.currentItem()
      self.lineEdit.setText(item.text(0))

   def addTopLevel(self, itemText):
      item = QTreeWidgetItem()
      item.setText(0, itemText)
      self.tree.addTopLevelItem(item)
      return item

   def addChild(self, parent, itemText):
      item = QTreeWidgetItem(parent)
      item.setText(0, itemText)
      parent.addChild(item)
      return item

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
