
def alertAndRedirect(msg,url):
    '''
    实现js弹框并跳转
    :param msg: 消息提示
    :param url: 要跳转的网址
    :return: js脚本
    '''
    #格式化下
    msg=msg.replace("'",'').replace('"','')\
        .replace("\r","").replace("\n","")
    js=f'<script>alert("{msg}");location.href="{url}";</script>'
    return js

def alertAndBack(msg):
    '''
    实现js弹框并后退一步
    :param msg: 消息提示
    :return: js脚本
    '''
    #格式化下
    msg=msg.replace("'",'').replace('"','')\
        .replace("\r","").replace("\n","")
    js=f'<script>alert("{msg}");history.go(-1);</script>'
    return js

