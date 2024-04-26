from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from ui.leagueUI import Ui_League
from dsa.database import OracleDB
from dsa.sql import FilePath

class Win_league(Ui_League, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_League, self).__init__()
        self.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon('../photos/information.png'))  # 图标设置
        self.setWindowIcon(QtGui.QIcon(FilePath.file2)) # 图标设置

#事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.btn_display.clicked.connect(self.display)
        self.btn_insert.clicked.connect(self.attend)#参赛事件
        self.btn_update2.clicked.connect(self.update2)
        self.btn_delete2.clicked.connect(self.delete2)

    def get_league(self):
        Lid=self.le_Lid.text()
        Lname=self.le_Lname.text()
        Llevel=self.le_Llevel.text()
        Lrule=self.le_Lrule.text()
        input_data=(Lid,Lname,Llevel,Lrule)
        return input_data
#录入
    def add(self):
        sql_add = 'insert into League(Lid,Lname,Llevel,Lrule) values(:Lid,:Lname,:Llevel,:Lrule)'
        try:
            input_data=self.get_league()
            if(input_data[0]==''or input_data[1]==''):
                QMessageBox.warning(self, '提示', '联赛id或联赛名称未输入', QMessageBox.Yes)
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
        sql_Lname = 'update League set Lname=:Lname where Lid=:Lid'
        sql_Llevel = 'update League set Llevel=:Llevel where Lid=:Lid'
        sql_Lrule = 'update League set Lrule=:Lrule where Lid=:Lid'
        field=['联赛名称','联赛等级','联赛规则']#修改字段列表
        update_field=self.comboBox_Leagueupdate.currentText()#获取需要修改的字段
        inpute_data = self.get_league()#输入数据
        league_dict = [{'Lname': inpute_data[1],'Lid': inpute_data[0]},{'Llevel': inpute_data[2],'Lid': inpute_data[0]},
                     {'Lrule': inpute_data[3],'Lid': inpute_data[0]}]#修改数据封装
        try:
            inpute_data= self.get_league()
            if (inpute_data[0]==''):
                QMessageBox.warning(self, '提示', '请输入联赛id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Lname,league_dict[0])
                elif(update_field==field[1]):
                    db.execute(sql_Llevel, league_dict[1])
                elif (update_field == field[2]):
                    db.execute(sql_Lrule, league_dict[2])
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
        sql_id = "delete from League where Lid=:Lid"
        input = self.le_input.text()
        dic_id = {'Lid': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '请输入需删除联赛的id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if result:
                    QMessageBox.warning(self, '提示', '数据库中未找到该联赛信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '联赛信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
#查找
    def search(self):
        sql = "select*from League where Lid=:Lid"
        input = self.le_input.text()
        dic_id = {'Lid': input}
        headers = ['id', '联赛名称', '联赛等级','联赛规则']
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
        sql_all = 'select Team.Tid,Tname,Lname,Llevel,Tpoints from Team,League,Attend ' \
                  'where Team.Tid=Attend.Tid and League.Lid=Attend.Lid order by Team.Tid'
        sql_byTpoints='select Team.Tid,Tname,Lname,Llevel,Tpoints from Team,League,Attend ' \
                    'where Team.Tid=Attend.Tid and League.Lid=Attend.Lid order by Tpoints desc'

        sql_byLname = 'select Team.Tid,Tname,Lname,Llevel,Tpoints from Team,League,Attend ' \
                      'where Team.Tid=Attend.Tid and League.Lid=Attend.Lid order by Lname'

        sql_byLlevel = 'select Team.Tid,Tname,Lname,Llevel,Tpoints from Team,League,Attend ' \
                      'where Team.Tid=Attend.Tid and League.Lid=Attend.Lid order by Llevel'

        sort_commond=self.comboBox_sort.currentText()#获取排序命令
        if(sort_commond=='' or sort_commond=='战队id'):
            sql=sql_all
        if (sort_commond == '积分'):
            sql = sql_byTpoints
        if (sort_commond == '联赛名称'):
            sql = sql_byLname
        if (sort_commond == '联赛等级'):
            sql = sql_byLlevel
        try:
            db = OracleDB()
            db.connect()
            league_list = db.query(sql)
            db.close()
            self.model = QStandardItemModel()
            # self.model.setColumnCount(4)  # 设置行数
            headers = ['战队id', '战队名', '联赛名称','联赛等级','积分']
            self.model.setHorizontalHeaderLabels(headers)  # 设置表头
            # 设置表头字体字号
            for i, header in enumerate(headers):
                item = QStandardItem(header)
                item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
                self.model.setHorizontalHeaderItem(i, item)
            # 将数据加载进model中
            for row, record in enumerate(league_list):
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

    def attend(self):
        sql_add = 'insert into Attend(Tid,Lid,Tpoints) values(:Tid,:Lid,:Tpoints)'
        try:
            Tid=self.le_Tid.text()
            Lid=self.le_Lid2.text()
            Tpoints=self.le_Tpoints.text()
            input_data=(Tid,Lid,Tpoints)
            if (input_data[0] == '' and input_data[1] == ''):
                QMessageBox.warning(self, '提示', '战队id或联赛id未输入', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                db.executemany(sql_add, [input_data])
                db.close()
                QMessageBox.warning(self, '提示', '信息已录入', QMessageBox.Yes)
        except Exception as e:
            # 发生错误时回滚事务
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def update2(self):
        Tid = self.le_Tid.text()
        Lid = self.le_Lid2.text()
        Tpoints = self.le_Tpoints.text()
        inpute_data = (Tid, Lid, Tpoints)
        sql_Tpoints = 'update Attend set Tpoints=:Tpoints where Tid=:Tid and Lid=:Lid'
        update_field = self.comboBox_Attendupdate.currentText()  # 获取需要修改的字段
        attend_dict={'Tpoints':Tpoints,'Tid':Tid,'Lid':Lid}
        try:
            if (inpute_data[0] == '' or inpute_data[1]==''):
                QMessageBox.warning(self, '提示', '请输入战队id和联赛id', QMessageBox.Yes)
            elif (update_field == '积分'):
                db = OracleDB()
                db.connect()
                db.execute(sql_Tpoints,attend_dict)
                db.close()
                QMessageBox.warning(self, '提示', '信息已修改', QMessageBox.Yes)
            else:
                QMessageBox.warning(self, '提示', '请选择修改字段', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def delete2(self):
        sql_id = "delete from Attend where Tid=:Tid and Lid=:Lid"
        Lid2 = self.le_Lid2.text()
        Tid=self.le_Tid.text()
        dic_input = {'Tid':Tid,'Lid': Lid2}
        try:
            if (Lid2 == '' or Tid==''):
                QMessageBox.warning(self, '提示', '请输入战队id和联赛id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                result = db.execute(sql_id, dic_input)
                db.close()
                if result:
                    QMessageBox.warning(self, '提示', '参赛信息已删除', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '参赛信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_league()
    window.show()
    sys.exit(app.exec_())
