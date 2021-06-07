import sympy as sym
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import sys
import math

dir = os.getcwd() + '\\'
_translate = QtCore.QCoreApplication.translate
ui = uic.loadUiType(dir+'main.ui')[0]

class Form(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setFixedSize(308,144)
        self.setupUi(self)
        self.doubleSpinBox.valueChanged.connect(self.cal)
        self.doubleSpinBox_2.valueChanged.connect(self.cal)
        self.pushButton.clicked.connect(self.close)

        self.show()

    def cal(self):
        A = self.doubleSpinBox.value()
        B = self.doubleSpinBox_2.value()
        x = sym.Symbol('x')
        roottwopi = (2*math.pi)**(1/2)
        xsquare = (x**2)
        F = (1/(roottwopi*sym.exp(xsquare/2)))
        a = sym.integrate(F, (x, A, B))
        result = sym.N(a)
        self.lineEdit.setText(str(result))
        return

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())