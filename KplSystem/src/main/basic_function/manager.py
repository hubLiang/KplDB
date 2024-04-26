from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from dsa.database import OracleDB
from ui.managerUI import Ui_Manager
from dsa.sql import FilePath

class Win_Manager(Ui_Manager, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Manager, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file2))  # 图标设置
        #事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.btn_display.clicked.connect(self.display)

#录入
    def add(self):
        sql_add = 'insert into Manager(Mid,Mname,Mage,Msex) values(:Mid,:Mname,:Mage,:Msex)'
        try:
            input_data=self.get_manager()
            if(input_data[0]==''or input_data[1]==''):
                QMessageBox.warning(self, '提示', '经理id或姓名未输入', QMessageBox.Yes)
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
        sql_Mname = 'update Manager set Mname=:Mname where Mid=:Mid'
        sql_Mage = 'update Manager set Mage=:Mage where Mid=:Mid'
        sql_Msex = 'update Manager set Msex=:Msex where Mid=:Mid'
        field=['姓名','年龄','性别']#修改字段列表
        update_field=self.comboBox_Managerupdate.currentText()#获取需要修改的字段
        inpute_data = self.get_manager()#输入数据
        manager_dict = [{'Mname': inpute_data[1],'Mid': inpute_data[0]},{'Mage': inpute_data[2],'Mid': inpute_data[0]},{'Msex': inpute_data[3],'Mid': inpute_data[0]}]#修改数据封装
        try:
            inpute_data= self.get_manager()
            if (inpute_data[0]==''):
                QMessageBox.warning(self, '提示', '请输入英雄id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Mname,manager_dict [0])
                elif(update_field==field[1]):
                    db.execute(sql_Mage, manager_dict[1])
                elif (update_field == field[2]):
                    db.execute(sql_Msex,manager_dict[2])
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
        sql_id = "delete from Manager where Mid=:Mid"
        input = self.le_input.text()
        dic_id = {'Mid': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '请输入需删除经理的id', QMessageBox.Yes)
            elif (input):
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '数据库中没有该经理信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '经理信息已删除', QMessageBox.Yes)

        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#查找
    def search(self):
        sql = "select*from Manager where Mid=:Mid"
        input = self.le_input.text()
        dic_id = {'Mid': input}
        headers = ['id', '姓名', '年龄','性别']
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
        sql_all = 'select Manager.* from Manager'
        sort_byMid = 'select Manager.* from Manager order by Mid'
        sort_byMname= 'select Manager.* from Manager order by Mname'
        #sort_byMsex = 'select Manager.* from Manager order by Msex'
        sort_commond=self.comboBox_sort.currentText()#获取排序命令
        if(sort_commond==''):
            sql=sql_all
        elif(sort_commond=='id'):
            sql=sort_byMid
        elif(sort_commond=='年龄'):
            sql=sort_byMname
        try:
            db = OracleDB()
            db.connect()
            Manager_list = db.query(sql)
            db.close()
            self.model = QStandardItemModel()
            headers = ['id', '姓名', '年龄','性别']
            self.model.setHorizontalHeaderLabels(headers)  # 设置表头
            # 设置表头字体字号
            for i, header in enumerate(headers):
                item = QStandardItem(header)
                item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
                self.model.setHorizontalHeaderItem(i, item)
            # 将数据加载进model中
            for row, record in enumerate(Manager_list):
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

    def get_manager(self):
        Mid=self.le_Mid.text()
        Mname=self.le_Mname.text()
        Mage=self.le_Mage.text()
        Msex=self.le_Msex.text()
        input_data=(Mid,Mname,Mage,Msex)
        return input_data

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_Manager()
    window.show()
    sys.exit(app.exec_())


