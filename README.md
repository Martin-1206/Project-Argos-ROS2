# Unitree GO1 with gestures

## Introduction


This repository is the product of a students project at BHT Berlin in humanoid robotics (HROB), module cognitive robotics (KogRob).
With these packages you can control the Unitree Go1 robot via gestures by using a camera of Go1 or your webcam. 
We recommand you to run these packages in Ubuntu 22.04 and ROS2 Humble.
	
Authors are Emily Jean Thomas, Marek Pessel, Martin Faißt and Olivia Schmitt.

![pose_cut](https://github.com/Martin-1206/Project-Argos/assets/129275767/32782657-7190-4bc6-af37-36e7578d6376)


## Dependencies
All necessary packages are in this repo. For running them you have to make sure the following software is installed:
	
* ROS2 (recommanded version Humble)
* Python3
* OpenCV

		pip install opencv-python
		
* Mediapipe

		pip install mediapipe	
		
* GStreamer

		sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
		
		sudo apt install ros-humble-camera-calibration-parsers
		
		sudo apt install ros-humble-camera-info-manager
		
* LCM-Library

		sudo apt install liblcm-dev

## Configuration

Create a ROS Workspace
	
		mkdir -p ~/ros2_ws/src
		cd ros2_ws
		source /opt/ros/humble/setup.bash
		cd ros2_ws/src
		
Clone this repo into your src
	
		git clone https://gitlab.bht-berlin.de/kogrob-go1/kogrob_go1.git
		cd ..
		
Now build your packages
	
		colcon build
		
Check your setup by launching pose2cmd_webcam_launch.py
	
		ros2 launch media_pipe_ros2 pose2cmd_webcam_launch.py

To control the Go1 robot with your webcam, you have to enable the ros2_udp node in the
pose2cmd_webcam_launch.py


