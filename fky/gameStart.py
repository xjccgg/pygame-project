import random
import pygame
from plane_sprites import *

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 提取图片
backGround = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")

# 将图片置入窗口
screen.blit(backGround, (0, 0))
screen.blit(hero, (185, 500))

# 刷新画面
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 英雄位置
heroX = 185
heroY = 500

# 创建敌方战机
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png",2)

# 创建精灵组
enemy_group = pygame.sprite.Group(enemy1,enemy2)

# 保证游戏运行
while True:
    clock.tick(90)

    heroY += random.randint(-5, 0)
    if heroX > 480:
        heroX = 0
        pass

    if heroY > 700:
        heroY = 0
        pass
    screen.blit(backGround, (0, 0))
    screen.blit(hero, (heroX, heroY))

    # 精灵组调用
    x = random.randint(-10, 10)
    enemy1.update(x)
    x = random.randint(-10, 10)
    enemy2.update(x)
    enemy_group.draw(screen)

    if heroY < 0 & heroY > -126:
        screen.blit(hero, (heroX, 700+heroY))
        pass

    if heroY < -126:
        heroY = 574
        pass

    if heroX < 0 & heroX > -102:
        screen.blit(hero, (480 + heroX, heroY))
        pass

    if heroX < -102:
        heroX = 378
        pass

    if heroX > 378 & heroX < 480:
        screen.blit(hero, (heroX - 480, heroY))
        pass

    if heroX > 480:
        heroX = 0
        pass

    # 更新画面
    pygame.display.update()

    # 监听事件
    # 处理事件
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            exit()

pygame.quit()
