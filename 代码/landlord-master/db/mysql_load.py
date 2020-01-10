# 2019年6月3日 by hyl
from db.mysql_joker import mysqlpython
import setting
from pymysql import connect
import hashlib

def md5(pwd):
    return hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()

# 注册时，记录用户信息
def user_zhuce(username, pwd, nickname, verify, sex):
    conn = connect(**setting.MYSQL_CONFIG)
    cur = conn.cursor()
    passwd = md5(pwd)
    sql_insert = 'insert into user\
        (username,passwd,sex,verify) \
        values("%s","%s","%s","%s");' %\
        (username,passwd,sex,verify)
    sql_insert2 = 'insert into game_info\
        (nickname,user_id) values("%s","%s");'
    try:
        cur.execute(sql_insert)
        user_id = cur.lastrowid
        cur.execute(sql_insert2 % (nickname, user_id))
        conn.commit()
        print('注册成功')
        return True
    except Exception as e:
        print('用户名重复', e)
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

# 登录时，匹配用户信息
def user_login(username, pwd):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    passwd = md5(pwd)
    sql_select = 'select id, username,passwd from user\
                   where username="%s" and passwd="%s";'\
                   % (username, passwd)
    data = user.select_op(sql_select)
    if not data:
        return False
    else:
        print('登录成功')
        return data[0]

# 游戏信息
def select_game_info(user_id):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select nickname, score, if(total_games > 0, (win_games / total_games * 100), 0)  as win_rate, total_games, total_landlord from game_info\
                  where user_id="%d"' % int(user_id)
    data = user.select_op(sql_select)
    doc = {'nickname': data[0], 'score': data[1],
           'win_rate': round(data[2]), 'total_games': data[3],
           'total_landlord': data[4]}
    return doc


# 重置密码时，验证信息
def check_vrifinfo(username, verify):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select id from user\
                  where username="%s" and verify="%s"' % (username, verify)
    data = user.select_op(sql_select)
    if data:
        return True
    return False


# 重置密码
def reset_passwd(username, newpasswd):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    newpasswd = md5(newpasswd)
    sql_update = 'update user set passwd="%s" where username="%s"' % (
        newpasswd, username)
    user.Insert(sql_update)


# 完成结算
def update_score(user_id, win, score, landlord):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    if score[0] == '_':
      score = -int(score[1:])
    else:
      score = int(score)
    sql_update = 'update game_info set score=if(%d < 0 and score < -%d, 0, score + %d),\
               total_games = total_games+1,\
               total_landlord = total_landlord+%s,\
               win_games = win_games+%s\
               where user_id=%s;' % (score, score, score, landlord, win, user_id)
    try:
        user.Insert(sql_update)
        print('结算成功')
        return True
    except Exception as e:
        return False


# 游戏好友
def select_friends(user_id):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_select = 'select t2.user_id, t2.nickname, t2.score, if(t2.total_games > 0, (t2.win_games / t2.total_games * 100), 0)  as win_rate, t2.total_games, t2.total_landlord\
                  from user_friend as t1 left join game_info as t2 on t1.friend_id = t2.user_id\
                  where t1.user_id = %d' % int(user_id)
    result = user.select_opall(sql_select)
    doc = {}
    for info in result:
        doc[info[0]] = info[1:]
    return doc

# 游戏排名
def rank_list():
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql_score = 'select nickname,score from game_info where score > 0 order by score desc limit 10;'
    sql_wrate = 'select nickname,win_games / total_games * 100 as win_rate from game_info where total_games > 0 and win_games > 0 order by win_rate desc limit 10;'
    rlt_score = user.select_opall(sql_score)
    rlt_wrate = user.select_opall(sql_wrate)
    return rlt_score, rlt_wrate


# 修改昵称
def change_nickname(old_nickname,new_nickname):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql = 'update game_info set nickname = "%s" where \
           nickname = "%s";' % (new_nickname, old_nickname)
    user.Insert(sql)
    print('change nickname succeed')

# 战绩改变
def zhanji(nickname,player1,player2,fightinfo):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql = 'insert into zhanji(nickname,player1,player2,fightinfo)\
           values("%s","%s","%s","%s")'%(nickname,player1,player2,fightinfo)
    user.Insert(sql)
    print('ok')

# 战绩显示
def select_zhanji(nickname):
    user = mysqlpython('localhost', 3306, 'root', '123456', 'pokergame')
    sql = 'select * from zhanji where nickname = "%s";'%nickname
    result = user.select_opall(sql) 
    if not result:
        return
    lst_zhanji = []
    for res in result:
        lst = []
        for info in res:
            lst.append(info)
        lst[2] = [lst[2],select_userinfo(lst[2])]
        lst[3] = [lst[3],select_userinfo(lst[3])]
        lst_zhanji.append(lst)
    print(lst_zhanji)

# 名字传递
def pass_name(user_id):
    user = mysqlpython(**setting.MYSQL_CONFIG)
    sql = 'select nickname from game_info\
    where user_id="%d"' % int(user_id)
    sql = user.select_opall(sql)
    return  sql[0][0]
