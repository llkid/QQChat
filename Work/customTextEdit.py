#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/6/14 20:51
# @Author : shi
# @Project: python code
# @File   : customTextEdit.py


from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


class CustomTextEdit(QTextEdit):

    def __init__(self, parent):
        super(CustomTextEdit, self).__init__(parent)

    def keyPressEvent(self, e: QKeyEvent) -> None:
        QTextEdit.keyPressEvent(self, e)
        if e.key() == Qt.Key_Return:
            cursor = self.textCursor()
            cursor.clearSelection()
            cursor.deletePreviousChar()
            if self.toPlainText() != '':
                print(self.toPlainText())
                self.clear()

    @property
    def isEmpty(self):
        if self.toPlainText() == '':
            return True
        else:
            return False
