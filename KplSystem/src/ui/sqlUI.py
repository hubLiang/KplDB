# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SQL.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(754, 426)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 291, 221))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(330, 50, 401, 361))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(Frame)
        self.widget.setGeometry(QtCore.QRect(20, 10, 351, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.widget1 = QtWidgets.QWidget(Frame)
        self.widget1.setGeometry(QtCore.QRect(60, 290, 201, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_execute = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.btn_execute.setFont(font)
        self.btn_execute.setObjectName("btn_execute")
        self.horizontalLayout_3.addWidget(self.btn_execute)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_clear = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_3.addWidget(self.btn_clear)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "sql"))
        self.label_2.setText(_translate("Frame", "输入"))
        self.radioButton.setText(_translate("Frame", "查询"))
        self.radioButton_2.setText(_translate("Frame", "其它"))
        self.label_3.setText(_translate("Frame", "输出"))
        self.btn_execute.setText(_translate("Frame", "执行"))
        self.btn_clear.setText(_translate("Frame", "clear"))
