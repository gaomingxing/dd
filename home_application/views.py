# -*- coding: utf-8 -*-
import sys
import random
import time

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_user
from conf.default import *
# from celery_test import *
from home_application.models import User

reload(sys)
sys.setdefaultencoding('utf8')

# 通用成功返回
SUCCESS_RETURN_DICT = {"result": True, "data": "success"}


def home(request):
    return render_mako_context(request, '/index.html')


def login_info(request):
    client = get_client_by_user(request.user.username)
    kwarg = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
    }
    user = client.bk_login.get_user(kwarg)
    if user["result"]:
        return render_json(user)
    else:
        return render_json({'result': False, 'data': user['data']})


def test(request):
    try:
        args = eval(request.body)
        print(args)
        print('qazxsw')
        return render_json({'result': True})
    except:
        print('aaaaa')
        return render_json({'result': False})


def exercise_test(request):
    try:
        args = eval(request.body)
        print(args)
        print('qazxsw')
        return render_json({'result': True})
    except:
        print('aaaaa')
        return render_json({'result': False})


# -----------------------------------------------------------------------------------------------------


def confirm(request):
    try:
        args = request.body
        print(args)
        return render_json({'result': True})
    except:
        return render_json({'result': False})


def add(request):
    for i in range(10):
        gender = random.choice([u'男', u'女'])
        addr = random.choice([u'北京', u'河北', u'上海', u'深圳'])
        User.objects.create(name=u'小明' + str(i), age='16' + str(i), gender=gender, addr=addr + str(i),
                            height='160' + str(i))
    return render_json({'result': True})


def operat(request):
    try:
        # 将id =3 的籍贯改为'北京'
        User.objects.filter(id=3).update(addr=u'北京')
        # 将id = 5的身高改为'170'
        User.objects.filter(id=5).update(height='170')
        # 查出年龄为'女'的所有数据
        data_nv = User.objects.filter(gender=u'女')
        # 查出最后5条数据并且从大到小排序（order_by(‘-id’)）
        data_5 = User.objects.all().order_by('-id')[:5]
        # 查出籍贯包括'北京'的所有数据
        data_beijing = User.objects.filter(addr__contains=u'北京')
        # 删除身高为'170'的所有数据
        User.objects.filter(height='170').delete()
        return render_json({'result': True})
    except Exception as e:
        print(e)
        return render_json({'result': False})


# 查询user
def search_user(request):
    try:
        args = eval(request.body)['condition']
        print(args)
        name = args['name']
        gender = args['gender']
        user = User.objects.filter(name__contains=name, gender__contains=gender, is_delete=0).order_by('-id')
        data = []
        for i in user:
            data.append(i.to_dic())
        return render_json({'result': True, 'data': data})
    except Exception as e:
        print(e)
        return render_json({'result': False})


# 删除user
def delete_user(request):
    try:
        # print(80/0)
        id = request.GET['id']
        User.objects.filter(id=id).update(is_delete=1)
        return render_json({'result': True})
    except Exception as e:
        print(e)
        return render_json({'result': False})


# 获取用户信息
def get_user(request):
    try:
        id = request.GET['id']
        user = User.objects.get(id=id).to_dic()
        print(user)
        return render_json({'result': True, 'data': user})
    except Exception as e:
        print(e)
        return render_json({'result': False})


# 更新user
def update_user(request):
    args = eval(request.body.replace('false', 'False'))['condition']
    # print(args)
    try:
        print(args)
        # print(4/0)
        if args['id']:
            if User.objects.filter(name=args['name']).exclude(id=args['id']):
                return render_json({'result': False, 'msg': u'更新的姓名已经存在！'})
            User.objects.filter(id=args['id']).update(name=args['name'], age=args['age'], gender=args['gender'],
                                                      addr=args['addr'],
                                                      height=args['height'])
        else:
            if User.objects.filter(name=args['name']):
                return render_json({'result': False, 'msg': u'添加的姓名已经存在！'})
            User.objects.create(name=args['name'], age=args['age'], gender=args['gender'], addr=args['addr'],
                                height=args['height'])
        return render_json({'result': True})
    except Exception as e:
        print(e)
        if args['id']:
            return render_json({'result': False, 'msg': u'更新用户失败，请联系开发人员！'})
        else:
            return render_json({'result': False, 'msg': u'添加用户失败，请联系开发人员！'})
