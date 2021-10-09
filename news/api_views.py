# 此处用于处理用户新闻收藏
import json

from django.http import HttpResponse

from news.dao.newdao import NewDao
from utils.mywarps import authenticate



def api_fav(request,id):
    uid=1
    dao=NewDao()
    ret=dao.fav_save(id,uid)
    result = {
        "success": 0,  # 成功标记
        "msg": "ok",
        "data": ret,  # 1表示收藏成功 0表示移除收藏
    }
    json_str = json.dumps(result)
    return HttpResponse(json_str)
