# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    # 姓名
    name = models.CharField(max_length=20,default='',unique=True)
    # 年龄
    age = models.CharField(max_length=20,default='')
    # 性别
    gender = models.CharField(max_length=10,default=u'男')
    # 籍贯
    addr = models.CharField(max_length=20,default='')
    # 身高
    height = models.CharField(max_length=20,default='')
    is_delete = models.BooleanField(default=0)

    def to_dic(self):
        tem_dict = dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
        return tem_dict

