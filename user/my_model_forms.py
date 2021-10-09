from django import forms

from user import models
from django.forms import widgets as wid

'''
我们再form_models里，添加了一些class
 class Xxx(forms.Form):
    pass
 为啥要写，因为模板中有表单，为了实现 编写简便
 验证方便
 ===============
 实际中
   models.py --
      模型类，
      class Book  (model.Model):
         pass
      ...
    模型，业务模型，是和数据表进行关联
   form.From 是和表单关联，进行的抽象

   我们发现，有很多列都是重复的。这样就会冗余
   所以，可以根据model来扩展form
'''

#这个模型，是跟进Model来定义扩展的
#这里放的是和表单相关的一些验证信息
#以及额外的扩展字段 如重复密码，验证码
#以及生成html脚本信息的
class UserModelForm(forms.ModelForm):
    ##这里先定义下扩展字段，即Model里不存在的
    code=forms.CharField(
        label='验证码',
        error_messages={
            'required':'验证码必须输入'
        }
    )
    #功能：是对Model里的字段，在表单里出现
    #作出必要的设置，验证信息，生成的html脚本等
    class Meta:
        #指定，这是基于那个Model的扩展
        model=models.Users
        #指定允许哪些列可以扩展 全部
        #也可以指定部分 ('name','gender','mail')
        fields=('id','name','phone','gender','birthday','id_card_number','email','province','city','district') #model.__all__

        def __init__(self):
            pass

        ##统一设置widgets,html脚本外观
        widgets={
            'name':wid.TextInput(attrs={
                'class':'txt',
                "placeholder":'这里用户真实姓名'}
            ),
            'phone': wid.TextInput(attrs={
                'class': 'txt',
                "placeholder": '这里输入手机号码'}
            ),
            # 单选框组
            'gender':wid.RadioSelect(attrs={
                'class': 'choice',
                'placeholder' : '性别',
            }),
              # 设置默认值,下面的必填已经无效了
            # required=True,
            # error_messages={
            #   'required':'性别必选选择'
            # },
            # 默认 <select />
            'birthday': wid.TextInput(attrs={
                'class': 'txt',
                'type':'date',
                "placeholder": '这里输入出生年月'}
            ),
            'email': wid.TextInput(attrs={
                'class': 'txt',
                "placeholder": '这里输入电子邮件'}
            ),
            # 'address': wid.TextInput(attrs={
            #     'class': 'txt',
            #     "placeholder": '这里输入家庭地址'}
            # ),
            'id_card_number': wid.TextInput(attrs={
                'class': 'txt',
                "placeholder": '这里输入身份证号码'}
            ),
            # 'province': forms.Select(),
            'province':wid.Select(attrs={
                'class':'txt',
            }),
            'city': forms.Select(),
            'district': forms.Select()
        }
        ##统一设置验证提示
        error_messages={
            'name':{
                'required':'姓名必须输入',
            },
            'phone':{
                'required': '手机号码必须输入',
                'invalid': '手机号码格式不正确',
                'min_length': '手机号码必须为11位',
                'max_length': '手机号码必须为11位',
            },
            'id_card_number':{
                'required': '身份证号码码必须输入',
                'invalid': '身份证号码格式不正确',
                'min_length': '身份证号码必须为18位',
                'max_length': '身份证号码必须为18位',
            },
            'address': {
                'required': '地址必须输入',
            }
        }

    #全局钩子函数,实现其他列的验证
    # def clean(self):
    #     phone=self.cleaned_data.get('phone')
    #     ret=models.Users.objects.filter(phone=phone).exists()
    #
    #     if ret:
    #         self.add_error('phone', '手机号码已存在，不能注册')
    #
    #     email = self.cleaned_data.get('email')
    #     #为啥加判断，因为数据表里，这个列是允许为空
    #     if email!=None:
    #         ret = models.Users.objects.filter(email=email).exists()
    #         if ret:
    #             self.add_error('email', '电子邮件已存在，不能注册')
    #
    #     pass


# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     form = MemberForm
#     fields = ('name', ('province', 'city', 'district'))
#     list_display = ('name', 'province', 'city', 'district')
#     change_form_template = 'area.html'
