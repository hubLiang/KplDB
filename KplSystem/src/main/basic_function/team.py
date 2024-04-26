from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from ui.teamUI import Ui_Team
from dsa.database import OracleDB
from dsa.sql import FilePath

class Win_Team(Ui_Team, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Team, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file2))  # 图标设置
        #事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.btn_display.clicked.connect(self.display)

    def add(self):
        sql_add = 'insert into Team(Tid, Tname,Tcity,Mid) values(:Tid,:Tname,:Tcity,:Mid)'
        try:
            input_data=self.get_team()
            if(input_data[0]==''or input_data[1]==''):
                QMessageBox.warning(self, '提示', 'id或战队名未输入', QMessageBox.Yes)
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

    def update(self):
        #sql语句
        sql_Tname = 'update Team set Tname=:Tname where Tid=:Tid'
        sql_Tcity = 'update Team set Tcity=:Tcity where Tid=:Tid'
        sql_Mid = 'update Team set Mid=:Mid where Tid=:Tid'
        field=['战队名','主场城市','经理id']#修改字段列表
        update_field=self.comboBox_Teamupdate.currentText()#获取需要修改的字段
        inpute_data = self.get_team()#输入数据
        team_dict = [{'Tname': inpute_data[1],'Tid': inpute_data[0]},{'Tcity': inpute_data[2],'Tid': inpute_data[0]},
                       {'Mid': inpute_data[3],'Tid': inpute_data[0]}]#修改数据封装
        try:
            inpute_data= self.get_team()
            if (inpute_data[0]==''):
                QMessageBox.warning(self, '提示', '请输入战队id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Tname,team_dict[0])
                elif(update_field==field[1]):
                    db.execute(sql_Tcity, team_dict[1])
                elif (update_field == field[2]):
                    db.execute(sql_Mid,team_dict[2])
                else:
                    QMessageBox.warning(self, '提示', '请选择要修改的字段！', QMessageBox.Yes)
                    return
                db.close()
                QMessageBox.warning(self, '提示', '信息已修改', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def delete(self):
        sql_id = "delete from Team where Tid=:Tid"
        input = self.le_input.text()
        dic_id = {'Tid': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '请输入需删除战队的id', QMessageBox.Yes)
            elif (input): #输入为id,则按id删除
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '战队基本信息已删除', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '战队基本信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def search(self):
        sql = "select*from Team where Tid=:Tid"
        input = self.le_input.text()
        dic_id = {'Tid': input}
        headers = ['id', '战队名', '主场城市', '经理']
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

    def display(self):
        # sql_all = 'select Team.* ,Mname from Team,Manager where Team.Mid=Manager.Mid'
        sql_all = 'select Team.* from Team'
        # sort_byid='select Team.* ,Mname from Team,Manager where Team.Mid=Manager.Mid ' \
        #           'order by Team.Tid'
        sort_byid = 'select Team.*  from Team ' \
                    'order by Team.Tid'

        # sort_byTname= 'select Team.* ,Mname from Team,Manager where Team.Mid=Manager.Mid  ' \
        #             'order by Tname'
        sort_byTname = 'select Team.* from Team  ' \
                       'order by Tname'

        sort_commond=self.comboBox_sort.currentText()#获取排序命令
        if(sort_commond==''):
            sql=sql_all
        elif(sort_commond=='id'):
            sql=sort_byid
        elif(sort_commond=='战队名'):
            sql=sort_byTname
        try:
            db = OracleDB()
            db.connect()
            Team_list = db.query(sql)
            db.close()
            self.model = QStandardItemModel()
            # self.model.setColumnCount(4)  # 设置行数
            headers = ['id', '战队名', '主场城市', '经理']
            self.model.setHorizontalHeaderLabels(headers)  # 设置表头
            # 设置表头字体字号
            for i, header in enumerate(headers):
                item = QStandardItem(header)
                item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
                self.model.setHorizontalHeaderItem(i, item)
            # 将数据加载进model中
            for row, record in enumerate(Team_list):
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
            # 设置行高
            # self.tableView.verticalHeader().setDefaultSectionSize(30) #设置行高
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    def get_team(self):
        Tid = self.le_Tid.text()
        Tname = self.le_Tname.text()
        Tcity=self.le_Tcity.text()
        Mid=self.le_Mid.text()
        input_data = (Tid, Tname,Tcity,Mid)
        return input_data


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_Team()
    window.show()
    sys.exit(app.exec_())


