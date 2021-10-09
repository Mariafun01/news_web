import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "news_web.settings")
django.setup()
from user import models
#新闻类别
# models.Category.objects.create(name='新闻资讯')
# models.Category.objects.create(name='社会热点')
# models.Category.objects.create(name='财经频道')
# models.Category.objects.create(name='地产频道')
# models.Category.objects.create(name='历史文化')
# models.Category.objects.create(name='人物专栏')
# models.Category.objects.create(name='城市观察')
# models.Category.objects.create(name='前沿资讯')

#新闻标签
# models.Lable.objects.create(name='母亲')
# models.Lable.objects.create(name='女性')
# models.Lable.objects.create(name='疫情')
# models.Lable.objects.create(name='房地产')
# models.Lable.objects.create(name='保险')
# models.Lable.objects.create(name='营销')
# models.Lable.objects.create(name='娱乐圈')
# models.Lable.objects.create(name='离婚')
# models.Lable.objects.create(name='工作')
# models.Lable.objects.create(name='进出口')
# models.Lable.objects.create(name='年轻人')

# 新闻
# models.New.objects.create(title='占领品质制高点，本土品牌安婕妤以“功效护肤”实现市场再扩容',
#                           author='汤婉月',create_date='2021-07-01',
#                           description='随着国货复兴热潮席卷，国内功能护肤的高端市场已然有新兴力量诞生，不再被进口垄断。'
#                                       '同时，消费新势力也从中崛起，他们有更高的自主消费能力、更多元化的消费需求、更超前的消费观念，且拥有更强的民族自豪感和文化认同度。',
#                           text='随着国货复兴热潮席卷，国内功能护肤的高端市场已然有新兴力量诞生，不再被进口垄断。'
#                                '同时，消费新势力也从中崛起，他们有更高的自主消费能力、更多元化的消费需求、更超前的消费观念，且拥有更强的民族自豪感和文化认同度。',
#                           category_id=8)
# models.New.objects.create(title='困境突围！疫情以来最大规模中新贸易盛会在新西兰奥克兰盛大举行',
#                           author='《华尔街日报》',create_date='2021-07-05',
#                           description='在新冠疫情新西兰全国的封锁期间，小马哥带领团队，从容应对消费市场的变化，'
#                                       '将工作重心放在倾听消费者的实际需求上，不但帮助更多中国消费者解决细胞健康的相关问题，'
#                                       '也带领企业迈上新台阶。论坛当天，他的演说获得了在场宾客们的阵阵掌声。',
#                           text='在新冠疫情新西兰全国的封锁期间，小马哥带领团队，从容应对消费市场的变化，'
#                                       '将工作重心放在倾听消费者的实际需求上，不但帮助更多中国消费者解决细胞健康的相关问题，'
#                                       '也带领企业迈上新台阶。论坛当天，他的演说获得了在场宾客们的阵阵掌声。',
#                           category_id=8)
# models.New.objects.create(title='金科实控人离婚后续：只剩利益和狗血剧情',
#                           author='刘碎平',create_date='2021-07-10',
#                           description='离婚4年后，前妻陶虹遐以一种决绝的态度，站在前夫黄红云，也是重庆本土开发商、TOP20房企金科股份实控人的对立面。',
#                           text='离婚4年后，前妻陶虹遐以一种决绝的态度，站在前夫黄红云，也是重庆本土开发商、TOP20房企金科股份实控人的对立面。',
#                           category_id=4)
# models.New.objects.create(title='占领品质制高点，本土品牌安婕妤以“功效护肤”实现市场再扩容',
#                           author='汤婉月',create_date='2021-07-01',
#                           description='随着国货复兴热潮席卷，国内功能护肤的高端市场已然有新兴力量诞生，不再被进口垄断。'
#                                       '同时，消费新势力也从中崛起，他们有更高的自主消费能力、更多元化的消费需求、更超前的消费观念，且拥有更强的民族自豪感和文化认同度。',
#                           text='随着国货复兴热潮席卷，国内功能护肤的高端市场已然有新兴力量诞生，不再被进口垄断。'
#                                '同时，消费新势力也从中崛起，他们有更高的自主消费能力、更多元化的消费需求、更超前的消费观念，且拥有更强的民族自豪感和文化认同度。',
#                           category_id=8)
# models.New.objects.create(title='为更多婚假，台湾夫妇37天内结婚四次',
#                           author='《纽约时报》',create_date='2021-05-25',
#                           description='为更多婚假，台湾夫妇37天内结婚四次',
#                           text='为更多婚假，台湾夫妇37天内结婚四次',
#                           category_id=1)
# models.New.objects.create(title='2021国际布克奖短名单公布',
#                           author='《新京报书评周刊》',create_date='2021-05-25',
#                           description='从玛丽亚·斯捷潘诺娃的家庭回忆录到埃里克·维亚尔的历史随笔，今年的国际布克奖短名单，突出了那些“真正突破了”虚构与非虚构界限的作品。',
#                           text='出版过英文书籍，不过他们在自己的国家受到好评。“每一本书都在做一些新的事情，”休斯·哈雷特说，“但是，这并不意味着他们不平易近人、不容易享受。”',
#                           category_id=2)

