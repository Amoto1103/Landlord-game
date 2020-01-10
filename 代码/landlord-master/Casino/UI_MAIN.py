from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .UI_Mainwindow import mainwindow
from .UI_login import login
from .UI_register import register
from .UI_playerinfo_dialog import playerinfo
from .UI_reset_passwd import reset_password
from .Ui_room import room
import sys


class UIreset_password(reset_password):
    def __init__(self):
        super(UIreset_password, self).__init__()


class UIplayerinfo(playerinfo):
    def __init__(self):
        super(UIplayerinfo, self).__init__()


class UImainwindow(mainwindow):
    signal_msg = pyqtSignal(str)
    def __init__(self):
        super(UImainwindow, self).__init__()


class UIregister(register):
    def __init__(self):
        super(UIregister, self).__init__()


class UIlogin(login):
    def __init__(self):
        super(UIlogin, self).__init__()


class UIroom(room):
    def __init__(self):
        super(UIroom, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = UImainwindow()
    login = UIlogin()
    register = UIregister()
    playerinfo = UIplayerinfo()
    reset_passwd = UIreset_password()
    login.show()
    main.show()
    sys.exit(app.exec_())
