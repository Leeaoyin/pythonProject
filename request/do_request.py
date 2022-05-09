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


def send_request():
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'Connection':'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'cookie':'_uab_collina=159064902498619873123303; lastCity=101200100; historyState=state; wd_guid=b872d8ad-7b90-485e-8017-9c2fc324d4d9; _bl_uid=p1k1bztLy6s1I1b0R5qkik0wtLRj; acw_tc=0a099d9216519081060921091e9e12e83b258ad896f0dcf2fbbf102aace7d2; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1651908031; __g=-; __c=1651908036; __a=13727421.1590649025.1645605114.1651908036.220.8.5.10; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1651908118; __zp_stoken__=3ac4dMRYiIQA%2FSSYYNQwxJxofe3tvXmBeW2wyQ3t2VgQqEnVVNW0NHHhtK1NqeHQwWl0HKDspBBx%2FKRw3Jn9%2FVA4wJQ9JD1cNXzhleBR2QR8oOlJXFw9YAA0faQwPTRxqGGQ1VmBWBWRpbEY%3D; __zp_sseed__=Nr5Ybxmdx4fckjDsWN5i2/HLbHGjTzDA2CLS/k6rzXw=; __zp_sname__=1a5b7263; __zp_sts__=1651908317762'

    }
    resp = requests.post('https://www.zhipin.com/c101200100-p100101/', header)
    res_json = resp.text
    print(res_json)


def do_sem():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser  = webdriver.Chrome()
    browser .get('https://www.baidu.com')
    # 通过元素ID获取元素
    kw_input = browser.find_element(By.ID, 'kw')
    # 模拟用户输入行为
    kw_input.send_keys('Python')
    # 通过CSS选择器获取元素
    su_button = browser.find_element(By.CSS_SELECTOR, '#su')
    # 模拟用户点击行为
    su_button.click()
    res = input('qingshuru ')




def main():
    # url = 'https://www.sohu.com/'
    # doRequest.req(url)
    do_sem()

if __name__ == '__main__':
    main()
