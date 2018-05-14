#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *
import random

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos,screen):
        pygame.sprite.Sprite.__init__(self)
        bullet_rect = pygame.Rect(1004, 987, 9, 21)
        plane_img = pygame.image.load('../../resource/image/shoot.png')
        bullet_img = plane_img.subsurface(bullet_rect)
        self.rect = bullet_img.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def update(self):
        self.rect.top -= self.speed



# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, init_pos,screen):
        pygame.sprite.Sprite.__init__(self)
        # 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果

        player_rect = []
        player_rect.append(pygame.Rect(0, 99, 102, 126))  # 玩家飞机图片
        player_rect.append(pygame.Rect(165, 360, 102, 126))
        player_rect.append(pygame.Rect(165, 234, 102, 126))  # 玩家爆炸图片
        player_rect.append(pygame.Rect(330, 624, 102, 126))
        player_rect.append(pygame.Rect(330, 498, 102, 126))
        player_rect.append(pygame.Rect(432, 624, 102, 126))
        self.initPos = [200, 600]
        # 飞机及子弹图片集合
        self.image =[]
        plane_img = pygame.image.load('../../resource/image/shoot.png')
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())

        self.screen = screen
        self.f = 0

    # 发射子弹
    def shoot(self, bullet_img):
        pass


    # 向上移动，需要判断边界
    def moveUp(self):
        pass


    # 向下移动，需要判断边界
    def moveDown(self):
        pass


    # 向左移动，需要判断边界
    def moveLeft(self):
        pass


    # 向右移动，需要判断边界
    def moveRight(self):
        pass


    def update(self):
        self.f = self.f + 1
        if self.f % 100 == 0:
            self.initPos = [self.initPos[0] - 3,self.initPos[1]]
        self.screen.blit(self.image[self.f %len(self.image)], self.initPos)
        pass


# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self,initPos,screen):
        pygame.sprite.Sprite.__init__(self)
        plane_img = pygame.image.load('resource/image/shoot.png')
        enemy1_rect = pygame.Rect(534, 612, 57, 43)
        enemy1_img = plane_img.subsurface(enemy1_rect)
        self.screen = screen
        self.img = enemy1_img
        self.initPos = initPos
        self.f = 0

    # 敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        pass

    def update(self):
        self.f = self.f + 1
        if self.f % 30 == 0:
            self.initPos =  self.initPos[0] - 1
        self.screen.blit(self.img,self.initPos)
        pass

if __name__ == '__main__':
    # 初始化 pygame
    pygame.init()
    # 设置游戏界面大小、背景图片及标题
    # 游戏界面像素大小
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 游戏界面标题
    pygame.display.set_caption('飞机大战')
    # 背景图
    background = pygame.image.load('../../resource/image/background.png').convert()
    # 游戏循环帧率设置
    clock = pygame.time.Clock()
    # 判断游戏循环退出的参数
    running = True
    p = Player(1, screen)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后退出程序
                exit()
        # 绘制背景
        screen.fill(0)
        screen.blit(background, (0, 0))

        p.update()
        # 更新屏幕
        pygame.display.update()
    pass
