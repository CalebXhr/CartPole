

def anti_angle_strategy(state):
    cart_position = state[0]  # 小车的位置
    cart_speed = state[1]  # 小车的速度
    pole_angle = state[2]  # 杆子的偏角
    pole_speed = state[3]  # 杆子的角速度
    if pole_angle < 0:
        action = 0  # push to left
    else:
        action = 1  # push to right
    return action