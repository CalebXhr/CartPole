import pygame
import random

def human_play(keys):
    # 所谓非阻塞，就是用户什么都不做，程序也会持续进行
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        # 随机的输入中做下一个行动action
        print("no input")
        action = random.choice([0, 1])

    # 如果收到左方向键输入
    elif keys[pygame.K_LEFT]:
        print("left")
        action = 0

    # 如果收到右方向键输入
    elif keys[pygame.K_RIGHT]:
        print("right")
        action = 1

    return action