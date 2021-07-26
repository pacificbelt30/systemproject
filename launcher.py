#!/usr/bin/env python
import sys
import os
import atexit
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
#from Raspberrypi.GUI.Download import downloadMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dwnbtn = QPushButton('ダウンロード')
        self.dwnbtn.clicked.connect(lambda: self._click_func(1))
        self.upbtn = QPushButton('アップロード')
        self.upbtn.clicked.connect(lambda: self._click_func(2))
        self.mainbtn = QPushButton('出席管理')
        self.mainbtn.clicked.connect(lambda: self._click_func(3))

        layout = QVBoxLayout()
        layout.addWidget(self.dwnbtn)
        layout.addWidget(self.upbtn)
        layout.addWidget(self.mainbtn)
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def _click_func(self,num):
        if num == 1:
            path = os.path.join(os.path.dirname(__file__),'./Raspberrypi/GUI/Download.py')
        elif num == 2:
            path = os.path.join(os.path.dirname(__file__),'./Raspberrypi/GUI/upload.py')
        else:
            path = os.path.join(os.path.dirname(__file__),'./Raspberrypi/GUI/attendance_management_gui.py')
        if os.name == 'nt':#windows
            atexit.register(lambda:os.system('py '+path))
        elif os.name == 'posix':#linux or mac
            #os.system(path+ ' 1')
            atexit.register(lambda:os.system('python '+path))
        else:
            pass
        self.hide()
        QCoreApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
