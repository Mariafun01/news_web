'''
这里放的是，自动定义校验器

'''
from django.core.exceptions import ValidationError

from user import models


def check_phone(value):
    '''
    用来判断手机号码是否唯一不重复
    :param value:  传入的手机号码
    :return:
    '''
    ret=models.Users.objects.filter(phone=value).exists()
    if ret:
        #存在，那么不能注册，就是验证失败，就是抛出以一个异常
        raise  ValidationError('手机号码已存在，不能注册')
