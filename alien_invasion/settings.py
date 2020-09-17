# -*- coding: utf-8 -*-
'''
@File    :   settings.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/25 8:22 
'''


# 每次添加新的功能，都会引入新的设置，下面编写设置的类
class Settings():
    '''存储外星人设置的所有的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置(创建宽3像，高15像素的深灰色子弹
        self.bullet_speed_factor = 9
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1 表示向右移，为-1表示向左移
        self.fleet_direction = 1


