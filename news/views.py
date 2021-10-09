from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 首页
from django.urls import reverse

from user import models
from news.dao.newdao import NewDao, CategoryDao, UserNewsDao, UserDao
from user.models import New
from utils.mywarps import authenticate
from utils.webtools import alertAndRedirect


def index(request):
    session=request.session
    username = session.get("username", None)
    user=models.Users.objects.filter(phone=username)

    userdao = UserDao()
    users = userdao.get_list()
    # print(session)
    print(username,users)
    newdao = NewDao()  # 创建数据访问对象
    news = newdao.get_list()  # 获取新闻列表
    categorydao = CategoryDao()  # 创建数据访问对象
    categorys = categorydao.get_list()  # 获取新闻列表

    return render(request, 'news/index.html',locals())


# 新闻列表
def newslist(request,id):
    session = request.session
    username = session.get("username", None)
    user=models.Users.objects.filter(phone=username)

    categorydao = CategoryDao()  # 创建数据访问对象
    categorys = categorydao.get_list()  # 获取新闻列表
    # 根据category的id获取所属类别的新闻？
    # 多类类名.objects.filter(多类中的关联属性__id=值)
    news=models.New.objects.filter(category_id=id)
    # pageindex = int(request.GET.get("pageindex", "1"))
    # pagesize = settings.pagesize  # 每页5要
    # start = (pageindex - 1) * pagesize
    # end = pageindex * pagesize
    return render(request, 'news/newslist.html',locals())


# 新闻详情
def newsdetail(request):
    return render(request, 'news/newsdetail.html')


def news(request, id):
    session = request.session
    username = session.get("username", None)

    # 获取当前id对应的新闻
    new = models.New.objects.filter(pk=id)

    # 获取当前用户
    user = models.Users.objects.get(phone=username)

    # 收藏状态查询：根据用户id查询新闻ID，确定新闻是否被当前用户收藏 多查多
    # 获取当前用户收藏的所有新闻
    ret = models.Users.objects.get(phone=request.session['username'])\
        .news.filter(id=id).exists()
    # 查询当前新闻是否在当前用户收藏的新闻里，得到的是true或false

    # 根据新闻的id查询所属的新闻类别 多查一
    # 一类类名.objects.filter(多类类名小写__id=1)
    category = models.Category.objects.filter(new__id=id)

    # 根据新闻id查询相关的评论，一查多
    # 多类类名.objects.filter(多类中的关联属性__id=值)
    comments=models.Comments.objects.filter(new__id=id)

    # 根据当前新闻的id查询对应标签的name 多查多
    labels = models.Lable.objects.filter()
    label_ret=models.New.objects.get(id=id).label.all().exists()

    return render(request, 'news/news.html',locals())


@authenticate
def upload_comment(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    get_news_id = request.POST.get('id')

    user = models.Users.objects.get(phone=request.session['username'])
    get_user_id = user.id
    models.Comments.objects.create(title=title, text=text,
                                   new_id=get_news_id,
                                   createUser_id=get_user_id)
    id = get_news_id
    news_url = reverse('news:news',kwargs={'id':id})
    js = alertAndRedirect('评论成功啦！', news_url)
    return HttpResponse(js)