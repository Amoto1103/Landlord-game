# -*- coding: utf-8 -*- 

# Form implementation generated from reading ui file 'playerinfo_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_playerinfo_dialog(object):
    def setupUi(self, playerinfo_dialog):
        playerinfo_dialog.setObjectName("playerinfo_dialog")
        playerinfo_dialog.resize(400, 300)
        playerinfo_dialog.setMinimumSize(QtCore.QSize(400, 300))
        playerinfo_dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.pushButton_ok = QtWidgets.QPushButton(playerinfo_dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(240, 240, 80, 25))
        self.pushButton_ok.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_ok.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.layoutWidget = QtWidgets.QWidget(playerinfo_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 30, 191, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_gamename = QtWidgets.QLabel(self.layoutWidget)
        self.label_gamename.setMinimumSize(QtCore.QSize(80, 25))
        self.label_gamename.setMaximumSize(QtCore.QSize(80, 25))
        self.label_gamename.setObjectName("label_gamename")
        self.horizontalLayout.addWidget(self.label_gamename)
        self.lineEdit_gamename = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_gamename.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_gamename.setMaximumSize(QtCore.QSize(100, 25))
        self.lineEdit_gamename.setObjectName("lineEdit_gamename")
        self.horizontalLayout.addWidget(self.lineEdit_gamename)
        self.layoutWidget1 = QtWidgets.QWidget(playerinfo_dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 80, 188, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_total_gametimes = QtWidgets.QLabel(self.layoutWidget1)
        self.label_total_gametimes.setMinimumSize(QtCore.QSize(80, 25))
        self.label_total_gametimes.setMaximumSize(QtCore.QSize(80, 25))
        self.label_total_gametimes.setObjectName("label_total_gametimes")
        self.horizontalLayout_2.addWidget(self.label_total_gametimes)
        self.lcdNumber_total_gametimes = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.lcdNumber_total_gametimes.setMinimumSize(QtCore.QSize(100, 25))
        self.lcdNumber_total_gametimes.setMaximumSize(QtCore.QSize(100, 25))
        self.lcdNumber_total_gametimes.setObjectName("lcdNumber_total_gametimes")
        self.horizontalLayout_2.addWidget(self.lcdNumber_total_gametimes)
        self.layoutWidget2 = QtWidgets.QWidget(playerinfo_dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 180, 188, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_winpercent = QtWidgets.QLabel(self.layoutWidget2)
        self.label_winpercent.setMinimumSize(QtCore.QSize(80, 25))
        self.label_winpercent.setMaximumSize(QtCore.QSize(80, 25))
        self.label_winpercent.setObjectName("label_winpercent")
        self.horizontalLayout_3.addWidget(self.label_winpercent)
        self.label_show_winpercent = QtWidgets.QLabel(self.layoutWidget2)
        self.label_show_winpercent.setMinimumSize(QtCore.QSize(100, 25))
        self.label_show_winpercent.setMaximumSize(QtCore.QSize(100, 25))
        self.label_show_winpercent.setObjectName("label_show_winpercent")
        self.horizontalLayout_3.addWidget(self.label_show_winpercent)
        self.layoutWidget3 = QtWidgets.QWidget(playerinfo_dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(100, 130, 188, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_dizhu_gametimes = QtWidgets.QLabel(self.layoutWidget3)
        self.label_dizhu_gametimes.setMinimumSize(QtCore.QSize(80, 25))
        self.label_dizhu_gametimes.setMaximumSize(QtCore.QSize(80, 25))
        self.label_dizhu_gametimes.setObjectName("label_dizhu_gametimes")
        self.horizontalLayout_4.addWidget(self.label_dizhu_gametimes)
        self.lcdNumber_dizhu_gametimes = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.lcdNumber_dizhu_gametimes.setMinimumSize(QtCore.QSize(100, 25))
        self.lcdNumber_dizhu_gametimes.setMaximumSize(QtCore.QSize(100, 25))
        self.lcdNumber_dizhu_gametimes.setObjectName("lcdNumber_dizhu_gametimes")
        self.horizontalLayout_4.addWidget(self.lcdNumber_dizhu_gametimes)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.pushButton_ok.raise_()

        self.retranslateUi(playerinfo_dialog)
        QtCore.QMetaObject.connectSlotsByName(playerinfo_dialog)

    def retranslateUi(self, playerinfo_dialog):
        _translate = QtCore.QCoreApplication.translate
        playerinfo_dialog.setWindowTitle(_translate("playerinfo_dialog", "个人信息"))
        self.pushButton_ok.setText(_translate("playerinfo_dialog", "OK"))
        self.label_gamename.setText(_translate("playerinfo_dialog", "昵称"))
        self.lineEdit_gamename.setText(_translate("playerinfo_dialog", "xxx"))
        self.label_total_gametimes.setText(_translate("playerinfo_dialog", "总局数"))
        self.label_winpercent.setText(_translate("playerinfo_dialog", "胜率"))
        self.label_show_winpercent.setText(_translate("playerinfo_dialog", "TextLabel"))
        self.label_dizhu_gametimes.setText(_translate("playerinfo_dialog", "做地主局数"))