#添加用户信息
# models.Users.objects.create(name='张三',phone=13021132453,
#                             password='zhangsan123',email='zhangsan@163.com',
#                             gender=0,birthday='1995-9-28',
#                             id_card_number=130722199508184563,
#                             province='河北省',
#                             city='石家庄市',
#                             district='某某区',
#                             state=0)
# models.Users.objects.create(name='李四',phone=13021132456,
#                             password='lisi123',email='lisi@163.com',
#                             gender=0,birthday='1998-10-18',
#                             id_card_number=130722199508184566,
#                             province = '河南省',
#                             city = '洛阳市',
#                             district = '某某区',
#                             state = 0)
#
# models.Users.objects.create(name='王五',phone=13021132454,
#                             password='wangwu123',email='wangwu@163.com',
#                             gender=1,birthday='1994-6-2',
#                             id_card_number=130722199508184564,
#                             province='云南省',
#                             city='普洱市',
#                             district='某某区',
#                             state=1)
# models.Users.objects.create(name='赵六',phone=13021132455,
#                             password='zhaoliu123',email='zhaoliu@163.com',
#                             gender=1,birthday='1999-11-8',
#                             id_card_number=130722199508184565,
#                             province='上海',
#                             city='上海市',
#                             district='某某区',
#                             state=0)
#
#评论

# models.Comments.objects.create(title='沙发',text='还能有谁比我快，还有谁？！',new_id=2,createUser_id=2)
# models.Comments.objects.create(title='国货外岁！',text='楼上的只有快，评论要有深度！',new_id=2,createUser_id=3)
# models.Comments.objects.create(title='赞同楼上！',text='一楼说话小心点，我法外狂徒怕过谁！',new_id=2,createUser_id=1)
# models.Comments.objects.create(title='沙发',text='还能有谁比我快，还有谁？！',new_id=6,createUser_id=2)
# models.Comments.objects.create(title='怎么又是楼上的**！',text='楼上的只有快，评论要有深度！',new_id=6,createUser_id=3)

#图片名
# models.Fname.objects.create(fname='占领品质制高点，本土品牌安婕妤以“功效护肤”实现市场再扩容.jpg',new_id=2,)
# models.Fname.objects.create(fname='为更多婚假，台湾夫妇37天内结婚四次.jpg',new_id=6,)

##这里初始化下，多对多关系，用户收藏新闻
# user1=models.1#收藏新闻编号1
# user1.news.add(models.New.objects.get(id=2)) #收藏新闻编号2
# user1.news.add(models.New.objects.get(id=3)) #收藏新闻编号3
# user2=models.Users.objects.get(id=2)
# user2.news.add(models.New.objects.get(id=2)) #收藏新闻编号2
# user2.news.add(models.New.objects.get(id=3)) #收藏新闻编号3
# user2.news.add(models.New.objects.get(id=4)) #收藏新闻编号4
##这里初始化下，多对多关系，新闻添加标签
new1=models.New.objects.get(id=1)#收藏新闻编号1
new1.label.add(models.Lable.objects.get(id=2)) #收藏新闻编号2
new1.label.add(models.Lable.objects.get(id=3)) #收藏新闻编号3
new2=models.Users.objects.get(id=2)
new2.label.add(models.Lable.objects.get(id=2)) #收藏新闻编号2
new2.label.add(models.Lable.objects.get(id=6)) #收藏新闻编号3
new2.label.add(models.Lable.objects.get(id=4)) #收藏新闻编号4
########################
# ##对多对多的新闻发起查询
# #显示某个用户收藏的新闻列表 用户1的收藏新闻列表
# user1=models.Users.objects.get(pk=1)
# # 就表示用户收藏的图书
# news=user1.news.all()
# for n in news:
#     print(n.id,n.title,n.author,n.description)
#
# # ## 反向查询，一本书被哪些用户收藏
# new=models.Users.objects.get(pk=1)
# print(new.title,'被哪些用户收藏？')
# #related_name='user_books',#关系名字
# for n in new.user_news.all():
#     print(n.name,n.phone)
