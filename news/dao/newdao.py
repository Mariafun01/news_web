'''
这个类的功能是用来操作New对象
从Mysql获取New数据，用来导入新闻信息到服务端
'''
from urllib import request

from news.pojo.mynews import News, Comments, Users, UserNews, Labels, NewsLabels, Fnames
from news.pojo.mynews import Categorys
from user import models
from utils.mysql_helper import MySqlDbHelper

# 新闻
class NewDao():
    '''
    这个类的功能是用来操作Book对象
    '''

    def get_list(self) -> list:
        '''
        获取全部新闻信息
        :return:
        '''
        sql = 'select * from tb_News'
        rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
        news = []
        for row in rows:
            new = News()  # 新闻对象
            new.id = row["id"]
            new.title = row["title"]
            new.author = row["author"]
            new.create_date = row["create_date"]
            new.description = row['description']
            new.text = row["text"]
            new.category_id = row["category_id"]
            # new.category = row["category_id"].name
            news.append(new)
        return news


    def add(self, new) -> int:
        '''
        添加图书
        :parambook:
        :return:受影响的行数
        '''
        pass


    def update(self, new) -> int:
        pass


    def delete(self, id) -> int:
        '''
        删除
        :paramid:
        :return:
        '''
        pass
    # 此函数用于判断新闻的收藏状态
    def fav_save(self,id,uid):
        # uid 是否收藏id的新闻
        # if uid 收藏ID
        #     删除该ID
        # else
        new=models.New.objects.get(id=id)
        user=models.Users.objects.get(id=uid)
        ret = user.news.filter(id=id).exists()
        # 如果显示已收藏状态，点击按钮切换未收藏状态
        # 已收藏状态下，能够获得fav_new
        # fav_new = request.POST.get('fav_new')
        # print(fav_new)
        # # 未收藏状态下，能够获得not_fav_new
        # not_fav_new = request.POST.get('not_fav_new')
        print("----->",id,"用户编号：",uid,"ret",ret)
        # print(not_fav_new)
        if ret:
            user.news.remove(new)
            return 0
        else:

            user.news.add(new)
            return 1

        pass

# 新闻类别
class CategoryDao():
    '''
    这个类的功能是用来操作Category对象
    '''

    def get_list(self) -> list:
        '''
        获取全部新闻分类信息
        :return:
        '''
        sql = 'select * from tbCategory'
        rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
        categorys = []
        for row in rows:
            category = Categorys()  # 新闻对象
            category.id = row["id"]
            category.name = row["name"]
            categorys.append(category)
        return categorys


    def add(self, category) -> int:
        '''
        添加图书
        :parambook:
        :return:受影响的行数
        '''
        pass


    def update(self, category) -> int:
        pass


    def delete(self, id) -> int:
        '''
        删除
        :paramid:
        :return:
        '''
        pass

# 评论
class CommentDao():
    '''
    这个类的功能是用来操作Book对象
    '''

    def get_list(self) -> list:
        '''
        获取全部新闻信息
        :return:
        '''
        sql = 'select * from tbComments'
        rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
        comments = []
        for row in rows:
            comment = Comments()  # 新闻对象
            comment.id = row["id"]
            comment.title = row["title"]
            comment.text = row["text"]
            comment.createDate = row["createDate"]
            comment.createUser_id = row["createUser_id"]
            comment.new_id = row['new_id']
            comments.append(comment)
        return comments


    def add(self, comment) -> int:
        '''
        添加图书
        :parambook:
        :return:受影响的行数
        '''
        pass


    def update(self, comment) -> int:
        pass


    def delete(self, id) -> int:
        '''
        删除
        :paramid:
        :return:
        '''
        pass

