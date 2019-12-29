# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookStoreGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import math

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.b1 = QtWidgets.QLineEdit(Form)
        self.b1.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.b1.setObjectName("b1")
        self.p1 = QtWidgets.QLineEdit(Form)
        self.p1.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.p1.setObjectName("p1")
        self.q1 = QtWidgets.QLineEdit(Form)
        self.q1.setValidator(QtGui.QIntValidator())
        self.q1.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.q1.setObjectName("q1")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.t1.setObjectName("t1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 39, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openClick)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 150, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openClick2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title:"))
        self.label_2.setText(_translate("Form", "Price:"))
        self.label_3.setText(_translate("Form", "Quantity:"))
        self.label_4.setText(_translate("Form", "Total:"))
        self.pushButton.setText(_translate("Form", "Find Price"))
        self.pushButton_2.setText(_translate("Form", "Find Total"))

    def booklist(self, action):
        txt = (action.text())
        title = (self.b1.text())
        print(txt, title)
        if txt == 'pushButton':
            self.p1.setText(int(100))
           
    def openClick(self):
        MyStore = sqlite3.connect('BookStore.db')
        cur = MyStore.cursor()
        book = self.b1.text()
        sql = "SELECT * from books WHERE title = '"+book+"';"
        cur.execute(sql)
        record = str(cur.fetchone()).strip('()')
        if record:
            global p2
            price = "SELECT price from books WHERE title = '"+book+"';"
            cur.execute(price)
            p = str(cur.fetchone())
            pri1 = p.strip('()')
            p2 = int(pri1.replace(',', ''))
            self.p1.setText(str(p2))
        if not record:
            print("Book is not fond.")
            self.p1.setText(str("Book is not fond."))
        
    def openClick2(self):
        qty = int(self.q1.text())
        tp = p2 * qty
        self.t1.setText(str(tp))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
