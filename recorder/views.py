import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Label


def index(request):
    return render(request, "index.html")


def view(request):
    return render(request, "viewer.html")


def get_label(request):
    """
    获取标签
    """
    if request.method == "GET":
        name = request.GET.get("name", None)
        date_type = request.GET.get("dateType", None)
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        start = (page - 1) * limit
        date_start = request.GET.get("dateStart", "1970-01-01")
        date_end = request.GET.get("dateEnd", datetime.datetime.now().strftime("%Y-%m-%d"))

        """
        开始检索数据
        """
        if date_type == 1:
            label_list = Label.objects.filter(date_create__gte=date_start, date_create__lte=date_end)
        elif date_end == 2:
            label_list = Label.objects.filter(date_modify__gte=date_start, date_modify__lte=date_end)
        else:
            label_list = Label.objects.all()

        if name:
            label_list = label_list.filter(name=name)

        label_list = label_list[start:start + limit]
        print(label_list)

        """
        整理返回的数据格式
        """
        try:
            resp = {"code": 1, "msg": "获取标签列表成功！", "data": {
                "label_list": [{
                    "id": label.id,
                    "name": label.name,
                    "brief": label.brief,
                    "dateCreate": label.date_create.strftime("%Y-%m-%d"),
                    "dateModify": label.date_modify.strftime("%Y-%m-%d")
                } for label in label_list]
            }}
            print(resp)
        except Exception as error:
            resp = {"code": 0, "msg": error, "data": {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}

    return HttpResponse(json.dumps(resp))


def add_label(request):
    """
    创建标签
    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        brief = request.POST.get("brief", "")

        if name == "":
            return HttpResponse(json.dumps({"code": 0, "msg": "标签名称为空！", "data": {}}))
        try:
            Label.objects.create(name=name, brief=brief)
            resp = {"code": 1, "msg": "创建标签成功！", "data": {}}
        except Exception as error:
            resp = {"code": 0, "msg": error, "data": {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}

    return HttpResponse(json.dumps(resp))


def delete_label(request):
    """
    删除标签
    """
    if request.method == "GET":
        id = request.GET.get("id", "")

        if id == "":
            return HttpResponse(json.dumps({"code": 0, "msg": "标签号为空！", "data": {}}))
        try:
            label = Label.objects.get(id=id)
            label.delete()
            resp = {"code": 1, "msg": "删除标签成功！", "data": {}}
        except Exception as error:
            resp = {"code": 0, "msg": error, "data": {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}

    return HttpResponse(json.dumps(resp))


def modify_label(request):
    """
    修改标签
    """
    if request.method == "POST":
        id = request.POST.get("id", "")
        name = request.POST.get("name", "")
        brief = request.POST.get("brief", "")

        if id == "":
            return HttpResponse(json.dumps({"code": 0, "msg": "标签号为空！", "data": {}}))
        elif name == "":
            return HttpResponse(json.dumps({"code": 0, "msg": "标签名称为空！", "data": {}}))
        try:
            label = Label.objects.get(id=id)
            label.name = name
            label.brief = brief
            label.save()
            resp = {"code": 1, "msg": "修改标签成功！", "data": {}}
        except Exception as error:
            resp = {"code": 0, "msg": error, "data": {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}

    return HttpResponse(json.dumps(resp))
