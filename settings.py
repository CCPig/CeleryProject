#!/usr/bin/env python
# encoding: utf-8
"""
@author: chaochen
@file: settings.py
@time: 2021/5/15 下午3:45
"""
from celery.schedules import crontab
from kombu import Queue
import re
from datetime import timedelta

CELERY_QUEUES = {
    Queue("default", routing_key="task.default"),  # 路由键以task开头的信息都进入到default队列中
    Queue("tasks_A", routing_key="A.#"),  # 路由键以A开头的信息都进入到task_A队列中
    Queue("tasks_B", routing_key="B.#")  # 路由键以B开头的信息都进入到task_B队列中
}

CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE = "tasks"
CELERY_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_DEFAULT_ROUTING_KEY = "task.default"

CELERY_ROUTES = (
    {
        re.compile(r"CeleryPrj\.tasks\.(taskA|taskB)"): {"queue": "tasks_A", "routing_key": "A.import"}
    },
    {
        "CeleryPrj.tasks.add": {"queue": "default", "routing_key": "task.default"}
    }
)

BROKER_URL = "redis://192.168.53.184:6379/5"
CELERY_RESULT_BACKEND = "redis://192.168.53.184:6379/6"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ACCEPT_CONTENT = ['json']

CELERYBEAT_SCHEDULE = {
    "add":{
        "task":"CeleryPrj.tasks.add",
        "schedule":timedelta(seconds=10),   #每10s执行一次
        "args":(10,16)
    },
    "taskA":{
        "task": "CeleryPrj.tasks.taskA",
        "schedule": crontab(minute="*/1")   #每1min执行一次
    },
    "taskB":{
        "task": "CeleryPrj.tasks.taskB",
        "schedule": crontab(minute="*/1")   #每1min执行一次
    }
}

if __name__ == "__main__":
    pass
