# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Calvin/Downloads/study/Tedu/normal/project/game/test/room.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Room(object):
    def setupUi(self, room):
        room.setObjectName("room")
        room.resize(1000, 600)
        room.setMinimumSize(QtCore.QSize(1000, 600))
        room.setMaximumSize(QtCore.QSize(800, 400))

        self.centralwidget = QtWidgets.QWidget(room)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(room)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 61))
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 0, 200, 60))
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.back_to_hall = QtWidgets.QPushButton(self.frame)
        self.back_to_hall.setGeometry(QtCore.QRect(8, 8, 90, 50))
        self.back_to_hall.setObjectName("back_to_hall")
        self.player_sj = QtWidgets.QPushButton(room)
        self.player_sj.setGeometry(QtCore.QRect(20, 100, 100, 137))
        self.player_sj.setIconSize(self.player_sj.size())
        self.player_sj.setIcon(QtGui.QIcon("pic/gui/touxiang.png"))
        self.player_sj.setObjectName("player_sj")
        self.player_xj = QtWidgets.QPushButton(room)
        self.player_xj.setGeometry(QtCore.QRect(850, 110, 100, 137))
        self.player_xj.setIconSize(self.player_xj.size())
        self.player_xj.setIcon(QtGui.QIcon("pic/gui/touxiang.png"))
        self.player_xj.setObjectName("player_xj")
        self.player_self = QtWidgets.QPushButton(room)
        self.player_self.setGeometry(QtCore.QRect(20, 440, 100, 137))
        self.player_self.setIconSize(self.player_self.size())
        self.player_self.setIcon(QtGui.QIcon("pic/gui/touxiang.png"))
        self.player_self.setObjectName("player_self")
        self.graphicsViewMy = QtWidgets.QGraphicsView(room)
        self.graphicsViewMy.setGeometry(QtCore.QRect(145, 60, 711, 541))
        self.graphicsViewMy.setObjectName("graphicsViewMy")
        self.layoutWidget = QtWidgets.QWidget(room)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 295, 201, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pass_poker = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_poker.sizePolicy().hasHeightForWidth())
        self.pass_poker.setSizePolicy(sizePolicy)
        self.pass_poker.setMinimumSize(QtCore.QSize(0, 30))
        self.pass_poker.setObjectName("pass_poker")
        self.horizontalLayout_2.addWidget(self.pass_poker)
        self.send_poker = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_poker.sizePolicy().hasHeightForWidth())
        self.send_poker.setSizePolicy(sizePolicy)
        self.send_poker.setMinimumSize(QtCore.QSize(0, 30))
        self.send_poker.setObjectName("send_poker")
        self.horizontalLayout_2.addWidget(self.send_poker)
        self.send_poker.hide()
        self.pass_poker.hide()

        self.pass_landlord = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_landlord.sizePolicy().hasHeightForWidth())
        self.pass_landlord.setSizePolicy(sizePolicy)
        self.pass_landlord.setMinimumSize(QtCore.QSize(0, 30))
        self.pass_landlord.setObjectName("pass_landlord")
        self.horizontalLayout_2.addWidget(self.pass_landlord)
        self.get_landlord = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_landlord.sizePolicy().hasHeightForWidth())
        self.get_landlord.setSizePolicy(sizePolicy)
        self.get_landlord.setMinimumSize(QtCore.QSize(0, 30))
        self.get_landlord.setObjectName("get_landlord")
        self.horizontalLayout_2.addWidget(self.get_landlord)
        self.graphicsScene = QtWidgets.QGraphicsScene()

        self.rpokers_sj = QtWidgets.QLCDNumber(room)
        self.rpokers_sj.setGeometry(QtCore.QRect(40, 235, 64, 23))
        self.rpokers_sj.setObjectName("rpokers_sj")
        self.rpokers_self = QtWidgets.QLCDNumber(room)
        self.rpokers_self.setGeometry(QtCore.QRect(40, 410, 64, 23))
        self.rpokers_self.setObjectName("rpokers_self")
        self.rpokers_xj = QtWidgets.QLCDNumber(room)
        self.rpokers_xj.setGeometry(QtCore.QRect(870, 245, 64, 23))
        self.rpokers_xj.setObjectName("rpokers_xj")
        self.timer_lcd = QtWidgets.QLCDNumber(room)
        self.rpokers_self.setSegmentStyle(2)
        self.rpokers_sj.setSegmentStyle(2)
        self.rpokers_xj.setSegmentStyle(2)
        self.rpokers_self.setStyleSheet("background-color:MintCream;border:0px;")
        self.rpokers_sj.setStyleSheet("background-color:MintCream;border:0px;")
        self.rpokers_xj.setStyleSheet("background-color:MintCream;border:0px;")

        self.label_timer = QtWidgets.QLabel(room)
        self.label_timer.setMouseTracking(False)
        self.label_timer.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_timer.setTextFormat(QtCore.Qt.AutoText)
        self.label_timer.setObjectName("label_timer")
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        timer_palette = QtGui.QPalette()
        timer_palette.setBrush(self.label_timer.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap('pic/gui/alarm.png').scaled(50, 50)))
        self.label_timer.setPalette(timer_palette)
        self.label_timer.setAutoFillBackground(True)

        self.label_hat = QtWidgets.QLabel(room)
        self.label_hat.setMouseTracking(False)
        self.label_hat.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_hat.setTextFormat(QtCore.Qt.AutoText)
        self.label_hat.setObjectName("label_hat")
        hat_palette = QtGui.QPalette()
        hat_palette.setBrush(self.label_hat.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap('pic/gui/hat.png').scaled(50, 50)))
        self.label_hat.setPalette(hat_palette)
        self.label_hat.setAutoFillBackground(True)

        self.label_result = QtWidgets.QLabel(room)
        self.label_result.setMouseTracking(False)
        self.label_result.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_result.setTextFormat(QtCore.Qt.AutoText)
        self.label_result.setObjectName("label_result")
        self.win_palette = QtGui.QPalette()
        self.win_palette.setBrush(self.label_result.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap('pic/gui/win.png').scaled(400, 225)))
        self.lose_palette = QtGui.QPalette()
        self.lose_palette.setBrush(self.label_result.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap('pic/gui/lose.png').scaled(400, 225)))

        self.graphicsViewMy.raise_()
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.player_sj.raise_()
        self.player_xj.raise_()
        self.player_self.raise_()
        self.rpokers_sj.raise_()
        self.rpokers_self.raise_()
        self.rpokers_xj.raise_()
        self.timer_lcd.raise_()
        self.timer_lcd.hide()
        self.label_timer.raise_()
        self.label_timer.hide()

        self.graphicsViewMy.setScene(self.graphicsScene)
        self.graphicsViewMy.setSceneRect(QtCore.QRectF(0, 0, 705, 535))
        self.graphicsViewMy.setStyleSheet("background: transparent;border: none;")
        self.graphicsViewMy.show()


        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(5, 70, 81, 20))
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(840, 70, 100, 20))
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(5, 390, 81, 20))
        self.label3.setObjectName("label3")

        self.zuoqiang = QtWidgets.QLabel(self.centralwidget)
        self.zuoqiang.setGeometry(QtCore.QRect(235, 110, 81, 40))
        self.zuoqiang.setObjectName("zuoqiang")

        self.youqiang = QtWidgets.QLabel(self.centralwidget)
        self.youqiang.setGeometry(QtCore.QRect(720, 110, 81, 40))
        self.youqiang.setObjectName("youqiang")

        self.zuobuqiang = QtWidgets.QLabel(self.centralwidget)
        self.zuobuqiang.setGeometry(QtCore.QRect(235, 110, 81, 40))
        self.zuobuqiang.setObjectName("zuobuqiang")

        self.youbuqiang = QtWidgets.QLabel(self.centralwidget)
        self.youbuqiang.setGeometry(QtCore.QRect(720, 110, 81, 40))
        self.youbuqiang.setObjectName("youbuqiang")

        self.woqiang = QtWidgets.QLabel(self.centralwidget)
        self.woqiang.setGeometry(QtCore.QRect(480, 290, 81, 40))
        self.woqiang.setObjectName("woqiang")
        
        self.wobuqiang = QtWidgets.QLabel(self.centralwidget)
        self.wobuqiang.setGeometry(QtCore.QRect(480, 290, 81, 40))
        self.wobuqiang.setObjectName("wobuqiang")

        self.yaobuqi1 = QtWidgets.QLabel(self.centralwidget)
        self.yaobuqi1.setGeometry(QtCore.QRect(235, 110, 81, 40))
        self.yaobuqi1.setObjectName("yaobuqi1")

        self.yaobuqi2 = QtWidgets.QLabel(self.centralwidget)
        self.yaobuqi2.setGeometry(QtCore.QRect(720, 110, 81, 40))
        self.yaobuqi2.setObjectName("yaobuqi2")

        self.tuoguan = QtWidgets.QPushButton(self.frame)
        self.tuoguan.setGeometry(QtCore.QRect(900, 10, 60, 40))
        self.tuoguan.setObjectName("tuoguan")
        
        self.butuoguan = QtWidgets.QPushButton(self.frame)
        self.butuoguan.setGeometry(QtCore.QRect(900, 10, 60, 40))
        self.butuoguan.setObjectName("butuoguan")

        self.zuoqiang.hide()
        self.zuobuqiang.hide()
        self.youqiang.hide()
        self.youbuqiang.hide()
        self.woqiang.hide()
        self.wobuqiang.hide()
        self.yaobuqi1.hide()
        self.yaobuqi2.hide()

        self.butuoguan.hide()
        self.retranslateUi(room)
        QtCore.QMetaObject.connectSlotsByName(room)

        
    def retranslateUi(self, room):
        _translate = QtCore.QCoreApplication.translate
        room.setWindowTitle(_translate("room", "房间"))
        self.back_to_hall.setText(_translate("room", "返回大厅"))
        self.pass_landlord.hide()
        self.get_landlord.setText(_translate("room", "准备开始"))

        self.label1.setText(_translate("room", "1"))
        self.label2.setText(_translate("room", "2"))
        self.label3.setText(_translate("room", "3"))

        self.zuoqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">抢地主</span></p></body></html>"))
        self.youqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">抢地主</span></p></body></html>"))
        self.zuobuqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">不抢</span></p></body></html>"))
        self.youbuqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">不抢</span></p></body></html>"))
        self.woqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">抢地主</span></p></body></html>"))
        self.wobuqiang.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">不抢</span></p></body></html>"))

        self.yaobuqi1.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">要不起</span></p></body></html>"))
        self.yaobuqi1.setText(_translate("room", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">要不起</span></p></body></html>"))

        self.tuoguan.setText(_translate("room", "托管"))
        self.butuoguan.setText(_translate("room", "取消托管"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room = QtWidgets.QWidget()
    ui = Ui_Room()
    ui.setupUi(room)
    room.show()
    sys.exit(app.exec_())
