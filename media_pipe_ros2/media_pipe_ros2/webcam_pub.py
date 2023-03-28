import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    """
    Create an ImagePublisher class, which is a subclass of the Node class.
    """
    def __init__(self):
        
        super().__init__('image_publisher')

        self.image_pub = self.create_publisher(Image, 'video_frame', 10)

        self.timer = self.create_timer(0.03, self.timer_callback) # publishing with 30 Hz
        
        self.cap = cv2.VideoCapture(0) # The argument '0' gets the default webcam

        self.br = CvBridge() # Bridge between ROS and OpenCV

    def timer_callback(self):
        # Capture frame-by-frame
        # This method returns True/False as well as the video frame.
        ret, frame = self.cap.read()

        if ret == True:
            
            msg = self.br.cv2_to_imgmsg(frame) # converts an OpenCV image to a ROS 2 image message
            self.image_pub.publish(msg)

def main(args=None):

    rclpy.init(args=args)

    image_publisher = ImagePublisher()

    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()


    if __name__ == '__main__':
        main()
