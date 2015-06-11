#-*-coding:utf-8-*-

import torndb

try:
    import sae
except ImportError:
    import saemonitor as sae

DB_HOST = "%s:%d" % (sae.const.MYSQL_HOST, sae.const.MYSQL_PORT)
DB_NAME = sae.const.MYSQL_DB
DB_USER = sae.const.MYSQL_USER
DB_PSWD = sae.const.MYSQL_PASS

def execute(sql):
    try:
        db = torndb.Connection(DB_HOST, DB_NAME, user = DB_USER, password = DB_PSWD, time_zone = "+8:00")
        outcome = db.execute(sql)
    except:
        outcome = -1
    finally:
        try:
            db.close()
        except:
            pass
    return outcome

def query(sql):
    try:
        db = torndb.Connection(DB_HOST, DB_NAME, user = DB_USER, password = DB_PSWD, time_zone = "+8:00")
        outcome = db.query(sql)
    except:
        print '[Failed] Executing \"' + sql + '\"'
        outcome = None
    finally:
        try:
            db.close()
        except:
            pass
    return outcome

def update_user_info(uid, nickname, psw, email, qq):
    pass

def register_user(uid, nickname, psw, email, qq):
    sql = 'INSERT INTO user(u_id, u_nickname, u_password, u_email, u_qq) VALUES(\"%s\", \"%s\", \"%s\", \"%s\", \"%s\");' % (uid, nickname, psw, email, qq);
    outcome = execute(sql)
    return outcome

def get_user_info(uid):
    sql = """SELECT u_nickname AS nickname,
    u_email AS email,
    u_qq AS qq
    FROM user WHERE u_id = \"%s\" LIMIT 1;""" % uid
    return query(sql)

def verify_user(uid, psw):
    sql = """SELECT u_password AS password FROM user WHERE u_id = \"%s\" LIMIT 1;""" % uid
    result = query(sql)
    if len(result) != 0:
        password = result[0].password
        return (password == psw)
    else:
        return False

def get_random_articles(num):
    sql = 'SELECT a_id FROM article LIMIT %d;' % num
    outcome = query(sql)
    return outcome

def add_article(uid, tittle, mode, content):
    sql = 'INSERT INTO article(u_id, a_tittle, a_mode, a_content) VALUES(\"%s\", \"%s\", \"%s\", \"%s\");' % (uid, tittle, mode, content);
    outcome = execute(sql)
    return outcome

def get_articles(uid):
    sql = 'SELECT a_id AS aid FROM article WHERE u_id = \"%s\";' % uid
    return query(sql)

def get_article(aid):
    sql = """SELECT article.u_id AS uid,
    article.a_tittle AS tittle,
    article.a_mode AS mode,
    article.a_content AS content,
    user.u_nickname AS nickname
    FROM user, article
    WHERE a_id = %d;""" % aid
    return query(sql)

def get_version():
    sql = 'SELECT VERSION() AS version;'
    return query(sql)

if __name__ == "__main__":
    # 测试用：user
    uid = 'testid'
    nickname = '昵称nick123'
    psw = '000000'
    email = '10000@qq.com'
    qq = '10000'

    # 测试用：article
    # aid为11位long类型，插入时自动生成并返回
    tittle = '标题tittle'
    mode = '类型mode'
    content = '内容content'

    # 注册新用户
    # outcome = register_user(uid, nickname, psw, email, qq)
    # print outcome, type(outcome)
    # output: 0 <type 'long'>

    # 用户已存在
    # outcome = register_user(uid, nickname, psw, email, qq)
    # print outcome, type(outcome)
    # 验证失败返回-1：
    # output: -1 <type 'int'>

    # 获取用户信息
    # outcome = get_user_info(uid)
    # if len(outcome) != 0:
    #     data = outcome[0]
    #     print data
        # output: {'qq': u'10000', 'nickname': u'\u6635\u79f0nick123', 'email': u'10000@qq.com'}

    # 获取不存在的用户的信息
    # outcome = get_user_info('unknown_user')
    # print outcome, type(outcome)
    # output: [] <type 'list'>

    # 用户验证通过
    # outcome = verify_user(uid, psw);
    # print outcome, type(outcome)
    # output: True <type 'bool'>

    # 用户验证失败
    # outcome = verify_user('unknown_user', psw);
    # print outcome, type(outcome)
    # output: False <type 'bool'>

    # 插入文章，返回文章id: long
    # outcome = add_article(uid, tittle, mode, content)
    # print outcome, type(outcome)
    # 每次插入，返回自增id值(long)，如：
    # 1 <type 'long'>
    # 2 <type 'long'>
    # 3 <type 'long'>
    # ...

    # 根据用户id(uid)，查找其所有文章id(aid)：
    # outcome = get_articles(uid)
    # print outcome
    # output: [{'aid': 1L}, {'aid': 2L}, {'aid': 3L}]

    # 根据文章id(aid)，查找文章：
    # aid = 1L
    # outcome = get_article(aid)
    # print outcome
    # [{'content': u'\u5185\u5bb9content', 'tittle': u'\u6807\u9898tittle', 'nickname': u'\u6635\u79f0nick123', 'uid': u'testid', 'mode': u'\u7c7b\u578bmode'}]

    # 获取最新n条文章：
    # outcome = get_random_articles(10);
    # print outcome
    # output: [{'a_id': 1L}, {'a_id': 2L}, {'a_id': 3L}]


