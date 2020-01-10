#2019年6月3日 by hyl
from socket import *
from threading import Condition, current_thread
import sys
import pickle
import my_thread
from setting import *
import pymysql
from db.mysql_load import *

class GameServer(object):
    def __init__(self, addr):
        self.addr = addr
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        self.serverName = addr[0]
        self.serverPort = addr[1]
        self.queue = []
        self.room = {}
        self.online = {}
        self.rid = [0]
        self.tmp_rid = 0
        self.con = Condition()

    def serverForever(self):
        #服务器启动函数，接收客户端请求，创建新的线程
        while True:
            print('Waiting for a connection...')
            print(self.queue, '队列中')
            connfd, clientAddr = self.sockfd.accept()
            clientThread = my_thread.MyThread(self.handleRequest, (connfd,clientAddr))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self, connfd, addr):
            try:
                data = connfd.recv(BUFFERSIZE).decode()
            except OSError:
                data = ''
            if not data:
                for i in self.online:
                    if self.online[i] == addr:
                        del self.online[i]
                        break
                connfd.close()
                current_thread().stoped = True
                return
            data = data.split(OPS_DELIMITER)
            if len(data) > 2:
                module = data[0]
                app = data[1]
                params = data[2].split(PARAM_DELIMITER)
            else:
                module = data[0]
                app = data[1]
                params = []
            if app == 'match_room':
                self.con.acquire()
                id = params[0]
                record = (addr,id)
                pass_room=[]
                sql_select=[]
                if record not in self.queue:
                    self.queue.append(record)
                if len(self.queue) >= 3:
                    self.con.notify(3)
                    self.tmp_rid = self.generate_rid()
                    self.room[self.tmp_rid] = self.queue[:3]
                else:
                    self.con.wait()
                sql_select = [pass_name(self.room[self.tmp_rid][0][1]), pass_name(self.room[self.tmp_rid][1][1]), pass_name(self.room[self.tmp_rid][2][1])]
                pass_room = [self.room[self.tmp_rid][0][0], self.room[self.tmp_rid][1][0], self.room[self.tmp_rid][2][0]]
                connfd.send(pickle.dumps((self.tmp_rid, pass_room, sql_select)))
                self.queue = self.queue[3:]
                self.con.release()
                return
            elif app == 'login' or app == 'player_info':
                params.append(self.online)
            elif app == 'update_score':
                if int(params[0]):
                    self.room.pop(int(params[1]))
                    self.rid[int(params[1]) - 1] = 0
            sys.path.insert(0, HDL_ROOT)
            # 交互模块
            m = __import__(module)
            application = getattr(m, app)
            if not params:
                application(connfd)
            else:
                application(connfd, params)

    def generate_rid(self):
        tmp_lst = [x for x in range(len(self.rid))]
        if self.rid == tmp_lst:
            rid = self.rid[-1] + 1
            self.rid.append(rid)
        else:
            rid = list(filter(None, map(lambda x, y: x ^ y, self.rid, tmp_lst)))[0]
            self.rid[rid - 1] = rid
        return rid

# 控制服务器启动
def main():
    httpd = GameServer(ADDR)
    print('Serving HTTP on port', PORT)
    httpd.serverForever()

if __name__ == '__main__':
    main()
