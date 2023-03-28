from setuptools import setup
from glob import glob
import os

package_name = 'media_pipe_ros2'
submodules = 'media_pipe_ros2/submodules'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name), glob("launch/*pose2cmd_webcam_launch.py*")),
        (os.path.join("share", package_name), glob("launch/*pose2cmd_go1_launch.py*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Marek Pessel',
    maintainer_email='s42989@bht-berlin.de',
    description='Package responsible for using the media pipe in ros2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'human_pose_go1 = media_pipe_ros2.human_pose_go1:main',
            'human_pose_webcam = media_pipe_ros2.human_pose_webcam:main',
            'webcam_pub = media_pipe_ros2.webcam_pub:main',
            'cmd_pub = media_pipe_ros2.feature_extractor:main',
            'cmd_sub = media_pipe_ros2.cmd_sub:main',
        ],
    },
)
