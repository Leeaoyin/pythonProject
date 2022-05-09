# -*- coding: utf-8 -*-
"""
#@File : getDateApi.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/8 20:45
#@Description : TODO
"""
import time

import requests


def do_request():
    """发送请求"""
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    response = requests.get(url='https://api2.dayi.org.cn/api/cmedical/list2?pageNo=1&pageSize=10',
                             headers=headers)
    code = response.status_code
    print(code)
    result = response.json()['list']
    for i in range(10):
        title = result[i]['title']
        pic_url = result[i]['thumbnail']
        introduction = result[i]['introduction']



def main():
    do_request()


if __name__ == '__main__':
    main()
