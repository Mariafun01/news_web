from django.contrib import admin
#
# # Register your models here.
# #这里是注册模型，为了让admin管理工具进行管理
from user import models

#
# admin.site.register(models.Users)
# admin.site.register(models.New)
admin.site.register(models.Category)
admin.site.register(models.Lable)
admin.site.register(models.Comments)
admin.site.register(models.Fname)


class Def_User(admin.ModelAdmin):
    '''
    编写此类的目的，是为了让User这个模型，自定义列表
    '''
    list_display = ('id', 'name', 'phone', 'gender', 'birthday', 'province',
                    'city', 'district', 'id_card_number', 'email', 'state')  #


# 别忘了，注册下Teacher
admin.site.register(models.Users, Def_User)
#
class Def_New(admin.ModelAdmin):
    #序号,学生姓名，科目，考试成绩
    list_display = ('id','title','author', 'create_date','description','text','category')
    #
    # def get_student_name(self,obj):
    #     return obj.student.name

    # get_student_name.short_description='考生姓名'

    # def get_course_name(self,obj):
    #     return obj.course.cname
    #
    # get_course_name.short_description='考试科目'
#注册
admin.site.register(models.New,Def_New)
#
# class Def_Teacher(admin.ModelAdmin):
#     '''
#     编写此类的目的，是为了让Teacher这个模型，自定义列表
#     '''
#     list_display = ('tno','name','phone','address','prof','salary') # 定制表格
#     #############
#     search_fields = ('name','phone','address') #元组，定制搜索栏
#
#
# class Def_Teacher(admin.ModelAdmin):
#     '''
#     编写此类的目的，是为了让Teacher这个模型，自定义列表
#     '''
#     list_display = ('tno','name','phone','address','prof','salary') # 定制表格
#     #############
#     search_fields = ('name','phone','address') #元组，定制搜索栏
#     ############
#     list_display_links = ('tno','phone') #允许被链接
#
#
# class Def_Score(admin.ModelAdmin):
#     #序号,学生姓名，科目，考试成绩
#     list_display = ('id','get_student_name','get_course_name', 'degree')
#
#     list_per_page = 10 #分页尺寸，即每页10条记录
#
# list_editable = ('name', 'phone','address', 'prof', 'salary')
# list_filter = ('prof',)  # 过滤条件
#
# #自定义表单
# fieldsets = (
#     ['基础信息',{'fields':('tno','name','phone')}],
#     ['高级信息',{
#         'classes':('collapse',),#css
#         'fields':('prof','salary','address')
#              }
#      ]
# )
