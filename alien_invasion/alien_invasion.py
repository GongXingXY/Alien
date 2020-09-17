# -*- coding: utf-8 -*-
'''
@File    :   alien_invasion.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/23 19:06 
'''
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏游戏并创建一个屏幕对象
    pygame.init()
    # 创建设置类的实例
    '''设置屏幕大小和标题'''
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 尺寸
    pygame.display.set_caption("Alien Invasion")  # 标题

    stats = GameStats(ai_settings)

    # 创建一艘飞船  飞船类的实例
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) # 飞船功能

        if stats.game_active:

            ship.update()  # 飞船移动
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets) #发射子弹
            gf.update_aliens(ai_settings, stats, screen, ship,aliens,bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 重绘屏幕


run_game()
