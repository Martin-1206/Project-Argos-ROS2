import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from ros2_unitree_legged_msgs.msg import HighCmd
from ros2_unitree_legged_msgs.msg import HighState
from .submodules.down import down
from .submodules.sit import sit
from .submodules.come import come


class CmdToAction(Node):
    def __init__(self) -> None:
        super().__init__("cmd_to_action_node")

        self.cmd_sub = self.create_subscription(
            Int8, 'cmd_pub', self.command_callback, 10)

        self.action_pub = self.create_publisher(
            HighCmd, 'high_cmd', 10)

        self.action = HighCmd()

    def command_callback(self, cmd):

        command = cmd.data

        if (command == 0):

            self.action = come()

        elif (command == 1):

            self.action = sit()

        elif (command == 2):

            self.action = down()

        else:
            self.action = HighCmd()

        self.action_pub.publish(self.action)


def main(args=None):
    rclpy.init(args=args)

    cmd_to_action = CmdToAction()

    rclpy.spin(cmd_to_action)

    cmd_to_action.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
