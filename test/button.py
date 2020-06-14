#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/6/12 0:40
# @Author : shi
# @Project: python code
# @File   : button.py


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton, QMenu, QApplication, QWidget, QAction
from PyQt5.QtCore import QTimer
import sys


class Example(QWidget):
    def initUI(self):
        self.setObjectName('Widget')
        self.resize(400, 300)
        self.setAutoFillBackground(False)

        self.bt1 = QPushButton("这是什么", self)

        self.bt2 = QPushButton('发送验证码', self)

        menu = QMenu()
        self.action1 = QAction('我是')
        # menu.addAction('我是')
        # menu.addSeparator()
        # menu.addAction('世界上')
        # menu.addSeparator()
        # menu.addAction('最帅的')
        # actions = [QAction('我是'), QAction('世界上'), QAction('最帅的')]
        # menu.addActions([QAction('我是'), QAction('世界上'), QAction('最帅的')])
        # [menu.insertSeparator(action) for action in actions]
        menu.addAction(self.action1)

        self.bt1.setMenu(menu)

        self.count = 10

        self.bt2.clicked.connect(self.Action)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.bt1.move(100, 100)
        _translate = QtCore.QCoreApplication.translate
        self.action1.setText(_translate('Widget', '按Enter键发送消息'))
        self.show()

    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)

    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count) + '秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.initUI()
    sys.exit(app.exec_())
