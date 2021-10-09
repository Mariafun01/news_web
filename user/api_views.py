"""
这个view，是用来提供api请求的
"""
import datetime
import json
import os
from decimal import Decimal

from django.contrib.auth.models import User
from django.http import HttpResponse

# @is_authenticate
from django.shortcuts import render

from user import models
from user.my_model_forms import UserModelForm
from utils.mywarps import authenticate
from utils.upload_helper import File_Upload_Helper
from news_web import settings


# 此方法用来序列化用户
def users_to_json(u):
    return {
        "id": u.id,
        "name": u.name,
        "phone": u.phone,
        "gender": u.gender,
        "birthday": u.birthday.strftime("%Y-%m-%d"),
        "province": u.province,
        "city": u.city,
        "district": u.district,
        "id_card_number": u.id_card_number,
        "email": u.email,
        "password": u.password,
        "state": u.state,
    }


# 获取单个用户信息
@authenticate
def userinfo(request):
    '''
        ajax请求，获取单个用户数据
        :param request:
        :return:
    '''
    json_str = None
    try:
        user_obj = models.Users.objects.get(phone=request.session['username'])
        result = {
            "success": 0,  # 成功标记
            "msg": "ok",
            "data": user_obj,  # 表示数据
        }
        json_str = json.dumps(result, default=users_to_json)
        print(json_str)
    except Exception as e:
        result = {
            "success": -1,  # 成功标记
            "msg": "查询失败:%s" % e,
        }
        json_str = json.dumps(result)  # 序列化json
    return HttpResponse(json_str)


# 更新用户信息
@authenticate
def userinfo_change(request):
    print('请求模式:', request.method)
    # id = request.POST.get("id")  # 获取要更新的用户ID   #RESTFUL风格请求
    json_str = None
    try:
        user_obj = models.Users.objects.get(phone=request.session['username'])

        # user = models.Users.objects.get(pk=id)  # 获取要更新的用户
        # 依次从 request.POST 里获取数据给user赋值
        user_obj.name = request.POST.get('name')
        user_obj.phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        user_obj.gender = int(gender)
        birthday = request.POST.get('birthday')
        user_obj.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        user_obj.province = request.POST.get('province')
        user_obj.city = request.POST.get('city')
        user_obj.district = request.POST.get('district')
        user_obj.id_card_number = request.POST.get('id_card_number')
        user_obj.email = request.POST.get('email')
        # user_obj.password = request.POST.get('password')
        # user_obj.state = request.POST.get('state')
        # user_obj.news = request.POST.get('news')
        user_obj.save()

        print('数据已成功获取到后端', user_obj)

        result = {
            "success": 0,  # 成功标记
            "msg": "ok",
            "data": user_obj,  # 表示数据
        }

        json_str = json.dumps(result, default=users_to_json)
        print('数据已成功转化成str', json_str)
    except Exception as e:
        result = {
            "success": -1,  # 标记失败
            "msg": "更新失败:%s" % e,
        }
        json_str = json.dumps(result)
        print(json_str)
    return HttpResponse(json_str)


# 此方法用来序列化新闻
def new_to_json(n):
    return {
        "id": n.id,
        "title": n.title,
        "author": n.author,
        "create_date": n.create_date.strftime('%Y-%m-%d'),
        "description": n.description,
        "text": n.text,
    }


def new_list(request):
    '''
    这是ajax请求，
    '''
    result = {}  # 是一个临时用的字典
    json_str = ""  # 返回的结果
    try:
        title = request.GET.get('title')  # 获取新闻
        # 如果没有，那么给默认值0，避免出错
        # categoryid = int(request.GET.get('categoryid', 0))  # 类别
        ##################
        # 显示第几页？
        pageindex = int(request.GET.get('pageindex', 1))  # 默认第一页开始
        pagesize = settings.pagesize  # 每页5条记录
        start = (pageindex - 1) * pagesize
        end = start + pagesize
        ##################
        news = models.New.objects.select_related('new').all().order_by("id")  # 获取全部 先不考虑查询条件

        # 注意，这里是动态查询，根据条件进行过滤
        if title:  # 如果有过滤
            # 相当于 where title like '% tite %' icontains不区分大小写
            news = news.filter(title__icontains=title)
        # if categoryid > 0:  # 如果选了过滤
        # 相当于 where category_id=2
        # books = news.filter(category_id=categoryid)
        # 需要求一个总页数
        recordcount = news.count()  # 获取总记录数
        pagecount = recordcount // pagesize if recordcount % pagesize == 0 else recordcount // pagesize + 1

        # 使用分页，切片
        news = news[start:end]
        news = list(news)  # QuerySet转成list集合
        result["success"] = 0  # 成功标记
        result["msg"] = "ok"  # 消息
        result["data"] = news  # 数据
        result["page"] = {  # 将和分页相关的内容页也返回给客户端
            "recordcount": recordcount,
            "pagecount": pagecount,
            "pageindex": pageindex
        }
        json_str = json.dumps(result, default=new_to_json)  # 指定序列化器
    except Exception as e:
        result["success"] = -1  # 失败了
        result["msg"] = "失败了,原因是%s" % e  # 消息
        result["data"] = None
        json_str = json.dumps(result)  # 序列化
    return HttpResponse(json_str)


