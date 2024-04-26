from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.controllerUI import Ui_MainWindow
from ui.loginUI import Ui_Winlogin
# from login import Win_login
from basic_function.player import Win_Player
from basic_function.coach import Win_Coach
from basic_function.hero import Win_hero
from basic_function.team import Win_Team
from basic_function.manager import Win_Manager
from basic_function.league import Win_league
from advanced_function.SQL import Win_SQL
from advanced_function.DataCalculate import Win_DataCalculate
from dsa.database import OracleDB
from dsa.sql import FilePath
#登录类
class Win_login(Ui_Winlogin,QtWidgets.QMainWindow):
    def __init__(self):
        super(Win_login,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file3))#图标设置
        #self.resize(1200, 1200)
        #登录绑定事件
        self.pb_login.clicked.connect(self.login_try)
        #退出绑定事件
        self.pb_exit.clicked.connect(self.close)

    def login_try(self):
        '''
        登录事件
        :return:
        '''
        db = OracleDB()
        db.connect()
        user_table=db.query("select*from users")
        db.close()
        usn_input=self.le_username.text()#获取用户输入名
        psd_input=self.le_password.text()#获取输入密码
        boolean=self.validate_login(usn_input,psd_input,user_table)
        #判断用户名和密码是否正确
        if boolean==True:
            self.login()
        else:
            self.logerror()
    #验证用户名、密码是否正确
    def validate_login(self,username, password, user_table):
        for user in user_table:
            if user[0] == username:
                if user[1] == password:
                    return True
                else:
                    return False
        return False

    def login(self):
        '''
        登录成功
        :param self:
        :return:
        '''
        self.ui1=Win_controller()
        self.ui1.show()
        self.close()

    def logerror(self):
        '''
        登录失败
        :param self:
        :return:
        '''
        QMessageBox.warning(self,'错误','用户名或密码错误！',QMessageBox.Yes)

#控制类
class Win_controller(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('../photos/user.svg'))#图标设置
        #事件绑定
        self.btn_return.clicked.connect(self.getback)#返回事件
        self.btn_exit.clicked.connect(self.close)#退出事件
        self.btn_player.clicked.connect(self.toplayer)#选手管理事件
        self.btn_coach.clicked.connect(self.tocoach)#教练管理事件
        self.btn_manager.clicked.connect(self.tomanager)  # 经理管理事件
        self.btn_team.clicked.connect(self.toteam)  # 战队管理事件
        self.btn_hero.clicked.connect(self.tohero)  # 英雄管理事件
        self.btn_league.clicked.connect(self.toleague)#联赛管理
        self.btn_sql.clicked.connect(self.tosql)
        self.btn_statistics.clicked.connect(self.tostatistics)


    def getback(self):
        self.ui=Win_login()
        self.ui.show()
        self.close()
    def toplayer(self):
        self.ui=Win_Player()
        self.ui.show()
    def tocoach(self):
        self.ui = Win_Coach()
        self.ui.show()
    def tomanager(self):
        self.ui = Win_Manager()
        self.ui.show()
    def toteam(self):
        self.ui = Win_Team()
        self.ui.show()
    def tohero(self):
        self.ui = Win_hero()
        self.ui.show()
    def toleague(self):
        self.ui = Win_league()
        self.ui.show()
    def tosql(self):
        self.ui=Win_SQL()
        self.ui.show()
    def tostatistics(self):
        self.ui = Win_DataCalculate()
        self.ui.show()

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window = Win_controller()
    window.show()
    sys.exit(app.exec_())
