import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class M_pub(Node):
    def __init__(self):
        super().__init__('message_publisher')
        self.message_publisher = self.create_publisher(String, 'm_pub', 10)

def main(args=None):
    pass

# main일때만 코드 실행
if __name__=='__main':
    main()
