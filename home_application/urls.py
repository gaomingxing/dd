# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    # 主页相关
    (r'^$', 'home'),
    (r'^login_info$', 'login_info'),

    (r'^test$', 'test'),
    (r'^exercise_test$', 'exercise_test'),
    # (r'^weixin$', 'weixin'),
    (r'^confirm$', 'confirm'),
    (r'^add$', 'add'),
    (r'^operat$', 'operat'),

    # celery练习接口
    (r'^async_test$', 'async_test'),
    (r'^time_test$', 'time_test'),

    # 实战
    (r'^search_user$', 'search_user'),
    (r'^delete_user$', 'delete_user'),
    (r'^get_user$', 'get_user'),
    (r'^update_user$', 'update_user'),

    # 作业
    (r'^select_business$', 'select_business'),  # 获取业务
    (r'^search_set$', 'search_set'),  # 获取业务下的集群
    (r'^search_hosts$', 'search_hosts'),  # 获取业务下的集群下的主机
    (r'^search_info$', 'search_info'),  # 查看详情

)
