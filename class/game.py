# -*- coding: utf-8 -*-
"""
#@File : game.py
#@Author : aoyinli@jksh.com
#@Time : 2022/5/6 23:31
#@Description : TODO
"""

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    #设置标题
    pygame.display.set_caption('自定义应用')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50

    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
