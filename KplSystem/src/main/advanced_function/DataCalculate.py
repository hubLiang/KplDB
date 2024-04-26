from __future__ import print_function
from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.dataCalculateUI import Ui_DataCalculate
from dsa.database import OracleDB


class Win_DataCalculate(Ui_DataCalculate, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_DataCalculate, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应屏幕分辨率
    app = QtWidgets.QApplication(sys.argv)
    window=Win_DataCalculate()
    window.show()
    sys.exit(app.exec_())