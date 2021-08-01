import random

import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义帧率
FRAME_PER_SEC = 60
# 创建敌机的事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
FIRE = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    """ 飞机大战精灵 """

    # 初始化方法
    def __init__(self, image_name, speed=1):
        # 调用父类init
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕上面移动
        self.rect.y += self.speed


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.y_speed = 0

    def update(self):
        # 英雄在水平方向上移动
        self.rect.x += self.speed
        self.rect.y += self.y_speed

        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centery < 0:
            self.rect.centery = 0
        if self.rect.centerx > SCREEN_RECT.width:
            self.rect.centerx = SCREEN_RECT.width
        if self.rect.centery > SCREEN_RECT.height:
            self.rect.centery = SCREEN_RECT.height

    def fire(self):
        bullet = Bullet(self.rect.centerx,self.rect.y)
        return bullet


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self, x_address, y_address):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/bullet1.png")

        # 2.指定敌机的初始随机速度
        self.speed = 10
        self.rect.x = x_address
        self.rect.y = y_address
        # 3.指定敌机的初始随机位置

    def update(self):
        # 1.调用父类方法，保持垂直方向飞行
        self.rect.y -= self.speed


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self, SpeedAdd):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始随机速度
        self.speed = random.randint(2, 3) + SpeedAdd
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0
        # 3.指定敌机的初始随机位置

    def update(self):
        # 1.调用父类方法，保持垂直方向飞行
        super().update()

        # 2.将飞出屏幕的敌机删除
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法会自动将精灵从精灵组中移出，一旦移出就会被销毁(调用__del__())
            self.kill()
            # print("删除")


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出则移动到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
