from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.loginUI import Ui_Winlogin
from dsa.sql import FilePath
from controller import Win_controller
from dsa.database import OracleDB
class Win_login(Ui_Winlogin,QtWidgets.QMainWindow):
    def __init__(self):
        super(Win_login,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file1))#图标设置
        #self.resize(1200, 1200)
        #登录绑定事件
        self.pb_login.clicked.connect(self.login_try)
        #退出绑定事件
        self.pb_regist.clicked.connect(self.regist)

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

    def regist(self):
        usn_input = self.le_username.text()  # 获取用户输入名
        psd_input = self.le_password.text()  # 获取输入密码
        sql="insert into user_table('Uname','Upassword') values(:Uname,:Upassword)"
        data=(usn_input,psd_input)
        # print(data)
        db = OracleDB()
        db.connect()
        db.executemany(sql,[data])
        QMessageBox.warning(self, '提示', '用户已注册！', QMessageBox.Yes)




if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window = Win_login()
    window.show()
    sys.exit(app.exec_())