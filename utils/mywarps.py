'''
这个模块中，放的是一些工程中需要用到的装饰器
'''
import functools

from django.http import HttpResponse
from django.urls import reverse

from user import models
from user.form_models import LoginFormModel


def authenticate(fn_view):
    '''
    自定义装饰器，用来装饰view，实现身份验证
    :param fn_view:
    :return:
    '''

    @functools.wraps(fn_view)
    def auth(*args, **kwargs):
        # 这个url列表，表示，哪些请求是需要授权访问
        url_list = [
            # 用户中心
            reverse('user:logout'),
            # 个人中心
            reverse('user:main'),
            # 更改密码
            reverse('user:api_userinfo_changepwd'),
            # 个人信息展示
            reverse('user:api_userinfo'),
            # 个人信息修改
            reverse('user:api_userinfo_change'),
            # 收藏新闻列表
            reverse('user:api_usernews_list'),
            # 收藏新闻删除
            reverse('user:api_usernews_delete'),
            # reverse('user:favnews'),
            # reverse('user:comments'),
            # 新闻
            reverse('news:upload_comment'),
            # reverse('news:updateusernews'),
            # reverse('upload_comment'),
        ]

        request = args[0]  # 获取目标view的request请求对象
        session = request.session
        next_url = request.path.lower()  # 获取当前的请求url
        print(next_url)
        # 如果这个请求，在受限名单中
        if next_url in url_list:
            # 那么验证是否已经登陆了
            username = session.get("username", None)
            print("username", username)
            if username == None:
                # 重定向到登录页面

                login_url = reverse("user:login")
                # 这里将当前访问的页面，通过get传参方式，传递给登录页
                js = f"<script>alert('必须登录后才能访问');" \
                     f"location.href='{login_url}?returnurl={next_url}';</script>"
                return HttpResponse(js)
            # 如果正常，那么最后调用目标view
            return fn_view(*args, **kwargs)

    return auth


def authenticate_id(fn_view):
    '''
    自定义装饰器，用来装饰view，实现身份验证
    :param fn_view:
    :return:
    '''

    @functools.wraps(fn_view)
    def auth(*args, **kwargs):
        # 这个url列表，表示，哪些请求是需要授权访问
        id = kwargs['id']
        url_list = [
            reverse('user:userinfo', kwargs={'id': id}),
            reverse('user:userinfo_change', kwargs={'id': id}),
            reverse('user:userinfo_pwdchange', kwargs={'id': id}),
            reverse('user:favnews', kwargs={'id': id}),
            reverse('user:comments', kwargs={'id': id}),
        ]

        request = args[0]  # 获取目标view的request请求对象

        session = request.session
        # session['id']=request.session
        next_url = request.path.lower()  # 获取当前的请求url
        print(next_url)
        # 如果这个请求，在受限名单中
        if next_url in url_list:
            # 那么验证是否已经登陆了
            username = session.get("username", None)
            print("username", username)
            if username == None:
                # 重定向到登录页面

                login_url = reverse("user:login")
                # 这里将当前访问的页面，通过get传参方式，传递给登录页
                js = f"<script>alert('必须登录后才能访问');" \
                     f"location.href='{login_url}?returnurl={next_url}';</script>"
                return HttpResponse(js)
            # 如果正常，那么最后调用目标view
            return fn_view(*args, **kwargs)

    return auth