# 修改密码 登录后才能修改
@authenticate
def userinfo_changepwd(request):
    result = {}
    print('已经到这里啦！', request.body)
    pwd1 = request.POST.get('pwd1')  # 旧密码
    pwd2 = request.POST.get('pwd2')  # 新密码
    # 验证，旧密码是否OK
    # 获取当前登录的用户对象
    user_obj = models.Users.objects.get(phone=request.session['username'])
    print('到这里啦！', user_obj)
    user_pwd = models.Users.objects.get(phone=request.session['username']).password
    print('原密码：', user_pwd)
    # 此方法验证密码是正确:
    if user_obj.password == pwd1:
        # 正确，那么修改密码
        print('输入的原密码正确！')
        print('新密码为：', pwd2)
        user_obj.password = pwd2
        user_obj.save()  # 更新保存
        result = {
            "success": 0,  #
            "msg": "OK"
        }
    else:
        result = {
            "success": -1,  #
            "msg": "原密码错误"
        }
    return HttpResponse(json.dumps(result))


# 个人收藏
def fav_to_json(b):
    return {
        "id": b.id,
        "title": b.title,
        # "img": b.img,
        "create_date": b.create_date.strftime('%Y-%m-%d'),
        "description": b.description,
        "category": {
            "id": b.category.id,
            "name": b.category.name,
        }
    }


# 我的关注新闻列表
@authenticate
def usernews_list(request):
    id=request.GET.get("id")

    result = {}  # 是一个临时用的字典
    json_str = None
    try:

        create_date = request.GET.get('create_date')
        print("create_date",create_date)
        ##################
        # 显示第几页？
        pageindex = int(request.GET.get('pageindex', 1))  # 默认第一页开始
        pagesize = 5  # 每页5条记录
        start = (pageindex - 1) * pagesize
        end = start + pagesize
        ##################
        user_obj = models.Users.objects.get(phone=request.session['username'])
        news = models.Users.objects.get(id=user_obj.id).news.all()  # 获取全部 先不考虑查询条件
        # news=list(news)
        # 注意，这里是动态查询，根据条件进行过滤
        if create_date:  # 如果有过滤
            # 相当于 where title like '% tite %' icontains不区分大小写
            news = news.filter(create_date__icontains=create_date)
            # 需要求一个总页数
        recordcount = news.count()  # 获取总记录数
        pagecount = recordcount // pagesize if recordcount % pagesize == 0 else recordcount // pagesize + 1

        # 使用分页，切片
        news = news[start:end]
        news = list(news)  # QuerySet转成list集合
        result["success"] = 0  # 成功标记
        result["msg"] = "ok"  # 消息
        result["data"] = news  # 数据
        result["page"] = {  # 将和分页相关的内容页也返回给客户端
            "recordcount": recordcount,
            "pagecount": pagecount,
            "pageindex": pageindex
        }
        json_str = json.dumps(result, default=fav_to_json)  # 指定序列化器
    except Exception as e:
        result["success"] = -1  # 失败了
        result["msg"] = "失败了,原因是%s" % e  # 消息
        result["data"] = None
        json_str = json.dumps(result)  # 序列化
    return HttpResponse(json_str)


# 我的关注新闻列表-删除
@authenticate
def usernews_delete(request):
    '''
        ajax请求，实现删除图书
        :param request:
        :return:
        '''
    id=request.GET.get("id") #获取要删除的图书   #RESTFUL风格请求

    result = {}
    json_str = None
    try:

        news = models.Users.objects.get(phone=request.session['username']).news.get(pk=id)
        news.delete()  # 删除
        result = {
            "success": 0,  # 成功标记
            "msg": "ok",
            "data": news,  # 表示已删除的对象
        }
        json_str = json.dumps(result, default=new_to_json)
    except Exception as e:
        result = {
            "success": -1,  # 成功标记
            "msg": "删除失败:%s" % e,
        }
        json_str = json.dumps(result)
    return HttpResponse(json_str)


# 我的评论列表
@authenticate
def comments_list(request):
    return None


# 我的评论列表-删除
@authenticate
def comments_delete(request):
    return None


# 我的评论列表-修改
@authenticate
def comments_change(request):
    return None