# 用户
class UserDao():
    '''
    这个类的功能是用来操作Book对象
    '''

    def get_list(self) -> list:
        '''
        获取全部新闻信息
        :return:
        '''
        sql = 'select * from users'
        rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
        users = []
        for row in rows:
            user = Users()  # 新闻对象
            user.id = row["id"]
            user.name = row["name"]
            user.phone = row["phone"]
            user.gender = row["gender"]
            user.birthday = row["birthday"]
            user.province = row['province']
            user.city = row["city"]
            user.district = row["district"]
            user.id_card_number = row["id_card_number"]
            user.email = row["email"]
            user.password = row['password']
            user.state = row['state']
            users.append(user)
        return users


    def add(self, user) -> int:
        '''
        添加图书
        :parambook:
        :return:受影响的行数
        '''
        pass


    def update(self, user) -> int:
        pass


    def delete(self, id) -> int:
        '''
        删除
        :paramid:
        :return:
        '''
        pass

# 用户收藏
class UserNewsDao():
        '''
        这个类的功能是用来操作Book对象
        '''

        def get_list(self) -> list:
            '''
            获取全部新闻信息
            :return:
            '''
            sql = 'select * from tbUserNews'
            rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
            usernews = []
            for row in rows:
                usernew = UserNews()  # 新闻对象
                usernew.id = row["id"]
                usernew.users_id = row["users_id"]
                usernew.new_id = row["new_id"]

                usernews.append(usernew)
            return usernews

        def add(self, usernew) -> int:
            '''
            添加图书
            :parambook:
            :return:受影响的行数
            '''
            pass

        def update(self, usernew) -> int:
            pass

        def delete(self, id) -> int:
            '''
            删除
            :paramid:
            :return:
            '''
            pass


# 标签
class LabelDao():
        '''
        这个类的功能是用来操作Book对象
        '''

        def get_list(self) -> list:
            '''
            获取全部新闻信息
            :return:
            '''
            sql = 'select * from tbLabel'
            rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
            labels = []
            for row in rows:
                label = Labels()  # 新闻对象
                label.id = row["id"]
                label.name = row["name"]

                labels.append(label)
            return labels

        def add(self, label) -> int:
            '''
            添加图书
            :parambook:
            :return:受影响的行数
            '''
            pass

        def update(self, label) -> int:
            pass

        def delete(self, id) -> int:
            '''
            删除
            :paramid:
            :return:
            '''
            pass


# 新闻标签
class NewsLabelsDao():
        '''
        这个类的功能是用来操作Book对象
        '''

        def get_list(self) -> list:
            '''
            获取全部新闻信息
            :return:
            '''
            sql = 'select * from tbNewsLabels'
            rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
            newslabels = []
            for row in rows:
                newslabel = NewsLabels()  # 新闻对象
                newslabel.id = row["id"]
                newslabel.new_id = row["new_id"]
                newslabel.label_id = row["label_id"]

                newslabels.append(newslabel)
            return newslabels

        def add(self, newslabel) -> int:
            '''
            添加图书
            :parambook:
            :return:受影响的行数
            '''
            pass

        def update(self, newslabel) -> int:
            pass

        def delete(self, id) -> int:
            '''
            删除
            :paramid:
            :return:
            '''
            pass


# 图片名
class FnameDao():
        '''
        这个类的功能是用来操作Book对象
        '''

        def get_list(self) -> list:
            '''
            获取全部新闻信息
            :return:
            '''
            sql = 'select * from tbFname'
            rows = MySqlDbHelper.query(sql)  # 执行查询了,返回的是字典
            fnames = []
            for row in rows:
                fname = Fnames()  # 新闻对象
                fname.id = row["id"]
                fname.fname = row["fname"]
                fname.new_id = row["new_id"]

                fnames.append(fname)
            return fnames

        def add(self, fname) -> int:
            '''
            添加图书
            :parambook:
            :return:受影响的行数
            '''
            pass

        def update(self, fname) -> int:
            pass

        def delete(self, id) -> int:
            '''
            删除
            :paramid:
            :return:
            '''
            pass