from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 会员注册
from django.urls import reverse

from user import models
from news.dao.newdao import NewDao
from user.form_models import LoginFormModel, RegisterFormModel
from utils.mywarps import authenticate, authenticate_id

# 登录
from utils.webtools import alertAndRedirect, alertAndBack


# 这里处理表单post提交上来，处理登陆
def login(request):
    # session = request.session
    # username = session['username']
    # user = models.Users.objects.filter(phone=request.session['username'])
    # print(user[0])
    # next_url = request.path.lower()  # 获取当前的请求url
    # print(next_url)
    global id
    if request.method == 'GET':
        form_model = LoginFormModel()  # 创建form对象
        return render(request, 'user/login.html', locals())
    else:
        # 这里进入的登录判断逻辑，post提交
        # 自动从request.POST中去获取 name="username"...
        # 并创建对象，依次赋值
        form_model = LoginFormModel(request.POST)  # 创建form对象

        if form_model.is_valid():
            # 如果为真，表示服务端校验通过
            # 开始进行检测用户名和密码是否正确
            data = form_model.cleaned_data  # 获取干净的数据
            ret = models.Users.objects.filter(phone=data.get('userCode')
                                              , password=data.get('userPassword')).exists()
            # uid=models.Users.objects.filter(id=data.get('user_id'))
            # print(uid)
            if ret:
                session = request.session
                session["username"] = data.get('userCode')
                username = session['username']

                # session['id']=uid
                # print(session['id'])
                url_next = reverse('news:index', )  # args={'id':id}
                return redirect(url_next)  # 此处跳转页面有待优化
            else:
                msg = "用户名或密码错"
                return render(request, 'user/login.html', locals())
        else:
            msg = "你提交的信息不正确，请改进"
            return render(request, 'user/login.html', locals())


def register(request):
    # return render(request,'user/register.html')
    form_model = RegisterFormModel(request.POST)  # 创建form对象
    if form_model.is_valid():
        # 如果为真，表示服务端校验通过
        # 开始进行检测用户名和密码是否正确
        data = form_model.cleaned_data  # 获取干净的数据
        js = ''
        try:
            # 创建用户
            name = data.get('userCode')
            password = data.get('userPassword')
            password2 = data.get('userPassword2')
            print(f'用户名:{name},密码:{password}')

            models.Users.objects.create(phone=name, password=password)
            login_url = reverse('user:login')
            js = alertAndRedirect('注册成功，赶快去登录吧', login_url)
        except Exception as e:
            js = alertAndBack(f'注册失败:{e}')
        finally:
            return HttpResponse(js)

    else:
        msg = "你提交的信息不正确，请改进"
        return render(request, 'user/register.html', locals())


# 会员中心
@authenticate
def main(request):
    session = request.session
    username = session['username']
    user=models.Users.objects.filter(phone=username)
    id=request.GET.get('id')
    print('main',username)
    return render(request, 'user/main.html', locals())


# def check_phone(request):
#     phone = request.GET.get("phone")  # 获取传入的phone
#     ret = models.Users.objects.filter(phone=phone).exists()
#     if ret:
#         # 存在，不能注册
#         json = '{"success":-1}'
#     else:
#         json = '{"success":0}'
#     response = HttpResponse(json)
#     # 允许跨域
#     response.headers['Access-Control-Allow-Origin'] = "*"
#     # response[“Access - Control - Allow - Origin”] = “ * ”
#     # response[“Access - Control - Allow - Methods”] = “POST, GET, OPTIONS”
#     # response[“Access - Control - Max - Age”] = “1000”
#     # response[“Access - Control - Allow - Headers”] = “ * ”
#     return respons

# @login_required
# @authenticate
def logout(request):
    # logout(request)  # 当前请求的session全部清除，clear;
    # 重定向到登录页面
    session = request.session
    session["username"] = request.session.get('userCode')
    del session["username"]  # 删除登录标志
    # url = reverse('user:login')
    # return redirect(url)
    return redirect(reverse('user:login'))


def newlist(request):
    # 新闻列表
    newdao = NewDao()  # 创建数据访问对象
    news = newdao.get_list()  # 获取新闻列表
    # new=models.New.objects.filter(pk=id)
    # for c in new.category_id.all():
    #     category=c.name

    return render(request, 'user/new/list.html', locals())


def hello(request):
    return HttpResponse('hello')


@authenticate_id
def userinfo(request,id):
    session = request.session
    username = session['username']  # 此处是为在页面上显示username
    # uid=request.SESSIONS.get('id')
    user = models.Users.objects.filter(phone=request.session['username'])  # 获取用户
    # 此处是为在页面上循环出user的ID
    print('userinfo',id,)
    return render(request, 'user/userinfo.html', locals())


@authenticate_id
def userinfo_change(request,id):
    session = request.session
    username = session['username']
    user = models.Users.objects.filter(phone=request.session['username'])  # 获取用户

    print('userinfo_change', id)
    return render(request, 'user/userinfo_change.html', locals())


@authenticate_id
def userinfo_pwdchange(request,id):
    session = request.session
    username = session['username']
    user = models.Users.objects.filter(phone=request.session['username'])  # 获取用户

    print('userinfo_pwdchange', id)
    return render(request, 'user/userinfo_pwdchange.html', locals())


@authenticate_id
def favnews(request,id):
    session = request.session
    username = session['username']
    user = models.Users.objects.filter(phone=request.session['username'])  # 获取用户
    news = models.Users.objects.get(phone=request.session['username']).news.all()
    print(news)
    print('favnews', id)
    return render(request, 'user/favnews.html', locals())


@authenticate_id
def comments(request,id):
    session = request.session
    username = session['username']
    user = models.Users.objects.filter(phone=request.session['username'])  # 获取用户
    print('comments', id)
    return render(request, 'user/comments.html', locals())
