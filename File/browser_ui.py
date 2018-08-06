# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 549)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pb_browser = QtWidgets.QPushButton(Form)
        self.pb_browser.setObjectName("pb_browser")
        self.horizontalLayout.addWidget(self.pb_browser)
        self.pb_open = QtWidgets.QPushButton(Form)
        self.pb_open.setObjectName("pb_open")
        self.horizontalLayout.addWidget(self.pb_open)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lb_show = QtWidgets.QLabel(Form)
        self.lb_show.setText("")
        self.lb_show.setPixmap(QtGui.QPixmap("1.jpg"))
        self.lb_show.setScaledContents(True)
        self.lb_show.setWordWrap(False)
        self.lb_show.setObjectName("lb_show")
        self.verticalLayout.addWidget(self.lb_show)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "File browser"))
        self.pb_browser.setWhatsThis(_translate("Form", "<html><head/><body><p>浏览文件</p></body></html>"))
        self.pb_browser.setText(_translate("Form", "浏览"))
        self.pb_open.setText(_translate("Form", "打开"))

