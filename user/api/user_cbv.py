from datetime import datetime
import json
from decimal import Decimal

from django.http import HttpResponse
from django.views import View

from user import models


class UserView(View):

    def dispatch(self, request, *args, **kwargs):
        # 分发之前预处理
        # print(request.method)
        # pass
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        ##做两件事情 如果存在id 查单个，否则查列表
        if id > 0:
            return self.single(request, id)
        else:
            return self.list(request)

    # 添加、新增
    def post(self, request):
        # loads方法，将一个json格式字符串转成dict
        data = json.loads(request.body)
        result = {}
        try:
            id = data.get('id', 0)
            name = data.get('name', '')
            phone = data.get('phone', '')
            gender = data.get('gender', 0)
            birthday = data.get('birthday', '')
            province = data.get('province', '')
            city = data.get('city', '')
            district = data.get('district', '')
            id_card_number = data.get('id_card_number', '')
            email = data.get('email', '')
            password=data.get('password','')
            state=data.get('state',0)
            news=data.get('news','')
            record = models.Users.objects.create(users_id=id,
                                                 users_name=name,
                                                 users_phone=phone,
                                                 users_gender=gender,
                                                 users_birthday=birthday,
                                                 users_province=province,
                                                 users_city=city,
                                                 users_district=district,
                                                 users_id_card_number=id_card_number,
                                                 users_email=email,
                                                 users_password=password,
                                                 users_state=state,
                                                 users_news=news,
                                                 )
            # print(record)
            result["success"] = 0
            result["msg"] = "OK"
            # 构造下，发给前端的数据
            result["data"] = record.id  # 成功后返回自增长的主键字段
        except Exception as e:
            result["success"] = -1
            result["msg"] = str(e)

        json_str = json.dumps(result)  # 序列化json
        return HttpResponse(json_str)

    # 更新
    def put(self, request):
        # loads方法，将一个json格式字符串转成dict
        data = json.loads(request.body)
        result = {}
        try:
            id = data.get('id', 0)
            name = data.get('name', '')
            phone = data.get('phone', '')
            gender = data.get('gender', 0)
            birthday = data.get('birthday', '')
            province = data.get('province', '')
            city = data.get('city', '')
            district = data.get('district', '')
            id_card_number = data.get('id_card_number', '')
            email = data.get('email', '')
            password = data.get('password', '')
            state = data.get('state', 0)
            news = data.get('news', '')
            if id == 0:
                result["success"] = -2
                result['msg'] = '未提供id'
            else:
                record = models.Users.objects.get(pk=id)
                record.name = name
                record.phone = phone
                record.gender = gender
                record.birthday = birthday
                record.province = province
                record.city = city
                record.district = district
                record.id_card_number = id_card_number
                record.email = email
                record.password = password
                record.state = state
                record.news = news
                # 更新成绩
                record.save()  # 更新
                result["success"] = 0
                result["msg"] = "OK"
                # 构造下，发给前端的数据
                result["data"] = id
        except Exception as e:
            result["success"] = -1
            result["msg"] = str(e)

        json_str = json.dumps(result)  # 序列化json
        return HttpResponse(json_str)

    # 删除
    def delete(self, request, id=0):
        result = {}
        try:
            record = models.Users.objects.get(pk=id)

            record.delete()  # 删除
            result["success"] = 0
            result["msg"] = "OK"
            result["data"] = id  # 成功data放的是删除的编号
        except Exception as e:
            result["success"] = -1

            result["msg"] = str(e)

        json_str = json.dumps(result)  # 序列化json
        return HttpResponse(json_str)

    # 查多个
    def list(self, request):
        id = request.GET.get("id", "-1")
        cno = request.GET.get("cno", "-1")
        query_para = {}  # 查询条件字典
        # 根据传递值，构造查询条件字典
        if id != '-1':
            # 字符串，模糊匹配
            query_para["users_id"] = id
        if cno != '-1':
            query_para["new_id"] = id
        result = {}
        try:
            scores = models.Users.objects. \
                select_related("name").select_related("course") \
                .filter(**query_para) \
                .values("id", "student__name", "course__cname", "degree", 'create_date') \
                .order_by("id")
            scores = list(scores)
            result["success"] = 0
            result["msg"] = "OK"
            result["data"] = scores
        except Exception as e:
            result["success"] = -1
            result["msg"] = str(e)

        json_str = json.dumps(result, default=self.score_to_json)  # 序列化json
        return HttpResponse(json_str)
        return HttpResponse('我是get请求')

    # 查单个
    def single(self, request, id):
        result = {}
        try:
            record = models.Score.objects. \
                select_related("student"). \
                select_related("course").get(pk=id)
            result["success"] = 0
            result["msg"] = "OK"
            # 构造下，发给前端的数据
            result["data"] = {
                "id": id,
                "sid": record.student.id,
                "sname": record.student.name,
                "cid": record.course.cno,
                "cname": record.course.cname,
                "degree": float(record.degree)
            }
        except Exception as e:
            result["success"] = -1

            result["msg"] = str(e)

        json_str = json.dumps(result)  # 序列化json
        return HttpResponse(json_str)

    ##json解析
    def score_to_json(self, obj):
        # print('类型是:',type(obj),'内容是：',obj)
        if type(obj) is Decimal:
            return float(obj)
        elif type(obj) is datetime:
            return obj.strftime('%Y-%m-%d')
