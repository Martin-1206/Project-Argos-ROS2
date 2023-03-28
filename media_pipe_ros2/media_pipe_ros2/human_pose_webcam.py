import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import mediapipe as mp                         
from mediapipe.python.solutions.pose import PoseLandmark
from media_pipe_ros2_msgs.msg import MediaPipeHumanPoseList

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

NAME_POSE = [
    (PoseLandmark.NOSE), (PoseLandmark.LEFT_EYE_INNER),
    (PoseLandmark.LEFT_EYE), (PoseLandmark.LEFT_EYE_OUTER),
    (PoseLandmark.RIGHT_EYE_INNER), (PoseLandmark.RIGHT_EYE),
    (PoseLandmark.RIGHT_EYE_OUTER), (PoseLandmark.LEFT_EAR),
    (PoseLandmark.RIGHT_EAR), (PoseLandmark.MOUTH_LEFT),
    (PoseLandmark.MOUTH_RIGHT), (PoseLandmark.LEFT_SHOULDER),
    (PoseLandmark.RIGHT_SHOULDER), (PoseLandmark.LEFT_ELBOW),
    (PoseLandmark.RIGHT_ELBOW), (PoseLandmark.LEFT_WRIST),
    (PoseLandmark.RIGHT_WRIST), (PoseLandmark.LEFT_PINKY),
    (PoseLandmark.RIGHT_PINKY), (PoseLandmark.LEFT_INDEX),
    (PoseLandmark.RIGHT_INDEX), (PoseLandmark.LEFT_THUMB),
    (PoseLandmark.RIGHT_THUMB), (PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP), (PoseLandmark.LEFT_KNEE),
    (PoseLandmark.RIGHT_KNEE), (PoseLandmark.LEFT_ANKLE),
    (PoseLandmark.RIGHT_ANKLE), (PoseLandmark.LEFT_HEEL),
    (PoseLandmark.RIGHT_HEEL), (PoseLandmark.LEFT_FOOT_INDEX),
    (PoseLandmark.RIGHT_FOOT_INDEX)
]

class PosePublisher(Node):

    def __init__(self):
        super().__init__('mediapipe_pose_publisher')
        self.subscription = self.create_subscription(Image, '/video_frame', self.getimage_callback, 10)  
        self.pose_pub = self.create_publisher(MediaPipeHumanPoseList, 'pose_pub', 10)
        self.cvbr = CvBridge()

        self.pose = mp_pose.Pose(
               min_detection_confidence=0.7, # value for the person-detection to be considered successful.
               min_tracking_confidence=0.8)  # value for the pose-landmarks-detection to be considered tracked successfully,
        
    def getimage_callback(self, data):

        
        mediapipehumanposelist = MediaPipeHumanPoseList()
  
        image = self.cvbr.imgmsg_to_cv2(data)  #if RGB is incorrect try to add ,desired_encoding="bgr8"                 
        image.flags.writeable = False          #to improve performance mark image as not writeable to pass by reference
        results_p = self.pose.process(image)
        image.flags.writeable = True

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        mp_drawing.draw_landmarks(
            image, results_p.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                
        if results_p.pose_landmarks != None:
            index_pose = 0
            for pose_landmarks in (results_p.pose_world_landmarks.landmark):

                mediapipehumanposelist.human_pose_list[index_pose].name = str(NAME_POSE[index_pose])
                mediapipehumanposelist.human_pose_list[index_pose].x = pose_landmarks.x
                mediapipehumanposelist.human_pose_list[index_pose].y = pose_landmarks.y
                mediapipehumanposelist.human_pose_list[index_pose].visibility = pose_landmarks.visibility
                index_pose = index_pose +1

            mediapipehumanposelist.num_humans = 1
            self.pose_pub.publish(mediapipehumanposelist)


        cv2.imshow('MediaPipe Pose', image)
        cv2.waitKey(1)

         
def main(args=None):
    rclpy.init(args=args)

    pose_publisher = PosePublisher()
    
    #cap.release()
    
    rclpy.spin(pose_publisher)

    pose_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
