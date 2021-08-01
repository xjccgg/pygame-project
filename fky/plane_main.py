import pygame

from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    # 游戏初始化
    def __init__(self):
        self.run_time = 0
        self.score = 0
        pygame.init()
        print("游戏初始化")

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，创建精灵，精灵组
        self.__create_sprites()

        # 4.设置定时器事件 - 创建敌机 - 1s
        # pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        pygame.time.set_timer(FIRE, 100)

    # 创建精灵组
    def __create_sprites(self):
        # 创建背景精灵与精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵和精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和晶精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌机精灵和精灵组
        self.bullet_group = pygame.sprite.Group()

    # 开始游戏主进程
    def start_game(self):
        print("游戏开始")

        runTime = 0

        while True:
            # 1.设置刷|新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.事件监听
            self.__event_handler(runTime)

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新/绘制精灵组
            self.__update_sprites()

            # 5.更新显示
            pygame.display.update()

            # 6.增加游戏时间
            runTime += 0.005
            # pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000, 1)
            pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    # 事件处理方法
    def __event_handler(self, runTime):
        for event in pygame.event.get():
            # 用户点击退出按钮
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy(runTime)
                # 将敌机添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == FIRE:
                bullet = self.hero.fire()
                self.bullet_group.add(bullet)

            # 通过监听事件,无法监听到长按
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

        # 通过按键数组监听
        Keys_pressed = pygame.key.get_pressed()
        if Keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif Keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

        if Keys_pressed[pygame.K_UP]:
            self.hero.y_speed = -3
        elif Keys_pressed[pygame.K_DOWN]:
            self.hero.y_speed = 3
        else:
            self.hero.y_speed = 0

    # 碰撞处理方法
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, True, True)

        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            print("Boom!!!")

            # 游戏结束
            self.__game_over()

    # 画面更新
    def __update_sprites(self):
        # 背景更新
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 敌机更新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 英雄更新
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 子弹更新
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
