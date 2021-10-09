from django.contrib import admin
from django.urls import path

from user import views, api_views
from user.api.user_cbv import UserView

app_name='user'


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    # 注册
    path('register/',views.register,name='register'),
    # 登录
    path('login/', views.login, name='login'),
    # 退出登录
    path('logout/',views.logout,name='logout'),
    # 个人中心主页
    path('main/', views.main, name='main'),
    path('main/userinfo/<int:id>', views.userinfo, name='userinfo'),
    path('main/userinfo_change/<int:id>', views.userinfo_change, name='userinfo_change'),
    path('main/userinfo_pwdchange/<int:id>', views.userinfo_pwdchange, name='userinfo_pwdchange'),
    path('main/favnews/<int:id>', views.favnews, name='favnews'),
    path('main/comments/<int:id>', views.comments, name='comments'),

    # RESTFUL风格
    # 获取用户信息
    path('api/userinfo/', api_views.userinfo, name='api_userinfo'),
    # 更新用户信息
    path('api/userinfo/change/', api_views.userinfo_change, name='api_userinfo_change'),
    # 修改密码
    path('api/userinfo/changepwd/', api_views.userinfo_changepwd, name='api_userinfo_changepwd'),
    # 我的关注列表
    path('api/usernews/list/', api_views.usernews_list, name='api_usernews_list'),
    path('api/usernews/delete/', api_views.usernews_delete, name='api_usernews_delete'),

    # 我的评论列表
    path('api/comments/list', api_views.comments_list, name='comments_list'),
    path('api/comments/delete/', api_views.comments_delete, name='comments_delete'),
    path('api/comments/change/', api_views.comments_change, name='comments_change'),

    # restful 风格
    # 多个用户
    path('api_a/userinfo/', UserView.as_view()),
    # 单个用户
    path('api_a/userinfo/<int:id>/', UserView.as_view()),

]