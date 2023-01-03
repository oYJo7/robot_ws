import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from rclpy.qos import QoSProfile

class M_pub(Node):
    def __init__(self):
        super().__init__('time_publisher')
        self.qos_profile = QoSProfile(depth = 10)
        self.message_publisher = self.create_publisher(Header, 'time', self.qos_profile)
        self.timer = self.create_timer(0.01, self.m_publisher)
    
    def m_publisher(self):
        msg = Header()
        msg.stamp = self.get_clock().now().to_msg()
        self.message_publisher.publish(msg) 
        self.get_logger().info(f'Publisher message: {msg.stamp}')
        self.get_logger().info(f'Publisher message: {self.get_clock().now().seconds_nanoseconds()}')

def main(args=None):
    rclpy.init(args=args)
    node = M_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt!!!!')
    finally:
        node.destroy_node()
        rclpy.shutdown

# main일때만 코드 실행
if __name__=='__main':
    main()
