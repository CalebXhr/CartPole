import gym
import pygame
import time
import random
from strategies.human_play import human_play
from strategies.greedy_strategy import anti_angle_strategy

if __name__ == '__main__':
    pygame.init()
    env = gym.make('CartPole-v1', render_mode='human')
    state, _ = env.reset()

    # print(state)

    cart_position = state[0]  # 小车的位置
    cart_speed = state[1]  # 小车的速度
    pole_angle = state[2]  # 杆子的偏角
    pole_speed = state[3]  # 杆子的角速度

    # 显示环境参数变化会用于后续的训练

    print(f"Begin state: {state}")
    print(f"cart_position = {cart_position:.2f}")
    print(f"cart_speed = {cart_speed:.2f}")
    print(f"pole_angle = {pole_angle:.2f}")
    print(f"pole_speed = {pole_speed:.2f}")

    time.sleep(3)  # 等待3秒钟，以便人类观察, 完成一个采
    # 样周期

    # 获得游戏过程
    start_time = time.time() # 记录游戏的开始时间
    max_action = 1000 # 设置策略的最大执行次数

    # 我考虑用最大值10000次作为步数限制。因为我记得学习的时候，
    # 那种游戏200多步，1000就实际上是够了，我就横着差不多折中值的这样

    step = 0
    fail = False
    for step in range(1, max_action + 1):
        # 我们先使用time.sleep. 值等待0.3秒，用于人的反应时间。
        time.sleep(0.3)

        # 如果觉得自己反应够快，这里可以设置更短时间。比如1分钟，
        # time.sleep(0.1)

        # 以非阻塞的方式，接收用户的输入输入
        keys = pygame.key.get_pressed()
        action = 0

        # action = human_play(keys)
        action = anti_angle_strategy(state)
        if action == 0:
            print("push to left")
        else:
            print("push to right")
        # 控制环境中的小车，执行输入命令
        # 每行动一次，都会得到当前的小车信息
        state, _, done, _, _ = env.step(action)

        # 如果done为真，就说明游戏结束了，即杆子倒了
        if done:
            fail = True
            break

        print("----------------------")
        print(f"step = {step} action = {action}"
              f"angle = {state[2]:.2f} position = {state[0]:.2f}")

    # 计算结束时间
    end_time = time.time()
    game_time = end_time - start_time

    # 打印提示
    if fail:
        print(f"Game over, you play {game_time:.2f} seconds, {step} steps.")
    else:

        print(f"Congratulation! You play {game_time:.2f} seconds, {step} steps.")
    env.close()