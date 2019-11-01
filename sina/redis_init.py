#!/usr/bin/env python
# encoding: utf-8
import redis
import sys
import os

sys.path.append(os.getcwd())
from sina.settings import LOCAL_REDIS_HOST, LOCAL_REDIS_PORT

r = redis.Redis(host=LOCAL_REDIS_HOST, port=LOCAL_REDIS_PORT)

for key in r.scan_iter("weibo_spider*"):
    r.delete(key)

start_uids = [
    '1926909715',#第一财经日报
    '1642088277',#财经网
    '1649173367',  # 每日财经新闻
    '1638782947'  # 新浪财经
]
for uid in start_uids:
    r.lpush('weibo_spider:start_urls', "https://weibo.cn/%s/info" % uid)

print('redis初始化完毕')
