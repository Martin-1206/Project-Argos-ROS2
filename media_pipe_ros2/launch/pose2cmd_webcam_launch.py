from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_path = get_package_share_directory("media_pipe_ros2")

    webcam_pub = Node(
        package = "media_pipe_ros2",
        name = "webcam_pub",
        executable = "webcam_pub"
    )

    human_pose_webcam = Node(
        package = "media_pipe_ros2",
        name = "human_pose_webcam",
        executable = "human_pose_webcam"
    )

    cmd_from_pose = Node(
        package = "media_pipe_ros2",
        name = "feature_extractor",
        executable = "cmd_pub"
    )
    
    cmd_to_action = Node(
        package = "media_pipe_ros2",
        name = "cmd_sub",
        executable = "cmd_sub"
    )
    
    """
    ros2_udp = Node(
    	packages = "unitree_legged_real",
    	name = "ros_udp",
    	executable = "ros2_udp",
    	arguments = ["highlevel"]
    )
    """
    return LaunchDescription([webcam_pub, human_pose_webcam, cmd_from_pose, cmd_to_action]) # ros2_udp
