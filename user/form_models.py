from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import widgets as wid

from user import models
from user.my_vailator import check_phone


class LoginFormModel(forms.Form):
    userCode = forms.CharField(
        label='手机号码',  # 标签
        required=True,  # 必填验证器
        min_length=11,
        max_length=11,
        validators=[
            RegexValidator(r'^1[3-9]\d{9}$'),  # 正则表达式校验器
        ],
        # 这是验证错误,
        error_messages={
            # key叫做验证器
            'required': '手机号码不能为空',
            'min_length': '手机号码必须为11位',
            'max_length': '手机号码必须为11位',
            'invalid': '手机号码格式不正确'
        },
        # 用来生成对应的html元素，默认就是TextInput
        # 这里会自动生成html,attrs属性就是对应了客户端html属性
        # <input type='text' class='txt' placeholder='手机/邮箱/昵称'/>
        widget=wid.TextInput(attrs={"class": 'txt',
                                    "placeholder": '手机号码'})
    )

    userPassword = forms.CharField(
        label='密码',  # 标签
        required=True,  # 必填验证器
        min_length=5,  # 最小长度
        # 这是验证错误,
        error_messages={
            # key叫做验证器
            'required': '密码不能为空',
            'min_length': '密码长度至少5位以上'
        },
        widget=wid.PasswordInput(attrs={"class": 'txt',
                                        "placeholder": '字母数字下划线'})
    )


class RegisterFormModel(forms.Form):
    userCode = forms.CharField(
        label='手机号码',  # 标签
        required=True,  # 必填验证器
        min_length=11,
        max_length=11,
        # 用来生成对应的html元素，默认就是TextInput
        # 这里会自动生成html,attrs属性就是对应了客户端html属性
        # <input type='text' class='txt' placeholder='手机/邮箱/昵称'/>
        widget=wid.TextInput(attrs={"class": 'txt',
                                    "placeholder": '手机号码'}),
        # 校验器
        validators=[
            check_phone,  # 自定义校验器手机号是否唯一
            RegexValidator(r'^1[3-9]\d{9}$'),  # 正则表达式校验器
        ],
        error_messages={
            # key叫做验证器
            'required': '手机号码不能为空',
            'min_length': '手机号码必须为11位',
            'max_length': '手机号码必须为11位',
            'invalid': '手机号码格式不正确'  # 针对的是validators
        },
    )

    userPassword = forms.CharField(
        label='密码',  # 标签
        required=True,  # 必填验证器
        min_length=5,  # 最小长度
        # 这是验证错误,
        error_messages={
            # key叫做验证器
            'required': '密码不能为空',
            'min_length': '密码长度至少5位以上'
        },
        widget=wid.PasswordInput(attrs={"class": 'txt',
                                        "placeholder": '字母数字下划线'})

    )

    userPassword2 = forms.CharField(
        label='重复密码',  # 标签
        widget=wid.PasswordInput(attrs={"class": 'txt',
                                        "placeholder": '字母数字下划线'})
    )

    def clean_userPassword2(self):
        # 局部钩子，验证重复密码
        pwd1 = self.cleaned_data.get('userPassword')  # 提取密码
        pwd2 = self.cleaned_data.get('userPassword2')  # 重复密码
        # print(pwd1,pwd2)
        if pwd1 != pwd2:
            # 两个密码不一致，那么，就是错误了
            # raise ValidationError('重复密码和密码不一致')
            self.add_error('userPassword2', '重复密码和密码不一致')

