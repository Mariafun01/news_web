from django.db import models

# Create your models here.
from django.utils import timezone

sex_choice = (
    (0, '男'),
    (1, '女'),
)


# 新闻类别
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='类别名称', null=True, unique=True)

    def __str__(self):
        return f'{self.id},{self.name}'

    class Meta:
        db_table = 'tbCategory'  # 用来生成数据的表名
        # admin工具里可以看到中文
        verbose_name = '新闻类别'  # 标签名
        verbose_name_plural = '新闻类别'  # 复数名称


# 新闻标签
class Lable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name='标签')

    class Meta:  # 元数据
        db_table = "tbLable"  # 映射到数据表的名字，默认，是应用_类名
        verbose_name = '新闻标签'
        verbose_name_plural = '新闻标签'

    def __str__(self):
        return f'{self.id},{self.name}'


# 新闻
class New(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, null=False, verbose_name='标题')
    author = models.CharField(max_length=50, verbose_name='作者', null=True)
    create_date = models.DateField(verbose_name='发布日期', null=True)
    description = models.CharField(max_length=2000, null=True, verbose_name='摘要')
    text = models.CharField(max_length=2000, null=True, verbose_name='正文')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='新闻类别')
    label = models.ManyToManyField(Lable, related_name="new_label",
                                   db_table='tbNewsLabels', verbose_name="新闻标签表")

    class Meta:  # 元数据
        db_table = "tb_News"  # 映射到数据表的名字，默认，是应用_类名
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __str__(self):
        return f'{self.id},{self.title},{self.author},' \
               f'{self.create_date.strftime("%Y-%m-%d")},{self.description},' \
               f'{self.text},{self.category},{self.label}'



# 用户
class Users(models.Model):
    '''
    用户类
    id自增
    仅手机号码和密码必填，注册过的用户都在这里，可用于登录和登录后关注收藏
    '''
    # 创建id属性，并设置自增长，主键约束
    id = models.AutoField(primary_key=True)
    # 姓名 verbose_name='姓名' 生成标签名称
    name = models.CharField(max_length=50, verbose_name='真实姓名', null=True)
    # unique 唯一不重复
    phone = models.CharField(max_length=11,
                             verbose_name='手机号码', unique=True)
    gender = models.IntegerField(verbose_name='性别', choices=sex_choice,default=0, null=True)
    birthday = models.DateField(verbose_name='出生年月', null=True)
    # null 数据库允许为空，默认是false
    # blank=True 表单允许为空
    province = models.CharField(max_length=100, null=True, blank=True, verbose_name='省份')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='城市')
    district = models.CharField(max_length=100, null=True, blank=True, verbose_name='区/县')
    id_card_number = models.CharField(max_length=18, verbose_name='身份证号码', null=True)
    email = models.CharField(max_length=50, null=True,
                             verbose_name='电子邮件')
    password = models.CharField(max_length=20, verbose_name='密码')
    state = models.IntegerField(verbose_name='状态', default=0)
    news = models.ManyToManyField(New, related_name="user_news",
                                  db_table='tbUserNews', verbose_name="收藏的新闻")


    # 增加一个内部类，用来描述元数据
    class Meta:
        db_table = 'users'  # 用来配置生成的数据表名
        # admin管理工具里，可以看到中文
        verbose_name = '用户'  # 标签名
        verbose_name_plural = '用户'  # 复数名称

    def __str__(self):
        # return f'{self.id}:{self.name}'
        return f'{self.id},{self.name},' \
               f'{self.phone},{self.password},{self.email},{self.gender},' \
               f'{self.birthday},{self.id_card_number},' \
               f'{self.province},{self.city},{self.district},{self.state},{self.news}'


# 新闻评论
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    text = models.CharField(max_length=1000, null=True, verbose_name='正文')
    createDate = models.DateTimeField(verbose_name="创建日期", null=True, default=timezone.now)
    new = models.ForeignKey(to=New, on_delete=models.PROTECT, verbose_name="所在新闻", null=True)
    createUser = models.ForeignKey(to=Users, on_delete=models.PROTECT, verbose_name="评论者", null=True)

    class Meta:  # 元数据
        db_table = "tbComments"  # 映射到数据表的名字，默认，是应用_类名
        verbose_name = '新闻评论'
        verbose_name_plural = '新闻评论'

    def __str__(self):
        return f'{self.id},{self.title},{self.text},' \
               f'{self.createDate},' \
               f',{self.new},{self.createUser}'


# 新闻图片名
class Fname(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, null=True, verbose_name='图片名')
    new = models.ForeignKey(to=New, on_delete=models.PROTECT, verbose_name='所属新闻', null=True)

    class Meta:  # 元数据
        db_table = "tbFname"  # 映射到数据表的名字，默认，是应用_类名
        verbose_name = '新闻图片名'
        verbose_name_plural = '新闻图片名'

    def __str__(self):
        return f'{self.id},{self.fname},{self.new}'
