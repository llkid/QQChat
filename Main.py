#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/5/14 21:29
# @Author : shi
# @Project: python code
# @File   : Main.py


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QAction, QMenu, QToolButton
from PyQt5.QtCore import Qt
from QQChat.From import coolChat_chat
import sys
import ctypes


class MainWindow(QtWidgets.QMainWindow, coolChat_chat.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

    def MainWindow_init(self):
        self.setupUi(self)
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QtGui.QColor(255, 255, 255))
        self.setPalette(palette)
        # 解决 win10 下底部工具栏图标显示异常问题
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("coolChat")
        self.setWindowOpacity(0.9)
        self.widget_init()
        self.show()

    def widget_init(self):
        menu = QMenu()
        # actionTest = QAction('测试Action', self)
        # 手动添加快捷键
        self.pushButton.setShortcut('Ctrl+1')
        actions = [self.actionEnter, self.actionCEnter]
        [action.setCheckable(True) for action in actions]
        menu.addActions(actions)
        self.pushButton_5.setMenu(menu)

    @QtCore.pyqtSlot(name='on_pushButton_clicked')
    def on_pushButton_clicked(self):
        print('表情')

    @QtCore.pyqtSlot(name='on_pushButton_2_clicked')
    def on_pushButton_2_clicked(self):
        print('动态图')

    @QtCore.pyqtSlot(name='on_pushButton_3_clicked')
    def on_pushButton_3_clicked(self):
        print('截图')

    @QtCore.pyqtSlot()
    def on_actionEnter_triggered(self):
        self.actionCEnter.setChecked(False)

    @QtCore.pyqtSlot()
    def on_msg_send_clicked(self):
        # toPlainText 将 textEdit 的内容转换成纯文本
        if not self.messageSendEdit.isEmpty:
            print(self.messageSendEdit.toPlainText())
            self.messageSendEdit.clear()
        else:
            print('None')

    @QtCore.pyqtSlot()
    def on_actionCEnter_triggered(self):
        self.actionEnter.setChecked(False)

    @QtCore.pyqtSlot()
    def on_pushButton_4_clicked(self):
        print('关闭')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.MainWindow_init()
    sys.exit(app.exec_())
