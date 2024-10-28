#!/usr/bin/python3

#########################################################
# Nama file: DemoQThread1.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# kelas thread pertama
class OddThread(QThread):
   def __init__(self, listWidget):
      super().__init__()
      self.listWidget = listWidget
   # overrride metode run()
   def run(self):
      for i in range(1, 10000):
         if i % 2 == 1:
            self.listWidget.addItem(str(i))

# kelas thread kedua
class EvenThread(QThread):
   def __init__(self, listWidget):
      super().__init__()
      self.listWidget = listWidget
   # overrride metode run()
   def run(self):
      for i in range(1, 10000):
         if i % 2 == 0:
            self.listWidget.addItem(str(i))

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
      # membuat objek dari kelas OddThread
      self.thread1 = OddThread(self.oddListWidget)
      
      # membuat objek dari kelas EvenThread
      self.thread2 = EvenThread(self.evenListWidget)
      
   def setupUi(self):
      self.resize(300, 300)
      self.move(300, 300)
      self.setWindowTitle('Demo QThread')
      
      self.oddListWidget = QListWidget()        
      self.startButton1 = QPushButton('Mulai')
      vbox1 = QVBoxLayout()
      vbox1.addWidget(self.oddListWidget)
      hbox1 = QHBoxLayout()
      hbox1.addWidget(self.startButton1)
      hbox1.addStretch()
      vbox1.addLayout(hbox1)
      
      self.evenListWidget = QListWidget()        
      self.startButton2 = QPushButton('Mulai')
      vbox2 = QVBoxLayout()
      vbox2.addWidget(self.evenListWidget)
      hbox2 = QHBoxLayout()
      hbox2.addWidget(self.startButton2)
      hbox2.addStretch()
      vbox2.addLayout(hbox2)
                  
      layout = QHBoxLayout()
      layout.addLayout(vbox1)
      layout.addLayout(vbox2)
      self.setLayout(layout)
      
      self.startButton1.clicked.connect(self.startButton1Click)
      self.startButton2.clicked.connect(self.startButton2Click)      
      
   def startButton1Click(self):
      QApplication.processEvents()
      self.thread1.start()

   def startButton2Click(self):
      QApplication.processEvents()
      self.thread2.start()

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
