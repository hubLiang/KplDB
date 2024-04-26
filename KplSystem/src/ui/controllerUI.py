# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kpl_sys.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 559)
        MainWindow.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 60, 311, 411))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 141, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_player = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_player.setFont(font)
        self.btn_player.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_player.setObjectName("btn_player")
        self.verticalLayout.addWidget(self.btn_player)
        self.btn_coach = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_coach.setFont(font)
        self.btn_coach.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_coach.setObjectName("btn_coach")
        self.verticalLayout.addWidget(self.btn_coach)
        self.btn_manager = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_manager.setFont(font)
        self.btn_manager.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_manager.setObjectName("btn_manager")
        self.verticalLayout.addWidget(self.btn_manager)
        self.btn_team = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_team.setFont(font)
        self.btn_team.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_team.setObjectName("btn_team")
        self.verticalLayout.addWidget(self.btn_team)
        self.btn_hero = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_hero.setFont(font)
        self.btn_hero.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_hero.setObjectName("btn_hero")
        self.verticalLayout.addWidget(self.btn_hero)
        self.btn_league = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_league.setFont(font)
        self.btn_league.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_league.setObjectName("btn_league")
        self.verticalLayout.addWidget(self.btn_league)
        self.groupBox_advanced = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_advanced.setGeometry(QtCore.QRect(470, 60, 211, 411))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.groupBox_advanced.setFont(font)
        self.groupBox_advanced.setObjectName("groupBox_advanced")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_advanced)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 121, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_statistics = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_statistics.setFont(font)
        self.btn_statistics.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_statistics.setObjectName("btn_statistics")
        self.verticalLayout_2.addWidget(self.btn_statistics)
        self.btn_sql = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_sql.setFont(font)
        self.btn_sql.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_sql.setObjectName("btn_sql")
        self.verticalLayout_2.addWidget(self.btn_sql)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(720, 200, 77, 114))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_return = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_return.setObjectName("btn_return")
        self.verticalLayout_3.addWidget(self.btn_return)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_3.addWidget(self.btn_exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar_3)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_2)
        self.actionxusnhouguanl = QtWidgets.QAction(MainWindow)
        self.actionxusnhouguanl.setObjectName("actionxusnhouguanl")
        self.actionynnc = QtWidgets.QAction(MainWindow)
        self.actionynnc.setObjectName("actionynnc")
        self.menu_2.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统界面"))
        self.groupBox.setTitle(_translate("MainWindow", "基本功能"))
        self.btn_player.setText(_translate("MainWindow", "选手管理"))
        self.btn_coach.setText(_translate("MainWindow", "教练管理"))
        self.btn_manager.setText(_translate("MainWindow", "经理管理"))
        self.btn_team.setText(_translate("MainWindow", "战队管理"))
        self.btn_hero.setText(_translate("MainWindow", "英雄管理"))
        self.btn_league.setText(_translate("MainWindow", "联赛管理"))
        self.groupBox_advanced.setTitle(_translate("MainWindow", "高级功能"))
        self.btn_statistics.setText(_translate("MainWindow", "数据统计"))
        self.btn_sql.setText(_translate("MainWindow", "SQL"))
        self.label.setText(_translate("MainWindow", "欢迎访问KPL数据库管理系统！"))
        self.btn_return.setText(_translate("MainWindow", "返回"))
        self.btn_exit.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionxusnhouguanl.setText(_translate("MainWindow", "xusnhouguanl "))
        self.actionynnc.setText(_translate("MainWindow", "ynnc"))
