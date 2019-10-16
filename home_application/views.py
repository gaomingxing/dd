# -*- coding: utf-8 -*-
import sys
import random
import time
import requests
import json
import base64

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_user
from conf.default import *
# from celery_test import *
from home_application.models import User

reload(sys)
sys.setdefaultencoding('utf8')

# 通用成功返回
SUCCESS_RETURN_DICT = {"result": True, "data": "success"}

# 基本信息
bk_app_code = 'memory-usage'
bk_app_secret = 'cacc14e5-bc35-4d25-9e32-7e68879e3606'
host_url = 'http://testdop.gwmdc.com'


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


def select_business(request):
    '''获取业务'''
    try:
        url = host_url + '/api/c/compapi/v2/cc/search_business/'
        params = {
            'bk_app_code': bk_app_code,
            'bk_app_secret': bk_app_secret,
            "bk_username": 'admin',
        }
        res = requests.post(url, params).json()
        return render_json({'result': True, 'data': res["data"]['info']})
    except Exception as e:
        return render_json({'result': False, 'message': u'获取业务失败，{}'.format(e)})


def search_set(request):
    '''获取业务下的集群'''
    try:
        bk_biz_id = json.loads(request.body)['bk_biz_id']
        url = host_url + '/api/c/compapi/v2/cc/search_set/'
        print bk_biz_id, "--------------", url
        params = {
            'bk_app_code': bk_app_code,
            'bk_app_secret': bk_app_secret,
            'bk_biz_id': bk_biz_id,
            "bk_username": 'admin',
        }
        res = requests.post(url, params).json()
        return render_json({'result': True, 'data': res["data"]['info']})
    except Exception as e:
        return render_json({'result': False, 'message': u'获取业务下集群失败，{}'.format(e)})


def search_hosts(request):
    '''获取业务下的集群下的主机'''
    try:
        bk_set_id = json.loads(request.body)['bk_set_id']
        url = host_url + '/api/c/compapi/v2/cc/search_host/'
        params = {
            "bk_app_code": bk_app_code,
            "bk_app_secret": bk_app_secret,
            "bk_username": 'admin',
            "condition": [
                {
                    "bk_obj_id": "set",
                    "fields": [],
                    "condition": [
                        {
                            "field": "bk_set_id",
                            "operator": "$eq",
                            "value": bk_set_id
                        }
                    ]
                }
            ]
        }
        res = requests.post(url, json.dumps(params)).json()
        res_list = []
        for host_item in res['data']['info']:
            res_dict = {
                'bk_host_innerip': host_item['host']['bk_host_innerip'],
                'bk_os_name': host_item['host']['bk_os_name'],
                'bk_cpu': host_item['host']['bk_cpu'],
                'bk_host_name': host_item['host']['bk_host_name'],
                'bk_inst_name': host_item['host']['bk_cloud_id'][0]['bk_inst_name']
            }
            res_list.append(res_dict)
        return render_json({'result': True, 'data': res_list})
    except Exception as e:
        return render_json({'result': False, 'message': u'获取业务下集群下主机失败，{}'.format(e)})


# --------------------------------------------------------------------------------------------------------
# 查询主机基本信息
def search_info(request):
    host_ip = json.loads(request.body)['bk_host_innerip']
    bk_biz_id = json.loads(request.body)['bk_biz_id']
    res_tmp = fast_exe_script(host_ip, bk_biz_id)
    res = json.loads(res_tmp.content)
    if res['result'] is True:
        job_instance_id = res['job_instance_id']
        time.sleep(2)
        log_content = get_job_instance_log(job_instance_id, bk_biz_id)
        end_result_tmp = parse_log(log_content)
        end_result = json.loads(end_result_tmp.content)
        if end_result['result'] is True:
            data = end_result['data']
            return render_json({'result': True, 'data': data})
        else:
            return render_json({'result': False})
    else:
        return render_json({'result': False})


# 快速执行脚本
def fast_exe_script(host_ip, bk_biz_id):
    ip_list = [
        {
            "ip": str(host_ip),
            "bk_cloud_id": 0
        }
    ]
    params = {
        "bk_app_code": bk_app_code,
        "bk_app_secret": bk_app_secret,
        "bk_username": 'admin',
        "bk_biz_id": bk_biz_id,
        "script_content": base64.b64encode("free -m".encode('utf-8')),
        "script_type": 1,
        "account": 'root',
        "ip_list": ip_list
    }
    url = host_url + '/api/c/compapi/v2/job/fast_execute_script/'
    res = requests.post(url, json=params).json()
    try:
        job_id = res.get('data', None).get('job_instance_id', None)
        if job_id:
            return render_json({'result': True, 'job_instance_id': job_id})
    except:
        return render_json({'result': False})
    return render_json({'result': False})


# 获取日志信息
def get_job_instance_log(job_instance_id, bk_biz_id):
    # time.sleep(5)
    url = host_url + '/api/c/compapi/v2/job/get_job_instance_log/'
    params = {
        "bk_app_code": bk_app_code,
        "bk_app_secret": bk_app_secret,
        "bk_username": "admin",
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id
    }
    res = requests.get(url, params).json()
    print('job_id:{1},get log info:{0}'.format(res, job_instance_id))
    log_content = res[u'data'][0][u'step_results'][0][u'ip_logs'][0][u'log_content']
    return log_content


# 解析日志->入库
def parse_log(content):
    data = []
    print('content:{0}'.format(content))
    data_list = content.strip().split('\n')
    for item in data_list:
        print('line:{0}'.format(item))
        value_list = item.split()
        if len(value_list) < 7:
            value_list = value_list + [0, 0, 0, 0, 0, 0, 0][len(value_list):]
        value_dict = {
            'total': value_list[1],
            'used': value_list[2],
            'free': value_list[3],
            'shared': value_list[4],
            'cache': value_list[5],
            'available': value_list[6],
        }
        data.append(value_dict)
    return render_json({'result': True, 'data': data[1:2]})
