import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class M_sub(Node):
    def __init__(self):
        super().__init__('helloworld_subscriber')
        self.qos_profile = QoSProfile(depth = 10)
        self.helloworld_subscriber = self.create_subscription(String, 'message', self.subscriber_message, self.qos_profile)

    def subscriber_message(self, msg):
        msg.data = f'time : {self.time}'
        self.get_logger().info(f'Publisher message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = M_sub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt!!!!')
    finally:
        node.destroy_node()
        rclpy.shutdown

if __name__=='__main':
    main()