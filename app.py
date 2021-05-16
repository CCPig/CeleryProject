#!/usr/bin/env python
# encoding: utf-8
"""
@author: chaochen
@file: app.py
@time: 2021/5/15 下午3:42
"""
from celery import Celery
app = Celery("CeleryProject", include=["CeleryProject.tasks"])
app.config_from_object("CeleryProject.settings")


if __name__ == "__main__":
    app.start()
    pass