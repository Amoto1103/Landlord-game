from socket import *
import sys
import pickle
from Casino import UI_MAIN
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from game_player import Player
import pygame
import hashlib
import numpy as np
import zzai as ai


HOST = '192.168.1.106'
PORT = 3389
ADDR = (HOST, PORT)
BUFFERSIZE = 2048
VERIFY_TIPS = '最喜欢的(人、动物、书、电影或音乐等等)'


# 通信用子线程
class MyQthread(QThread):
    def __init__(self, func, args):
        super(MyQthread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args)
        self.exec()


# 客户端类，负责主流程控制
class GameClient(object):
    def __init__(self, sockfd):
        # 创建跟服务器沟通的tcp连接
        self.sockfd = sockfd
        # 设置是否开始游戏的属性默认值
        self.playing = False
        

    # 更新ui
    def update_gui(self, msg):
        msg = msg.split('-')
        if msg[0] == 'D':
            self.player.get_pokers(msg[1:], self.room)
        # 抢地主
        elif msg[0] == 'L':
            self.player.confirm_landlord(msg[1:], self.room, self.connfd)
        # 出牌
        elif msg[0] == 'S':
            self.player.confirm_send_pokers(msg[1:], self.room, self.connfd)
        elif msg[0] == 'F':
            self.playing = False
            self.handle_score(int(msg[2]), int(msg[1]))
            self.sockfd.send(('op_router-update_score-' + '#'.join(self.room.score_table)).encode())
            submit_rlt = self.sockfd.recv(10).decode()
            if submit_rlt == 'ok':
                self.player.update_info(self.room.score_table)
                self.refresh_playerinfo()
            tmp = int(self.room.score_table[3])
            self.room.close()
            self.room.t_child.exit(0)
            del self.room
            self.sound.stop()
            # 2为超时结算
                if msg[1] == '2' and self.player.pos == int(msg[2]):
                self.player.next_player('F', 2, self.connfd)
                self.enter_quickgame()
                self.room.show_result(0)
            if msg[1] == '0' or self.player.pos != int(msg[2]):
                
                self.enter_quickgame()
                if tmp:
                    self.room.show_result(1)
                else:
                    self.room.show_result(0)

    def handle_score(self, launcher, f_status):
        # 提交游戏结果，是否地主，房间号，得分，是否胜利
        self.room.score_table[2] = self.room.score_table[1] * self.room.score_table[2]
        self.room.score_table[1] = str(self.room.id)

        # 如果是逃跑，那么扣目前分数的双倍，其他人各加1倍分数
        if f_status:
            if self.player.pos == launcher:
                self.room.score_table[2] *= -2
                self.room.score_table[3] = '0'
            else:
                self.room.score_table[3] = '1'
        else:
            if self.room.score_table[0] == launcher:
                if self.player.pos == launcher:
                    self.room.score_table[2] *= 2
                    self.room.score_table[3] = '1'
                else:
                    self.room.score_table[2] *= -1
                    self.room.score_table[3] = '0'
            else:
                if self.player.pos == self.room.score_table[0]:
                    self.room.score_table[2] *= -2
                    self.room.score_table[3] = '0'
                else:
                    self.room.score_table[3] = '1'
        # 转成字符串，方便传参
        if self.room.score_table[2] < 0:
            self.room.score_table[2] = '_' + str(-1 * self.room.score_table[2])
        else:
            self.room.score_table[2] = str(self.room.score_table[2])

        if self.room.score_table[0] == self.player.pos:
            self.room.score_table[0] = '1'
        else:
            self.room.score_table[0] = '0'
        self.room.score_table.append(self.player.user_id)

    # 绑定信号
    def connect_singal(self):
        self.main.signal_msg.connect(self.update_gui)

    # 向服务器发送请求的接口函数
    def do_request(self, op):
        self.sockfd.send('-'.join(op).encode())

    # 进入房间，完成发牌，然后创建子线程来进行房间内各玩家的通信
    def enter_room(self):
        if not self.playing:
            self.playing = True
            self.room.label_result.hide()

            # 获取房间玩家的通信信息
            try:
                self.do_request(('op_router', 'match_room',str(self.id)))
                rdata = self.sockfd.recv(BUFFERSIZE)
                if not rdata:
                    return
                rdata = pickle.loads(rdata)
            except Exception as e:
                print(e)
                self.playing = False
                return
            self.player.pos = rdata[1].index(self.sockfd.getsockname())
            self.room.pos = self.player.pos
            self.room.id = rdata[0]
            self.nick = rdata[2]
            self.room.ai = False
            self.player.members = [(host, port % 10000 + 10000) for host, port in (set(rdata[1]) - {self.sockfd.getsockname()})]
            self.nick = [self.nick[(self.player.pos - 1) % 3], self.nick[(self.player.pos + 1) % 3], self.nick[self.player.pos]]
            self.room.print_nick(self.nick)
            
            # 启动接收消息的线程
            self.room.t_child = MyQthread(self.recv_msg_and_notify, self.player.members)
            self.room.t_child.start()

            # 设置按钮
            self.room.pass_landlord.setText(QCoreApplication.translate("room", "不抢"))
            self.room.pass_landlord.clicked.connect(lambda:self.player.get_landlord(0, self.room, self.connfd))
            self.room.pass_landlord.show()
            self.room.get_landlord.setText(QCoreApplication.translate("room", "抢地主"))
            self.room.get_landlord.clicked.connect(lambda:self.player.get_landlord(1, self.room, self.connfd))

            self.room.pass_poker.setText(QCoreApplication.translate("room", "不出"))
            self.room.pass_poker.clicked.connect(lambda:self.player.send_pokers(0, self.room, self.connfd))
            self.room.send_poker.setText(QCoreApplication.translate("room", "出牌"))
            self.room.send_poker.clicked.connect(lambda:self.player.send_pokers(1, self.room, self.connfd, self.main.signal_msg))

            self.room.tuoguan.clicked.connect(lambda:self.ai_or_not(1))
            self.room.butuoguan.clicked.connect(lambda:self.ai_or_not(0))
            
            self.room.deck = ai.Deck()
            self.room.deck.shangjiaNum = 17
            self.room.deck.xiajiaNum = 17

            self.room.cardList = []

            # 发牌
            self.player.deal(self.room, self.connfd)
            self.room.tuoguan.show()

    def recv_msg_and_notify(self, members):
        while self.playing:
            data, addr = self.connfd.recvfrom(BUFFERSIZE)
            if not data:
                break
            elif addr not in members:
                continue
            try:
                data = data.decode()
            except UnicodeDecodeError as e:
                data = str(self.player.pos) + repr(data)
            self.main.signal_msg.emit(data)
            if data[0] == 'F':
                self.connfd.sendto('end the thread'.encode(), addr)
                break
        print('child threading quit')

    # 登录
    def login(self, login, account, passwd):
        passwd = self.md5(passwd)
        self.sockfd.send(('op_router-login-' + account + '#' + passwd).encode())
        data = self.sockfd.recv(10).decode().split(' ')
        if data[0] == 'ok':
            # 登录成功后，创建游戏大厅，玩家，房间等对象
            self.main = UI_MAIN.UImainwindow()
            self.connect_singal()
            self.playerinfo = UI_MAIN.UIplayerinfo()
            self.player = Player(self.sockfd, data[1])
            self.id=data[1]

            # 创建跟其他客户端通信的套接字connfd
            self.connfd = socket(AF_INET, SOCK_DGRAM)
            # 因为每个玩家使用的客户端代码都是一样的，所以都需要绑定固定的端口，而且算法统一，我采取是对10000取余，然后再加10000，避免跟其他应用重复端口
            self.connfd.bind((self.sockfd.getsockname()[0], self.sockfd.getsockname()[1] % 10000 + 10000))

            login.close()
            self.main.show()
            self.refresh_playerinfo()
            # 主界面个人信息按钮弹窗
            self.main.Button_playerinfo.clicked.connect(self.playerinfo.OPEN)
            self.main.Button_quickgame.clicked.connect(self.enter_quickgame)
            self.playerinfo.pushButton_ok.clicked.connect(
                lambda: self.change_nickname(self.player.game_info['nickname'], self.playerinfo.lineEdit_gamename.text()))
        elif data[0] == 'failed':
            login.login_error()
        elif data[0] == 'logged':
            login.login_error(1)

    def refresh_playerinfo(self):
        self.player.get_player_info()
        self.player.get_rank_list()
        # 显示个人积分
        self.main.show_coins(str(self.player.game_info['score']))
        # 显示个人信息
        self.playerinfo.set_gamename(self.player.game_info['nickname'])
        self.playerinfo.show_winpercent(str(self.player.game_info['win_rate']) + '%')
        self.playerinfo.show_lcdnumbs(self.player.game_info['total_games'],
                                      self.player.game_info['total_landlord'])
        # 排行榜
        self.main.rank_list(self.player.rank_score, self.player.rank_wrate)

    # 快速游戏，进行界面切换，进入到房间，调用enter_room函数
    def enter_quickgame(self):
        self.room = UI_MAIN.UIroom()
        self.main.close()
        self.room.OPEN()

        # 初始化房间参数
        self.room.status = [True, True, True]
        self.room.poker_num = [17, 17, 17]
        self.room.landlord_num = 0
        self.room.signal_msg = self.main.signal_msg
        # 房间的积分表格，第一个为是否为地主，第二个为底分，第三个为倍数，第四个为是否获胜
        self.room.score_table = [-1, 1, 1, -1]
        self.room.label.setText(QCoreApplication.translate("room", "积分: %d" % self.player.game_info['score']))

        # 播放背景音乐
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("./pic/background.wav")
        self.sound.set_volume(1)
        self.sound.play(-1)

        # 点击返回，重新显示大厅
        def back():
            self.sound.stop()
            if self.playing:
                self.player.next_player('F', 1, self.connfd)
                self.main.signal_msg.emit('F-1-' + str(self.player.pos))
            else:
                self.room.close()
                del self.room
            self.main.show()
        self.room.back_to_hall.clicked.connect(back)
        self.room.get_landlord.clicked.connect(self.enter_room)

    # 修改昵称
    def change_nickname(self, old, new):
        if old == new:
            return
        self.sockfd.send(('op_router-change_nickname-' + old + '#' + new).encode())
        self.refresh_playerinfo()

    # 重置密码
    def reset_passwd(self, account, reset_passwd):
        newpasswd = reset_passwd.lineEdit_passwordconfirm.text()
        newpasswd = self.md5(newpasswd)
        self.sockfd.send(('op_router-reset_passwd-' + account + '#' + newpasswd).encode())
        reset_passwd.close()

    # 确认验证信息
    def check_vrifinfo(self, reset_passwd):
        account = reset_passwd.lineEdit_account.text()
        vrifinfo = reset_passwd.lineEdit_vrifinfo.text()
        self.sockfd.send(('op_router-check_vrifinfo-' + account + '#' + vrifinfo).encode())
        data = self.sockfd.recv(10).decode()
        if not data:
            return
        elif data == 'ok':
            reset_passwd.Button_checkaccount.setEnabled(False)
            reset_passwd.lineEdit_password.setEnabled(True)
            reset_passwd.lineEdit_passwordconfirm.setEnabled(True)
            reset_passwd.Button_ok.setEnabled(True)
            reset_passwd.Button_ok.clicked.connect(lambda: self.reset_passwd(
                account, reset_passwd))

    # 判断注册信息是否填写完整
    def register_info(self, regr):
        params = 'op_router-register-'
        lineEdit_passwd = regr.lineEdit_password.text()
        lineEdit_passwdc = regr.lineEdit_passwordconfirm.text()

        if lineEdit_passwd != lineEdit_passwdc:
            self.register_error()
        elif not regr.lineEdit_account.text():
            self.register_error()
        elif not regr.lineEdit_password.text():
            self.register_error()
        elif not regr.lineEdit_vrifinfo.text():
            self.register_error()
        elif not regr.lineEdit_gamename.text():
            self.register_error()
        else:
            lineEdit_passwd = self.md5(lineEdit_passwd)
            params += regr.lineEdit_account.text() + '#'\
                + lineEdit_passwd + '#'\
                + regr.lineEdit_gamename.text() + '#'\
                + regr.lineEdit_vrifinfo.text() + '#'
            if regr.radioButton_male.isChecked():
                params += 'M'
            elif regr.radioButton_female.isChecked():
                params += 'F'
            else:
                self.register_error()
            self.sockfd.send(params.encode())
            data = self.sockfd.recv(10).decode()
            if data == 'succeed':
                regr.close()
                return True
            elif data == 'existed':
                print('用户名已存在!!!请重新输入!')
                return False

    def register_error(self):
        print('register_error')

    def md5(self, pwd):
        return hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()

    def ai_or_not(self,i):
        if i==1:    #1表示要托管
            self.room.tuoguan.hide()
            self.room.butuoguan.show()
            self.room.ai=True
        elif i==0:  #0表示取消托管
            self.room.tuoguan.show()
            self.room.butuoguan.hide()
            self.room.ai=False
            
def main():
    app = QApplication(sys.argv)
    login = UI_MAIN.UIlogin()
    register = UI_MAIN.UIregister()
    reset_passwd = UI_MAIN.UIreset_password()
    sockfd = socket()
    sockfd.connect(ADDR)
    client = GameClient(sockfd)
    login.show()
    login.Button_login.clicked.connect(\
        lambda :client.login(login, login.lineEdit_account.text(), login.lineEdit_password.text()))

    login.Button_register.clicked.connect(register.OPEN)
    login.Button_forgot.clicked.connect(reset_passwd.OPEN)

    register.Button_ok.clicked.connect(lambda: login.register_tips_label.setText(QCoreApplication.translate('Login',
                                      ("注册成功，请登录！" if (client.register_info(register)) == True else ''))))

    reset_passwd.Button_checkaccount.clicked.connect(lambda: client.check_vrifinfo(reset_passwd))

    sys.exit(app.exec_())
    sockfd.close()


if __name__ == '__main__':
    main()
