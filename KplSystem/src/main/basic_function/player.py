from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt
from ui.playerUI import Ui_Player
from dsa.database import OracleDB
from dsa.sql import FilePath
from dsa.algorithm import bubble_sort
from dsa.algorithm import quick_sort_2d
class Win_Player(Ui_Player, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Player, self).__init__()
        self.setupUi(self)
        # self.setGeometry(70, 100, 1178, 626)
        self.setWindowIcon(QtGui.QIcon(FilePath.file2))  # 图标设置


        # 事件绑定
        self.btn_add.clicked.connect(self.add)
        self.btn_update.clicked.connect(self.update)
        self.btn_search.clicked.connect(self.search)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_display.clicked.connect(self.display)
        self.btn_assigning.clicked.connect(self.assign)
        self.btn_update2.clicked.connect(self.update2)
        self.btn_delete2.clicked.connect(self.delete2)

    # 获取文本框输入
    def get_player(self):
        Pid = self.le_Pid.text()
        Pname = self.le_Pname.text()
        Page = self.le_Page.text()
        Psex = self.le_Psex.text()
        Plocation = self.le_Plocation.text()
        data = (Pid, Pname, Page, Psex, Plocation)
        return data

    # 检测是否有未输入
    def check(self, data):
        for item in data:
            if (item == ''):
                return False
        return True

    # 检测输入为id还是姓名
    def check_input_type(self, input):
        if (len(input) == 5):  # id长度为5
            return True
        else:
            return False

    # 录入
    def add(self):
        sql = 'insert into Player(Pid,Pname,Page,Psex,Plocation) values(:Pid,:Pname,:Page,:Psex,:Plocation)'
        try:
            data = self.get_player()
            if (self.check(data) == False):
                QMessageBox.warning(self, '提示', '信息未完整输入', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                db.executemany(sql, [data])
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
        sql_Pname = 'update Player set Pname=:Pname where Pid=:Pid'
        sql_Page = 'update Player set Page=:Page where Pid=:Pid'
        sql_Psex = 'update Player set Psex=:Psex where Pid=:Pid'
        sql_Plocation = 'update Player set Plocation=:Plocation where Pid=:Pid'
        field=['姓名','年龄','性别','主玩位置']#字段
        update_field=self.comboBox_Playerupdate.currentText()#获取需要修改的字段
        data = self.get_player()#输入数据
        player_dict = [{'Pname': data[1],'Pid': data[0]},{'Page': data[2],'Pid': data[0]},{'Psex': data[3],
                     'Pid': data[0]},{'Plocation': data[4],'Pid': data[0]}]#修改数据封装
        try:
            data = self.get_player()
            if (data[0]==''):
                QMessageBox.warning(self, '提示', '请输入信息', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Pname,player_dict[0])
                elif(update_field==field[1]):
                    db.execute(sql_Page, player_dict[1])
                elif (update_field == field[2]):
                    db.execute(sql_Psex, player_dict[2])
                elif (update_field == field[3]):
                    db.execute(sql_Plocation, player_dict[3])
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
        sql_id = "select*from Player where Pid=:Pid"
        sql_name = "select*from Player where Pname=:Pname"
        input = self.le_input.text()
        dic_id = {'Pid': input}
        dic_name = {'Pname': input}
        headers = ['id', '姓名', '年龄', '性别', '主玩位置']
        result = ''
        try:
            if (input==''):
                QMessageBox.warning(self, '提示', '输入为空', QMessageBox.Yes)
            elif (self.check_input_type(input)):  # 输入为id,则按id查询
                db = OracleDB()
                db.connect()
                data = db.query(sql_id, dic_id)  # 查询结果
                data1=[str(x) for x in data[0]]#转为1维
                if (len(data1) == 0):
                    QMessageBox.warning(self, '查询失败', '数据库中未查询到', QMessageBox.Yes)
                else:
                    for i in range(len(headers)):
                        result += str(headers[i]) + ': ' + str(data1[i]) + '\n'
                    self.textBrowser.setText(result)#UI显示
                    db.close()
            else:  # 输入为name,则按name查询
                db = OracleDB()
                db.connect()
                data= db.query(sql_name, dic_name)
                data1 = [str(x) for x in data[0]]  # 转为1维
                if (len(data1) == 0):
                    QMessageBox.warning(self, '查询失败', '数据库中未查询到', QMessageBox.Yes)
                else:
                    for i in range(len(headers)):
                        result += str(headers[i]) + ': ' + str(data1[i]) + '\n'
                        self.textBrowser.setText(result)  # UI显示
                    db.close()
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    # Player表删除
    def delete(self):
        sql_id = "delete from Player where Pid=:Pid"
        sql_name = "delete from Player where Pname=:Pname"
        input = self.le_input.text()
        dic_id = {'Pid': input}
        dic_name = {'Pname': input}
        try:
            if (input == ''):
                QMessageBox.warning(self, '提示', '输入为空', QMessageBox.Yes)
            elif (self.check_input_type(input)):  # 输入为id,则按id删除
                db = OracleDB()
                db.connect()
                result=db.execute(sql_id, dic_id)
                db.close()
                if not result:
                    QMessageBox.warning(self, '提示', '选手基本信息已删除', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '选手基本信息已删除', QMessageBox.Yes)
            else:  # 输入为name,则按删除
                db = OracleDB()
                db.connect()
                result=db.execute(sql_name, dic_name)
                db.close()
                if result:
                    QMessageBox.warning(self, '提示', '数据库中未找到该选手信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '选手基本信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #选手分派战队
    def assign(self):
        sql='insert into PT(Pid,Tid,Psalary,Pcaptain) values(:Pid,:Tid,:Psalary,:Pcaptain)'
        Pid=self.le_Pid2.text()
        Tid=self.le_Tid.text()
        Psalsay=self.le_Psalary.text()
        Pcaptain=self.replace(self.comboBox_Pcaptain.currentText())#字符转换为数字
        PT_data=[(Pid,Tid,Psalsay,Pcaptain)]
        try:
            if(Pid=='' or Tid==''):
                QMessageBox.warning(self, '提示', '选手或战队id为空', QMessageBox.Yes)
            else:
                db=OracleDB()
                db.connect()
                db.executemany(sql,PT_data)
                db.close()
                QMessageBox.warning(self, '提示', '信息已录入', QMessageBox.Yes)
        except Exception as e:
            # 发生错误时回滚事务
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()

    #修改PT表
    def update2(self):
        sql_Tid = 'update PT set Tid=:Tid where Pid=:Pid'
        sql_Psalary= "update PT set Psalary=:Psalary where Pid=:Pid"
        sql_Pcaptain = "update PT set Pcaptain=:Pcaptain where Pid=:Pid"
        #输入获取
        Pid = self.le_Pid2.text()
        Tid = self.le_Tid.text()
        Psalary = self.le_Psalary.text()
        Pcaptain = self.replace(self.comboBox_Pcaptain.currentText())  # 字符转换为数字
        update_field=self.comboBox_PTupdate.currentText()#获取要修改的对象
        field=['战队id','工资','队长？']#字段列表
        update_Tid={'Pid': Pid, 'Tid': Tid}
        update_Psalary={'Pid':Pid,'Psalary':Psalary}
        update_Pcaptain = {'Pid': Pid, 'Pcaptain': Pcaptain}
        try:
            if(Pid==''):
                QMessageBox.warning(self, '提示', '选手id为空', QMessageBox.Yes)
            else:
                db=OracleDB()
                db.connect()
                if(update_field==field[0]):
                    db.execute(sql_Tid,update_Tid)
                elif(update_field==field[1]):
                    db.execute(sql_Psalary, update_Psalary)
                elif (update_field == field[2]):
                    db.execute(sql_Pcaptain, update_Pcaptain)
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

    #PT表删除信息
    def delete2(self):
        sql_delete = "delete from PT where Pid=:Pid"
        Pid= self.le_Pid2.text()
        dic_id = {'Pid': Pid}
        try:
            if (Pid == ''):
                QMessageBox.warning(self, '提示', '请输入选手id', QMessageBox.Yes)
            else:
                db = OracleDB()
                db.connect()
                result=db.execute(sql_delete, dic_id)
                db.close()
                if result:
                    QMessageBox.warning(self, '提示', '数据库中未找到选手分派信息', QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, '提示', '选手分派信息已删除', QMessageBox.Yes)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
    #显示
    def display(self):
        sql_all = 'select Player.* ,Psalary,Pcaptain,Tname from Player,PT,Team where Player.Pid=PT.Pid and PT.Tid = Team.Tid'
        sql_1='select *from Player'
        sql_2='select *from PT'
        select = self.comboBox_select.currentText()  # 获取选择表
        sort_commond=self.comboBox.currentText()#获取排序命令
        headers = ['id', '姓名', '年龄', '性别', '主玩位置', '工资', '队长？', '所属战队']
        try:
            db = OracleDB()
            db.connect()
            if(select=='基本信息'):
                headers=headers[0:5]
                player_list1 = db.query(sql_1)
                player_list=[(x[0],x[1],x[2],x[3],x[4]) for x in player_list1]
                if(sort_commond=='id'):
                    player_list=bubble_sort(player_list,0)#按id排序
                elif (sort_commond == '年龄'):
                    # player_list = bubble_sort(player_list,2) #按年龄排序
                    player_list=quick_sort_2d(player_list,2)
            elif(select=='分配信息'):
                headers=['选手id','所属战队','工资','队长?']
                player_list2 = db.query(sql_2)
                player_list = [(x[0], x[1], x[2], x[3]) for x in player_list2]
                if (sort_commond == 'id'):
                    # player_list = bubble_sort(player_list, 0)  # 按id排序
                    player_list = quick_sort_2d(player_list, 0)
                elif (sort_commond == '工资'):
                    # player_list = bubble_sort(player_list, 2,True)  # 按工资排序
                    player_list = quick_sort_2d(player_list, 2,True)
            else:
                player_list = db.query(sql_all)
                if (sort_commond == 'id'):
                    # player_list = bubble_sort(player_list, 0)  # 按id排序
                    player_list = quick_sort_2d(player_list, 0)
                elif (sort_commond == '年龄'):
                    # player_list = bubble_sort(player_list, 2)  # 按年龄排序
                    player_list = quick_sort_2d(player_list, 2)
                elif (sort_commond == '工资'):
                    # player_list = bubble_sort(player_list, 5,True)  # 按工资降序排序
                    player_list = quick_sort_2d(player_list, 5, True)
            db.close()
            self.tablemodle(headers,player_list)
        except Exception as e:
            db.conn.rollback()
            QMessageBox.warning(self, '错误', 'Error:' + str(e), QMessageBox.Yes)
            db.close()
    #modle模型
    def tablemodle(self,headers,data:list):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(headers)  # 设置表头
        # 设置表头字体字号
        for i, header in enumerate(headers):
            item = QStandardItem(header)
            item.setFont(QFont('楷体', 10, QFont.Bold))  # 设置字体为10号
            self.model.setHorizontalHeaderItem(i, item)
        # 将数据加载进model中
        for row, record in enumerate(data):
            for column, value in enumerate(record):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # 设置数据居中显示
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)
        # 设置列宽
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        column_width = 70  # 置列宽为70
        for i in range(self.tableView.model().columnCount()):
            self.tableView.setColumnWidth(i, column_width)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动调整列宽
        # 设置行高
        self.tableView.verticalHeader().setDefaultSectionSize(30)  # 设置行高

    #替换，是：1，否：0
    def replace(self, str):
        if (str == '是'):
            str = 1
        elif (str == '否'):
            str = 0
        else:
            str = 0
        return str

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window = Win_Player()
    window.show()
    sys.exit(app.exec_())
