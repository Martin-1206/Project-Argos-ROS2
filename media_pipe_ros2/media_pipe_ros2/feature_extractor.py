import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from media_pipe_ros2_msgs.msg import MediaPipeHumanPoseList
 

class Feature_extractor(Node):

    def __init__(self) -> None:

        super().__init__('feature_extractor_node')
        self.holi_sub  = self.create_subscription(MediaPipeHumanPoseList, 'pose_pub', self.pose_callback, 10)
        self.cmd_pub  = self.create_publisher(Int8, 'cmd_pub', 10)
        self.cmd = Int8()


    def pose_callback(self, mediapipehumanposelist):

        #Coordinate origin is the upper right corner in video frame. 
        #Coordinates are normalized to [0.0, 1.0].
        

        wrist_left_y = mediapipehumanposelist.human_pose_list[15].y *100
        wrist_right_y = mediapipehumanposelist.human_pose_list[16].y *100

        shoulder_left_y = mediapipehumanposelist.human_pose_list[11].y *100
        shoulder_right_y = mediapipehumanposelist.human_pose_list[12].y*100

        index_left_y = mediapipehumanposelist.human_pose_list[19].y *100
        index_right_y = mediapipehumanposelist.human_pose_list[20].y *100

        knee_left_y = mediapipehumanposelist.human_pose_list[25].y *100
        knee_right_y = mediapipehumanposelist.human_pose_list[26].y *100


        left_come_y = abs(index_left_y - knee_left_y)
        right_come_y = abs(index_right_y - knee_right_y)

        if  (left_come_y < 1.5) and (right_come_y < 1.5): # both hands on knees

            self.cmd.data = 0       # move straight
            self.cmd_pub.publish(self.cmd)

        elif (wrist_left_y < shoulder_left_y): # left hand up

            self.cmd.data = 1       # sit
            self.cmd_pub.publish(self.cmd)

        elif (wrist_right_y < shoulder_right_y): # right hand up

            self.cmd.data = 2       # down
            self.cmd_pub.publish(self.cmd)


def main(args=None):
    rclpy.init(args=args)

    feature_extractor = Feature_extractor()

    rclpy.spin(feature_extractor)
    feature_extractor.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()