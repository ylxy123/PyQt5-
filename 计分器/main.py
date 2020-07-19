# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 625)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 290, 581, 281))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"迷你简楷体\";\n"
"background-color: rgb(124, 124, 124);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 71, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.BNumber = QtWidgets.QLCDNumber(Form)
        self.BNumber.setGeometry(QtCore.QRect(410, 80, 141, 41))
        self.BNumber.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.BNumber.setObjectName("BNumber")
        self.ANumber = QtWidgets.QLCDNumber(Form)
        self.ANumber.setGeometry(QtCore.QRect(130, 80, 141, 41))
        self.ANumber.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.ANumber.setObjectName("ANumber")
        self.AEdit = QtWidgets.QLineEdit(Form)
        self.AEdit.setGeometry(QtCore.QRect(130, 20, 141, 41))
        self.AEdit.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"font: 20pt \"迷你简粗行楷\";\n"
"color: rgb(255, 255, 255);")
        self.AEdit.setObjectName("AEdit")
        self.BEdit = QtWidgets.QLineEdit(Form)
        self.BEdit.setGeometry(QtCore.QRect(410, 20, 141, 41))
        self.BEdit.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"迷你简粗行楷\";")
        self.BEdit.setObjectName("BEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 141, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.AScoreEdit = QtWidgets.QLineEdit(Form)
        self.AScoreEdit.setGeometry(QtCore.QRect(170, 140, 101, 41))
        self.AScoreEdit.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"font: 20pt \"迷你简粗行楷\";\n"
"color: rgb(255, 255, 255);")
        self.AScoreEdit.setObjectName("AScoreEdit")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(290, 140, 141, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.BScoreEdit = QtWidgets.QLineEdit(Form)
        self.BScoreEdit.setGeometry(QtCore.QRect(450, 140, 101, 41))
        self.BScoreEdit.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"font: 20pt \"迷你简粗行楷\";\n"
"color: rgb(255, 255, 255);")
        self.BScoreEdit.setObjectName("BScoreEdit")
        self.RecordButton = QtWidgets.QPushButton(Form)
        self.RecordButton.setGeometry(QtCore.QRect(60, 200, 171, 41))
        self.RecordButton.setStyleSheet("font: 20pt \"钟齐王庆华毛笔简体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 102, 102);")
        self.RecordButton.setObjectName("RecordButton")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 141, 51))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.Timelabel = QtWidgets.QLabel(Form)
        self.Timelabel.setGeometry(QtCore.QRect(200, 590, 361, 21))
        font = QtGui.QFont()
        font.setFamily("迷你简粗行楷")
        font.setPointSize(16)
        self.Timelabel.setFont(font)
        self.Timelabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.Timelabel.setObjectName("Timelabel")
        self.ResetButton = QtWidgets.QPushButton(Form)
        self.ResetButton.setGeometry(QtCore.QRect(340, 200, 171, 41))
        self.ResetButton.setStyleSheet("font: 20pt \"钟齐王庆华毛笔简体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 102, 102);")
        self.ResetButton.setObjectName("ResetButton")
        self.label_7.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.BNumber.raise_()
        self.ANumber.raise_()
        self.AEdit.raise_()
        self.BEdit.raise_()
        self.label_5.raise_()
        self.AScoreEdit.raise_()
        self.label_6.raise_()
        self.BScoreEdit.raise_()
        self.RecordButton.raise_()
        self.Timelabel.raise_()
        self.ResetButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.AEdit, self.BEdit)
        Form.setTabOrder(self.BEdit, self.AScoreEdit)
        Form.setTabOrder(self.AScoreEdit, self.BScoreEdit)
        Form.setTabOrder(self.BScoreEdit, self.RecordButton)
        Form.setTabOrder(self.RecordButton, self.ResetButton)
        Form.setTabOrder(self.ResetButton, self.textBrowser)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "计分器"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'迷你简楷体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", " A组："))
        self.label_2.setText(_translate("Form", " B组："))
        self.label_3.setText(_translate("Form", "总分："))
        self.label_4.setText(_translate("Form", "总分："))
        self.label_5.setText(_translate("Form", "当前得分："))
        self.label_6.setText(_translate("Form", "当前得分："))
        self.RecordButton.setText(_translate("Form", "记  录"))
        self.label_7.setText(_translate("Form", "SCORE:"))
        self.Timelabel.setText(_translate("Form", "Time"))
        self.ResetButton.setText(_translate("Form", "重  置"))
import qr_rc
