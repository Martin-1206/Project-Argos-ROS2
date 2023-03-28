import rclpy
from ros2_unitree_legged_msgs.msg import HighCmd
from ros2_unitree_legged_msgs.msg import HighState


def sit():
    msg = HighCmd()

    msg.head[0] = int('0xFE', base=16)
    msg.head[1] = int('0xEF', base=16)
    msg.mode = 1  # forced stand
    msg.gait_type = 0
    msg.speed_level = 0
    msg.foot_raise_height = 0.0
    msg.body_height = -0.25  # 0.0 is bodyhight while standing
    msg.euler = [0.0, -0.6, 0.0]  # body rotation
    msg.velocity = [0.0, 0.0]
    msg.yaw_speed = 0.0
    msg.reserve = 0

    return msg
