# coding:utf-8

import os.path
import tornado.web
import dao
import urllib

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie("userId")
        print(id)
        if id:
            self.redirect('/')
        else:
            print("haha")
            self.render('reg.html')

    def post(self):
        user = self.get_argument('user', None)
        password = self.get_argument('password', None)
        repassword = self.get_argument('repassword', None)
        # name = self.get_argument('name',None)
        name = ""
        email = self.get_argument('email',None)
        qq = self.get_argument('qq', None)
        # if user == None:
        #     self.redirect('/signup')
        #     return
        # if password == None or repassword == None or not password == repassword:
        #     self.redirect('/signup')
        #     return
        #  if name == None:
        #     self.redirect('/signup')
        #      return
        # if email == None:
        #     self.redirect('/signup')
        #     return
        # '''
        # check and save data
        # '''
        outcome = dao.register_user(user, name, password, email, qq)
        if outcome == -1:
            return
            print("hahaha")
        else: 
            print(user)
            self.set_secure_cookie("userId", user)
            # self.set_secure_cookie("name", name)
            self.redirect('/')
        
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("userId")
        # name = self.get_secure_cookie("name")
        if user:
            self.redirect('/')
        else:
            self.render('login.html')

    def post(self):
        user = self.get_argument('user', None)
        password = self.get_argument('password', None)
        

        # userValidation
        valid = dao.verify_user(user, password)
        print(valid)

        if valid: #check information if true
            
            outcome = dao.get_user_info(user)
            if len(outcome) != 0:
                data = outcome[0]
                name = data.nickname
            else:
                name = 'name'

            self.set_secure_cookie("userId", user)
            # self.set_secure_cookie("name", name)
            self.redirect('/')
        else:
            self.redirect('/login')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_secure_cookie("userId")
        print(id)
        self.render('index.html', user = id)

class UpdateUserInfoHandler(tornado.web.RequestHandler):
    def get(self):
        # name = self.get_secure_cookie("name")
        user = self.get_secure_cookie("userId")
        self.render('change_info.html', user = user)
    
    def post(self):
        id = self.get_secure_cookie("id")
        # new_name = self.get_argument('userName')
        # old_password = self.get_argument('orginalPassword')
        # new_password = self.get_argument('newPassword')
        # new_repassword = self.get_argument('password-confirm')
        new_mail = self.get_argument('email')
        new_qq = self.get_argument('qq')
        print(new_mail)
        print(new_qq)
        if id: #check id and old_password if true
            #update information
            self.redirect('/profile/'+str(id))

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("userId", '')
        # self.set_secure_cookie("name", '')

        self.redirect('/')

class MailboxHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("userId")
        # name = self.get_secure_cookie("name")

        # get 5 random Article for (artid,title,userid,name)
        # txts = [(1000,"title1",1000,"author1"),(1001,"title2",1001,"author1")]

        articles = list()

        print(dao.get_mailbox_articles())
        
        aids = [item.a_id for item in dao.get_mailbox_articles()]
        for aid in aids:
            articleInfo = dao.get_article(aid)[0]
            print(articleInfo)
            article = (aid, articleInfo.title, articleInfo.uid, articleInfo.content)
            articles.append(article)

        print(articles)

        if user:
            self.render('read_message.html',user = user, articles = articles)
        else:
            self.redirect('/login')


class ArticleHandler(tornado.web.RequestHandler):
    def get(self, ArticleID):
        user = self.get_secure_cookie("userId")
        # name = self.get_secure_cookie("name")
        if ArticleID:
            # 获取article
            article = dao.get_article(ArticleID)[0]
            art_info = {"Title":article.title,"Artid":ArticleID,"Content":article.content,"Authorname":article.uid,"Authormail":article.email,"Authorqq":article.qq}
            # print(self)
            print(article.content)
            self.render('article.html', user = user, articleInfo = art_info)
        else:
            self.redirect('/error')


class UserInfoHandler(tornado.web.RequestHandler):
    def get(self, UserID):
        user = self.get_secure_cookie("userId")
       
        info = dao.get_user_info(UserID)[0]
        mail = info.email #get mail
        qq = info.qq #get qq

        # from userid get list for (artid, title)
        # artlist = [(1000,'ART1'),(1001,"ART2")]
        articles = list()
        aids = [item.aid for item in dao.get_articles(UserID)]
        for aid in aids:
            articleInfo = dao.get_article(aid)[0]
            print(articleInfo)
            article = (aid, articleInfo.title, articleInfo.content)
            articles.append(article)

        # muslist = [(1000,'mus1'),(1001,'mus2')]
        if user:
            self.render('user_info.html', user = user, mail = mail, qq = qq, articles = articles)
        else:
            self.redirect('/error')

class MuseumHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("userId")
        self.render('imageItem.html', user = user)

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
            self.set_secure_cookie("adminId", id)
            # self.set_secure_cookie("name", 'admin')
            self.redirect('/adminManage')
        else:
            self.redirect('/adminlogin')
            
class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie('adminId')
        print("ahahah")
        print(user)
        if user:
            # all article title and id
            # artlist= [{"title":"t1","aid":1000},{"title":"t2","aid":1001}]
            articles = dao.show_all_articles()
            print(articles)
            self.render('adminManage.html', user= user, articles = articles)
        else:
            self.redirect('/adminlogin')

class NewblogHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie('userId')
        # name = self.get_secure_cookie('name')
        if id:
            self.render('createArticleItem.html', user = user)
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
        uid = self.get_secure_cookie('userId')
        uri = self.request.body
        print(self.request.body)

        print(self.request.body.decode('ascii'))
    
        title = ''
        mode = ''
        content = ''
        data = []
        for item in uri.split('&'):
            data = item.split('=')
            if data[0] == 'title':
                title = data[1]
                wordList = title.split('+');
                title = ' '.join(wordList);
                title = urllib.unquote(title)
            if data[0] == 'html':

                content = data[1]
                wordList1 = content.split('+');
                content = ' '.join(wordList1);
                content = urllib.unquote(content)
            if data[0] == 'mode':
                mode = urllib.unquote(data[1])

        


        print(title)
        print(content)
        print(mode)



        if title:
            wordList = title.split('?');
            print(wordList)
            title = ' '.join(wordList);
            print(title)
            if mode:
                if content:
                    wordList1 = content.split('?');
                    print(wordList1)
                    content = ' '.join(wordList1);
                    print(content)
                    # save article and return article id
                    # artid = "1000"
                    artid = dao.add_article(uid, title, mode, content)
                    print('/article/'+ str(artid)) 
                    # self.redirect('/article/'+ str(artid))
                    self.write(str(artid))
                    # self.finish()

        
class NewexhHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('createImageItem.html')

