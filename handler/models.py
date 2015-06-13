#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web
import dao

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie("id")
        if id:
            self.redirect('/')
        else:
            self.render('reg.html')

    def post(self):
        user = self.get_argument('user', None)
        password = self.get_argument('password', None)
        repassword = self.get_argument('repassword', None)
        name = self.get_argument('name',None)
        email = self.get_argument('email',None)
        qq = self.get_argument('qq', None)
        if user == None:
            self.redirect('/signup')
            return
        if password == None or repassword == None or not password == repassword:
            self.redirect('/signup')
            return
        if name == None:
            self.redirect('/signup')
            return
        if email == None:
            self.redirect('/signup')
            return
        '''
        check and save data
        '''

        # 插入新用户
        outcome = dao.register_user(user, name, password, email, qq)
        if outcome == -1:
            # 用户名已存在
            return

        self.set_secure_cookie("id", user)
        self.set_secure_cookie("name", name)
        self.redirect('/')
        
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie("id")
        name = self.get_secure_cookie("name")
        if id:
            self.redirect('/')
        else:
            self.render('login.html')

    def post(self):
        user = self.get_argument('user', None)
        password = self.get_argument('password', None)

        # 用户验证
        valid = dao.verify_user(user, password)

        if valid: #check information if true
            # 获取用户信息
            outcome = dao.get_user_info(user)
            if len(outcome) != 0:
                data = outcome[0]
                name = data.nickname
            else:
                name = 'name'

            self.set_secure_cookie("id", user)
            self.set_secure_cookie("name", name)
            self.redirect('/')
        else:
            self.redirect('/login')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

# 未实现
class UpdateUserInfoHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("name")
        id = self.get_secure_cookie("id")
        self.render('change_info.html', name = name,id = id)
    
    def post(self):
        id = self.get_secure_cookie("id")
        new_name = self.get_argument('userName')
        old_password = self.get_argument('orginalPassword')
        new_password = self.get_argument('newPassword')
        new_repassword = self.get_argument('password-confirm')
        new_mail = self.get_argument('email')
        new_qq = self.get_argument('qq')
        if id: #check id and old_password if true
            #update information
            self.redirect('/profile/'+str(id))

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("id", '')
        self.set_secure_cookie("name", '')
        self.redirect('/')

class MailboxHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie("id")
        name = self.get_secure_cookie("name")

        # get 5 random Article for (artid,title,userid,name)
        # txts = [(1000,"title1",1000,"author1"),(1001,"title2",1001,"author1")]

        txts = list()
        # 获取最新n条文章的id(aid)：
        aids = [item.aid for item in dao.get_random_articles(5)]
        for aid in aids:
            article = dao.get_article(aid)[0]
            txt = (aid, article.title, article.uid, article.nickname)
            txts.append(txt)

        if id:
            self.render('read_message.html',id = id, name = name, allTxts = txts)
        else:
            self.redirect('/login')


class ArticleHandler(tornado.web.RequestHandler):
    def get(self, ArticleID):
        id = self.get_secure_cookie("id")
        name = self.get_secure_cookie("name")
        if ArticleID:
            # 获取article
            article = dao.get_article(ArticleID)[0]
            art_info = {"Title":article.title,"Artid":ArticleID,"Content":article.content,"Autid":article.uid,"Autname":article.nickname,"Autmail":article.email,"Autqq":article.qq}#get those information
            self.render('article.html', name = name,id = id,txt = art_info)
        else:
            self.redirect('/error')


class UserInfoHandler(tornado.web.RequestHandler):
    def get(self, UserID):
        name = self.get_secure_cookie("name")
        # 获取用户信息
        info = dao.get_user_info(UserID)[0]
        mail = info.email #get mail
        qq = info.qq #get qq

        # from userid get list for (artid, title)
        # artlist = [(1000,'ART1'),(1001,"ART2")]
        artlist = list()
        aids = [item.aid for item in dao.get_articles(UserID)]
        for aid in aids:
            article = dao.get_article(aid)[0]
            art = (aid, article.title)
            artlist.append(art)

        muslist = [(1000,'mus1'),(1001,'mus2')]
        if name:
            self.render('user_info.html', name = name, mail = mail, qq = qq, id = UserID,arts = artlist,muss = muslist)
        else:
            self.redirect('/error')

class MuseumHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("name")
        id = self.get_secure_cookie("id")
        self.render('imageItem.html', name = name, id =id)

class AdminLoginHandler(tornado.web.RequestHandler):
    def get(self):
        # id = self.get_secure_cookie("id")
        # if id:
        #     self.redirect('/')
        # else:
        self.render('adminLogin.html')

    def post(self):
        id =self.get_argument("id")
        paw = self.get_argument("password")
        print(id)
        print(paw)
        if id == "admin" and paw == "admin":
            self.set_secure_cookie("id", id)
            self.set_secure_cookie("name", 'admin')
            self.redirect('/adminManage')
        else:
            self.redirect('/adminlogin')
            
class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie('id')
        print("ahahah")
        print(id)
        if id == "admin":
            # all article title and id
            # artlist= [{"title":"t1","aid":1000},{"title":"t2","aid":1001}]
            artlist = dao.show_all_articles()
            self.render('adminManage.html', name = "admin", id = id)
        else:
            self.redirect('/')

class NewblogHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie('id')
        name = self.get_secure_cookie('name')
        if id:
            self.render('createArticleItem.html', name= name, id = id)
        else:
            self.redirect('/login')
            
    # def post(self):
    #     uid = self.get_secure_cookie('id')
    #     title = self.get_argument("title")
    #     content = self.get_argument("content")
    #     mode = self.get_argument("mode")
    #     if title and content and mode:
    #         # save article and return article id
    #         # artid = "1000"
    #         artid = dao.add_article(uid, title, mode, content)
    #         self.redirect('/article/'+artid)
class NewCreateArticleHandler(tornado.web.RequestHandler):
    def post(self):
        uid = self.get_secure_cookie('id')
        uri = self.request.body
        print(self.request.body)
    
        title = ''
        mode = ''
        content = ''
        for i in uri.split('&'):
            data = i.split('=')
            if data[0] == 'title':
                title = data[1]
            if data[0] == 'mode':
                mode = data[1]
            if data[0] == 'html':
                content = data[1]



        if title:
            if mode:
                if content:
                    # save article and return article id
                    # artid = "1000"
                    artid = dao.add_article(uid, title, mode, content)
                    # self.redirect('/article/'+ str(artid))
                    self.write(str(artid))
                    self.finish()

        
class NewexhHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('createImageItem.html')

