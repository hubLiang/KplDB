from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from ui.heroUI import Ui_Hero
from dsa.database import OracleDB
from dsa.sql import FilePath

class Win_hero(Ui_Hero, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Hero, self).__init__()
        self.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon('../photos/information.png'))  # 图标设置
        self.setWindowIcon(QtGui.QIcon(FilePath.file2)) # 图标设置

        #事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.btn_display.clicked.connect(self.display)

#录入
    def add(self):
        sql_add = 'insert into Hero(Hid,Hname,Hrole) values(:Hid,:Hname,:Hrole)'
        try:
            input_data=self.get_hero()
            if(input_data[0]==''or input_data[1]==''):
                QMessageBox.warning(self, '提示', '英雄id或英雄名未输入', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                db.executemany(sql_add,[input_data])
                db.close()
                QMessageBox.warning(self, '提示', '信息已录入', QMessageBox.Yes)
        except Exception as e:
            # 发生错误时回滚事务
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#修改
    def update(self):
        #sql语句
        sql_Hname = 'update Hero set Hname=:Hname where Hid=:Hid'
        sql_Hrole = 'update Hero set Hrole=:Hrole where Hid=:Hid'
        field=['英雄名','角色']#修改字段列表
        update_field=self.comboBox_Heroupdate.currentText()#获取需要修改的字段
        inpute_data = self.get_hero()#输入数据
        hero_dict = [{'Hname': inpute_data[1],'Hid': inpute_data[0]},{'Hrole': inpute_data[2],'Hid': inpute_data[0]}]#修改数据封装
        try:
            inpute_data= self.get_hero()
            if (inpute_data[0]==''):
                QMessageBox.warning(self, '提示', '请输入英雄id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Hname,hero_dict[0])
                elif(update_field==field[1]):
                    db.execute(sql_Hrole, hero_dict[1])
                else:
                    QMessageBox.warning(self, '提示', '请选择要修改的字段！', QMessageBox.Yes)
                    return
                db.close()
                QMessageBox.warning(self, '提示', '信息已修改', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#删除
    def delete(self):
        sql_id = "delete from Hero where Hid=:Hid"
        input = self.le_input.text()
        dic_id = {'Hid': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '请输入需删除英雄的id', QMessageBox.Yes)
            elif (input):
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '数据库中未找到该英雄信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '英雄基本信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#查找
    def search(self):
        sql = "select*from Hero where Hid=:Hid"
        input = self.le_input.text()
        dic_id = {'Hid': input}
        headers = ['id', '英雄名', '角色']
        result = ''
        try:
            self.textBrowser.clear()  # 显示前清空
            if (input==''):
                QMessageBox.warning(self, '提示', '输入为空', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                data = db.query(sql, dic_id)  # 查询结果
                data1=[str(x) for x in data[0]]#转为1维
                if (len(data1) == 0):
                    QMessageBox.warning(self, '查询失败', '数据库中未查询到', QMessageBox.Yes)
                else:
                    for i in range(len(headers)):
                        result += str(headers[i]) + ': ' + str(data1[i]) + '\n'
                    self.textBrowser.setText(result)#UI显示
                    db.close()
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#显示
    def display(self):
        sql_all = 'select Hero.* from Hero'
        sort_byHid = 'select Hero.* from Hero order by Hero.Hid'
        sort_byHname= 'select Hero.* from Hero order by Hero.Hname'
        sort_byHrole = 'select Hero.* from Hero order by Hero.Hrole'
        sort_commond=self.comboBox_sort.currentText()#获取排序命令
        if(sort_commond==''):
            sql=sql_all
        elif(sort_commond=='id'):
            sql=sort_byHid
        elif(sort_commond=='英雄名'):
            sql=sort_byHname
        elif (sort_commond == '角色'):
            sql = sort_byHrole
        try:
            db = OracleDB()
            db.connect()
            hero_list = db.query(sql)
            db.close()
            self.model = QStandardItemModel()
            # self.model.setColumnCount(4)  # 设置行数
            headers = ['id', '英雄名', '角色']
            self.model.setHorizontalHeaderLabels(headers)  # 设置表头
            # 设置表头字体字号
            for i, header in enumerate(headers):
                item = QStandardItem(header)
                item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
                self.model.setHorizontalHeaderItem(i, item)
            # 将数据加载进model中
            for row, record in enumerate(hero_list):
                for column, value in enumerate(record):
                    item = QStandardItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置数据居中显示
                    self.model.setItem(row, column, item)
            self.tableView.setModel(self.model)
            # 设置列宽
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
            column_width=70 #置列宽为70
            for i in range(self.tableView.model().columnCount()):
                self.tableView.setColumnWidth(i, column_width)
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动调整列宽
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def get_hero(self):
        Hid=self.le_Hid.text()
        Hname=self.le_Hname.text()
        Hrole=self.comboBox_Hrole.currentText()
        input_data=(Hid,Hname,Hrole)
        return input_data

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_hero()
    window.show()
    sys.exit(app.exec_())
