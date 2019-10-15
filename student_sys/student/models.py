# _*_ coding: utf-8 _*_
from __future__ import unicode_literals       #这两句是为了兼容python2.7,其中这句必须放在代码段首.
from django.db import models


class Student(models.Model):
    SEX_ITEM = [            #【】表示list
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    ]
    STATUS_ITEM = [
        (1, '申请'),
        (2, '通过'),
        (3, '拒绝'),
    ]

    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEM, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")

    status = models.IntegerField(choices=STATUS_ITEM, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return '<Student: {}>'.format(self.name)
    class Meta:
        verbose_name = verbose_name_plural = "学员信息"

    @property
    def sex_show(self):
        return dict(self.SEX_ITEM)[self.sex]

    @classmethod   #表示该方法是一个类方法，不是实例方法
    def get_all(cls):
        return cls.objects.all()