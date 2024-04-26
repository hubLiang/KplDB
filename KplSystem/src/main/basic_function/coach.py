from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from ui.coachUI import Ui_Coach
from dsa.database import OracleDB
from dsa.sql import FilePath

class Win_Coach(Ui_Coach, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Coach, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file2))  # 图标设置

        #事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.btn_display.clicked.connect(self.display)
        self.btn_assigning.clicked.connect(self.assign)
        self.btn_update2.clicked.connect(self.update2)
        self.btn_delete2.clicked.connect(self.delete2)

#录入
    def add(self):
        sql_add = 'insert into Coach(Cid,Cname,Cage,Csex) values(:Cid,:Cname,:Cage,:Csex)'
        try:
            input_data=self.get_coach()
            if(input_data[0]==''or input_data[1]==''):
                QMessageBox.warning(self, '提示', 'id或姓名未输入', QMessageBox.Yes)
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

# 更新/修改
    def update(self):
        #sql语句
        sql_Cname = 'update Coach set Cname=:Cname where Cid=:Cid'
        sql_Cage = 'update Coach set Cage=:Cage where Cid=:Cid'
        sql_Csex = 'update Coach set Csex=:Csex where Cid=:Cid'
        field=['姓名','年龄','性别']#修改字段列表
        update_field=self.comboBox_Coachupdate.currentText()#获取需要修改的字段
        inpute_data = self.get_coach()#输入数据
        Coach_dict = [{'Cname': inpute_data[1],'Cid': inpute_data[0]},{'Cage': inpute_data[2],'Cid': inpute_data[0]},
                       {'Csex': inpute_data[3],'Cid': inpute_data[0]}]#修改数据封装
        try:
            inpute_data= self.get_coach()
            if (inpute_data[0]==''):
                QMessageBox.warning(self, '提示', '请输入id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Cname,Coach_dict[0])
                elif(update_field==field[1]):
                    db.execute(sql_Cage, Coach_dict[1])
                elif (update_field == field[2]):
                    db.execute(sql_Csex, Coach_dict[2])
                else:
                    QMessageBox.warning(self, '提示', '请选择要修改的字段！', QMessageBox.Yes)
                    return
                db.close()
                QMessageBox.warning(self, '提示', '信息已修改', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    # 查找
    def search(self):
        sql1 = "select*from Coach where Cid=:Cid"
        sql2 = "select*from CT where Cid=:Cid"
        input = self.le_input.text()
        dic_id = {'Cid': input}
        headers1 = ['id', '姓名', '年龄', '性别']
        headers2 = ['教练id', '战队id','工资']
        select_search=['教练信息','分配信息']
        result = ''
        try:
            self.textBrowser.clear()  # 显示前清空
            if (input==''):
                QMessageBox.warning(self, '提示', '输入为空', QMessageBox.Yes)
            elif (self.comboBox_select_search.currentText()==select_search[0]):
                db = OracleDB()
                db.connect()
                data = db.query(sql1, dic_id)  # 查询结果
                data1=[str(x) for x in data[0]]#转为1维
                if (len(data1) == 0):
                    QMessageBox.warning(self, '查询失败', '数据库中未查询到', QMessageBox.Yes)
                else:
                    for i in range(len(headers1)):
                        result += str(headers1[i]) + ': ' + str(data1[i]) + '\n'
                    self.textBrowser.setText(result)#UI显示
                    db.close()
            elif (self.comboBox_select_search.currentText() == select_search[1]):
                db = OracleDB()
                db.connect()
                data = db.query(sql2, dic_id)  # 查询结果
                data1 = [str(x) for x in data[0]]  # 转为1维
                if (len(data1) == 0):
                    QMessageBox.warning(self, '查询失败', '数据库中未查询到', QMessageBox.Yes)
                else:
                    for i in range(len(headers2)):
                        result += str(headers2[i]) + ': ' + str(data1[i]) + '\n'
                    self.textBrowser.setText(result)  # UI显示
                    db.close()
            elif(self.comboBox_select_search.currentText()==''):
                self.textBrowser.clear()
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #删除Coach信息
    def delete(self):
        sql_id = "delete from Coach where Cid=:Cid"
        input = self.le_input.text()
        dic_id = {'Cid': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '请输入需删除教练的id', QMessageBox.Yes)
            elif (input): #输入为id,则按id删除
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '数据库中未找到教练基本信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '教练基本信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #教练分配
    def assign(self):
        sql_assign='insert into CT(Cid,Tid,Csalary) values(:Cid,:Tid,:Csalary)'
        Cid=self.le_Cid2.text()
        Tid=self.le_Tid.text()
        Csalsay=self.le_Csalary.text()
        CT_data=[(Cid,Tid,Csalsay)]
        try:
            if(Cid==''and Tid=='' ):
                QMessageBox.warning(self, '提示', '教练id与战队id未输入', QMessageBox.Yes)
            else:
                db=OracleDB()
                db.connect()
                db.executemany(sql_assign,CT_data)
                db.close()
                QMessageBox.warning(self, '提示', '分配信息已录入', QMessageBox.Yes)
        except Exception as e:
            # 发生错误时回滚事务
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #修改CT表
    def update2(self):
        sql_Tid = 'update CT set Tid=:Tid where Cid=:Cid'
        sql_Csalary= 'update CT set Csalary=:Csalary where Cid=:Cid'
        #输入获取
        Cid = self.le_Cid2.text()
        Tid = self.le_Tid.text()
        Csalary = self.le_Csalary.text()
        update_field=self.comboBox_CTupdate.currentText()#获取要修改的对象
        field=['战队id','工资']#字段列表
        update_Tid={'Cid': Cid, 'Tid': Tid}
        update_Csalary={'Cid':Cid,'Csalary':int(Csalary)}
        try:
            if(Cid==''):
                QMessageBox.warning(self, '提示','请输入教练id', QMessageBox.Yes)
            else:
                db=OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Tid,update_Tid)
                elif(update_field==field[1]):
                    db.execute(sql_Csalary, update_Csalary)
                else:
                    QMessageBox.warning(self, '提示', '请选择修改字段！', QMessageBox.Yes)
                    return
                db.close()
                QMessageBox.warning(self, '提示', '信息已修改', QMessageBox.Yes)
        except Exception as e:
            # 发生错误时回滚事务
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #CT表删除信息
    def delete2(self):
        sql_delete = "delete from CT where Cid=:Cid"
        Cid= self.le_Cid2.text()
        dic_id = {'Cid': Cid}
        try:
            if (Cid == ''):
                QMessageBox.warning(self, '提示', '请输入教练id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                result=db.execute(sql_delete, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '数据库中未找到教练分配信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '教练分配信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #显示
    def display(self):
        sql_all = 'select Coach.* ,Csalary,Tname from Coach,CT,Team where Coach.Cid=CT.Cid and CT.Tid = Team.Tid'
        sort_byid='select Coach.* ,Csalary,Tname from Coach,CT,Team where Coach.Cid=CT.Cid and CT.Tid = Team.Tid ' \
                  'order by Coach.Cid'
        sort_byage= 'select Coach.* ,Csalary,Tname from Coach,CT,Team where Coach.Cid=CT.Cid and CT.Tid = Team.Tid  ' \
                    'order by Cage'
        sort_bysalary ='select Coach.* ,Csalary,Tname from Coach,CT,Team where Coach.Cid=CT.Cid and CT.Tid = Team.Tid ' \
                     'order by Csalary desc'
        sort_commond=self.comboBox_sort.currentText()#获取排序命令
        if(sort_commond==''):
            sql=sql_all
        elif(sort_commond=='id'):
            sql=sort_byid
        elif(sort_commond=='年龄'):
            sql=sort_byage
        elif(sort_commond=='工资'):
            sql=sort_bysalary
        try:
            db = OracleDB()
            db.connect()
            Coach_list = db.query(sql)
            db.close()
            self.model = QStandardItemModel()
            self.model.setColumnCount(6)  # 设置行数
            headers = ['id', '姓名', '年龄', '性别','工资','所属战队']
            self.model.setHorizontalHeaderLabels(headers)  # 设置表头
            # 设置表头字体字号
            for i, header in enumerate(headers):
                item = QStandardItem(header)
                item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
                self.model.setHorizontalHeaderItem(i, item)
            # 将数据加载进model中
            for row, record in enumerate(Coach_list):
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
            #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动调整列宽
            # 设置行高
            self.tableView.verticalHeader().setDefaultSectionSize(30) #设置行高
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #获取输入coach表数据
    def get_coach(self):
        Pid = self.le_Cid.text()
        Pname = self.le_Cname.text()
        Page = self.le_Cage.text()
        Psex = self.le_Csex.text()
        input_data = (Pid, Pname, Page, Psex)
        return input_data


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_Coach()
    window.show()
    sys.exit(app.exec_())
