# -*- coding: utf-8 -*-
"""
#@File : do_request.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 20:00
#@Description : TODO
"""
import requests


class doRequest:


    def req(url):
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)


def main():
    url = 'https://www.sohu.com/'
    doRequest.req(url)


if __name__ == '__main__':
    main()
