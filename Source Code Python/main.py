#!/usr/bin/python3

#########################################################
# Nama file: main.py
#########################################################

import sys
from PyQt5.QtWidgets import QApplication

from MinimalForm import *

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   minform = MinimalForm()
   minform.show()
   
   a.exec_()
