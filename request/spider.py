# -*- coding: utf-8 -*-
"""
#@File : spider.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 20:14
#@Description : TODO
"""
import time

from lxml import etree
import requests


def doSpider():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            headers={'User-Agent': 'BaiduSpider'}
        )
        tree = etree.HTML(resp.text)
        # 通过XPath语法从页面中提取电影标题

        for x in range(1, 26):
            title_spans = tree.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{x}]/div/div[2]/div[1]/a/span[1]')
            # 通过XPath语法从页面中提取电影评分
            rank_spans = tree.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{x}]/div/div[2]/div[2]/div/span[2]')
            for title_span, rank_span in zip(title_spans, rank_spans):
                res = f'insert into movie_rank values(null,"{title_span.text}", {rank_span.text});'
                insert_into_table(title_span.text,res)

        # time.sleep(2)



def insert_into_table(name,sql):
    import pymysql
    conn = pymysql.connect(host='database.jkshay.cn', port=3306, user='root', password='jksh', database='cdc', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(sql)
            if affected_rows == 1:
                print(f'插入成功：{name}')
        conn.commit()
    except pymysql.MySQLError as error:
        conn.rollback()
        print(type(error),error)
    finally:
        conn.close()


def main():
    doSpider()


if __name__ == '__main__':
    main()
