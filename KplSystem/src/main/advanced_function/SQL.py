from __future__ import print_function
from __future__ import division
import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.sqlUI import Ui_Frame
from dsa.database import OracleDB
from dsa.sql import FilePath

class Win_SQL(Ui_Frame, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Frame, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(FilePath.file2))  # 图标设置
        self.db=OracleDB()
        self.radioButton.clicked.connect(self.onRadioButtonClicked)
        self.radioButton_2.clicked.connect(self.onRadioButtonClicked)
        self.btn_execute.clicked.connect(self.execute)#sql事件
        self.btn_clear.clicked.connect(self.clear)#清空

    def execute(self):
        sql = self.textEdit.toPlainText().strip(';')  # 获取查询语句
        option=self.onRadioButtonClicked()
        if(option==1):
            match = re.search(r'SELECT(.*?)FROM', sql, re.IGNORECASE)# 使用正则表达式提取SELECT和FROM之间的内容作为表格标题
            if match:
                self.db.connect()
                result = self.db.query(sql)  # 查询结果
                columns = match.group(1).strip().split(',')  # 提取列名
                formatted_result = "<html><head><style>table {border-collapse: collapse; width: 100%;} th, td {border: 1px solid #dddddd; text-align: left; padding: 8px;} th {background-color: #f2f2f2;} tr:nth-child(even) {background-color: #f2f2f2;} tr:hover {background-color: #e5e5e5;}</style></head><body><table>"
                formatted_result += "<tr>"
                for col in columns:
                    formatted_result += "<th>{}</th>".format(col.strip())
                formatted_result += "</tr>"
                for row in result:
                    formatted_result += "<tr>"
                    for value in row:
                        formatted_result += "<td>{}</td>".format(value)
                    formatted_result += "</tr>"
                formatted_result += "</table></body></html>"
                self.textBrowser.setHtml(formatted_result)
            else:
                self.textBrowser.setText("Invalid SELECT statement")  # 如果未找到SELECT和FROM之间的内容，显示错误信息
            self.db.close()
        elif(option==2):
            try:
                self.db.connect()
                self.db.execute(sql)
                self.db.close()
                self.textBrowser.setText("sql已执行")
            except Exception as e:
                self.db.conn.rollback()
                self.textBrowser.setText(str(e))
                self.db.close()
    # 槽函数
    def onRadioButtonClicked(self):
        if self.radioButton.isChecked():
            return 1
        elif self.radioButton_2.isChecked():
            return 2
    #清空
    def clear(self):
        self.textBrowser.clear()

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_SQL()
    window.show()
    sys.exit(app.exec_())
