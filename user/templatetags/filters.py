from django import template

register = template.Library()  # 创建对象，用来注册过滤器


@register.filter()  # 这是装饰器
# value这个值，就是传给你的原值
def gender(value):
    if value == 0:
        return '男'
    elif value == 1:
        return '女'
    else:
        return '保密'
