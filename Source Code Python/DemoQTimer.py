#!/usr/bin/python3

#########################################################
# Nama file: DemoQTimer.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      
      self.timer = QTimer()
      self.timer.setInterval(1000)	# 1 detik
      
      self.setupUi()            
      self.timer.start()
      
   def setupUi(self):
      self.resize(250, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QTimer')
      
      font = QFont()
      font.setFamily('SansSerif')
      font.setPixelSize(30)
      
      self.label = QLabel()
      self.label.setFont(font)
                  
      layout = QHBoxLayout()
      layout.addWidget(self.label)
      self.setLayout(layout)
      
      self.timer.timeout.connect(self.timerTimer)
      
   def timerTimer(self):
      currentTime = QTime.currentTime()
      self.label.setText(currentTime.toString())

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
