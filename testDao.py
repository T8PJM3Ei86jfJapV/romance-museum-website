#-*-coding:utf-8-*-

from handler.dao import *

def main():
    uid = 'testid'
    nickname = '昵称nick123'
    psw = '000000'
    email = '10000@qq.com'
    qq = '10000'

    # 测试用：article
    # aid为11位long类型，插入时自动生成并返回
    title = '标题title'
    mode = '类型mode'
    content = '内容content'

    # 注册新用户
    outcome = register_user(uid, nickname, psw, email, qq)
    print outcome, type(outcome)
    # output: 0 <type 'long'>

    # 用户已存在
    outcome = register_user(uid, nickname, psw, email, qq)
    print outcome, type(outcome)
    # 验证失败返回-1：
    # output: -1 <type 'int'>

    # 获取用户信息
    outcome = get_user_info(uid)
    if len(outcome) != 0:
        data = outcome[0]
        print data
    # {'qq': u'10000', 'nickname': u'\u6635\u79f0nick123', 'email': u'10000@qq.com'}

    # 获取不存在的用户的信息
    outcome = get_user_info('unknown_user')
    print outcome, type(outcome)
    # output: [] <type 'list'>

    # 用户验证通过
    outcome = verify_user(uid, psw);
    print outcome, type(outcome)
    # output: True <type 'bool'>

    # 用户验证失败
    outcome = verify_user('unknown_user', psw);
    print outcome, type(outcome)
    # output: False <type 'bool'>

    # 插入文章，返回文章id: long
    outcome = add_article(uid, title, mode, content)
    print outcome, type(outcome)
    # 每次插入，返回自增id值(long)，如：
    # 1 <type 'long'>
    # 2 <type 'long'>
    # 3 <type 'long'>
    # ...

    # 根据用户id(uid)，查找其所有文章id(aid)：
    outcome = get_articles(uid)
    print outcome
    # output: [{'aid': 1L}, {'aid': 2L}, {'aid': 3L}]

    # 根据文章id(aid)，查找文章：
    aid = 1L
    outcome = get_article(aid)
    print outcome
    # [{'qq': u'10000', 'uid': u'testid', 'title': u'\u6807\u9898title', 'content': u'\u5185\u5bb9content', 'mode': u'\u7c7b\u578bmode', 'nickname': u'\u6635\u79f0nick123', 'email': u'10000@qq.com'}]

    # 获取最新n条文章：
    outcome = get_random_articles(10);
    print outcome
    # output: [{'aid': 1L}, {'aid': 2L}, {'aid': 3L}]

if __name__ == "__main__":
	main()