#!/usr/bin/env python
# encoding: utf-8
"""
@author: chaochen
@file: tasks.py
@time: 2021/5/15 下午4:02
"""

import os
import time
import socket
from CeleryProject.app import app

def get_host_ip():
    """
    查询worker节点的ip
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

@app.task
def add(x, y):
    s = x + y
    time.sleep(3)
    print("主机IP{}:x + y = {}".format(get_host_ip(), s))
    return s

@app.task
def taskA():
    print("taskA begin...")
    print("主机IP{}:taskA".format(get_host_ip()))
    time.sleep(3)
    print("taskA end.")


@app.task
def taskB():
    print("taskB begin...")
    print("主机IP{}:taskB".format(get_host_ip()))
    time.sleep(3)
    print("taskB end.")


if __name__ == "__main__":
    print(get_host_ip())
    taskA()
    pass