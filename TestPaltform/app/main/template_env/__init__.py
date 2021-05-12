# -*- coding: utf-8 -*-
# @Time : 2021/5/12 1:59 下午
# @Author : zy
# @Email : zyanwei2011@163.com
# @File : __init__.py
# @Project : TestPaltform

"""
过滤器文件
"""

from datetime import datetime


def str_time(ts):
    """
    将时间戳转为时间
    """
    return datetime.fromtimestamp(ts)



