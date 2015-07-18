#!/usr/bin/env python
#coding:utf-8

#如果文件里面有汉字，避免出现乱码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.models import IndexHandler
from handler.models import SignupHandler
from handler.models import LoginHandler
from handler.models import UserInfoHandler
from handler.models import LogoutHandler
from handler.models import UpdateUserInfoHandler
from handler.models import MailboxHandler
from handler.models import MuseumHandler
from handler.models import AdminLoginHandler
from handler.models import AdminHandler, ArticleHandler,NewblogHandler,NewexhHandler, NewCreateArticleHandler
#from handler.models import HTTP404Error

url = [
    (r'/', IndexHandler),
    (r'/signup', SignupHandler),
    (r'/login', LoginHandler),
    (r'/profile/(\w+)', UserInfoHandler),
    (r'/logout', LogoutHandler),
    (r'/update', UpdateUserInfoHandler),
    (r'/mailbox', MailboxHandler),
    # (r'/museum', MuseumHandler),
    (r'/adminlogin',AdminLoginHandler),
    (r'/adminManage', AdminHandler),
    (r'/article/(\w+)', ArticleHandler),
    (r'/newBlog', NewblogHandler),
    (r'/newExhibit', NewexhHandler),
    (r'/createArticle', NewCreateArticleHandler)
    #(r'.*', HTTP404Error)
]
