import rclpy
from ros2_unitree_legged_msgs.msg import HighCmd
from ros2_unitree_legged_msgs.msg import HighState


def come():
    msg = HighCmd()

    msg.head[0] = int('0xFE', base=16)
    msg.head[1] = int('0xEF', base=16)
    msg.mode = 2  # walk continiously
    msg.gait_type = 0
    msg.speed_level = 0
    msg.foot_raise_height = 0.1  # in meter
    msg.body_height = 0.0  # 0.0 is bodyhight while standing
    msg.euler = [0.0, 0.0, 0.0]
    msg.velocity = [0.3, 0.0]  # walk straight m/s [x,y]
    msg.yaw_speed = 0.0  # [rotation z]
    msg.reserve = 0

    return msg
