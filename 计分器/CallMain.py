# @Time : 2020/7/19 14:04
# @Author : YLXY
# @File : CallMain.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5 import QtCore, QtGui
from main import Ui_Form
import re

class Calu(QWidget,Ui_Form):
    def __init__(self):
        super(Calu, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.curNum = 1
        self.curAScore = 0
        self.curBScore = 0
        self.outputWritten('\t+---------------------------------------+')
        self.outputWritten('\t| 局数\t| 组名\t| 分数\t| 组名\t| 分数\t|')
        self.outputWritten('\t+---------------------------------------+')


        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.Timelabel.setText(text)

    def connecter(self):
        self.ResetButton.clicked.connect(self.reset)
        self.RecordButton.clicked.connect(self.record)

    def reset(self):
        self.AEdit.clear()
        self.BEdit.clear()
        self.AScoreEdit.clear()
        self.BScoreEdit.clear()
        self.textBrowser.clear()
        self.curNum = 1
        self.curAScore = 0
        self.curBScore = 0
        self.ANumber.display(self.curAScore)
        self.BNumber.display(self.curBScore)

    def record(self):
        A_score = self.AScoreEdit.text()
        B_score = self.BScoreEdit.text()
        A_name = self.AEdit.text()
        B_name = self.BEdit.text()
        if A_name == '' or B_name == '':
            reply = QMessageBox.warning(self, "警告", "<font size='9' color='white'>组名为空，请输入组名</font>")
            return
        elif A_score == '' or B_score == '':
            reply = QMessageBox.warning(self, '警告',"<font size='9' color='white'>填写内容为空，请输入当前分数！</font>")
            return
        elif re.match(r'^-?[0-9]{1,3}$', A_score) == None or re.match(r'^-?[0-9]{1,3}$', B_score) == None:
            reply = QMessageBox.warning(self, '警告',"<font size='9' color='white'>填写内容非法，请重新输入！</font>")
            return
        self.outputWritten('\t|   {}\t|  A组\t|  {}\t|  B组\t|  {}\t|'.format(self.curNum, A_score, B_score))
        self.outputWritten('\t+---------------------------------------+')
        self.curNum += 1
        self.curAScore += int(A_score)
        self.curBScore += int(B_score)
        self.AScoreEdit.clear()
        self.BScoreEdit.clear()
        self.ANumber.display(self.curAScore)
        self.BNumber.display(self.curBScore)
        if self.curAScore >= 1000 :
            reply = QMessageBox.information(self, "恭喜", "<font size='9' color='white'>恭喜{}组获胜！！！</font>".format(self.AEdit.text()))
        elif self.curBScore >= 1000:
            reply = QMessageBox.information(self, "恭喜", "<font size='9' color='white'>恭喜{}组获胜！！！</font>".format(self.BEdit.text()))


    def keyPressEvent(self, key):
        if key.key() == Qt.Key_Enter or key.key() == Qt.Key_Return:
            self.record()



    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text + '\n')
        # self.textBrowser.setTextCursor(cursor)
        # self.textBrowser.ensureCursorVisible()



if __name__  == "__main__":
    app = QApplication(sys.argv)
    calu = Calu()
    calu.show()
    sys.exit(app.exec())