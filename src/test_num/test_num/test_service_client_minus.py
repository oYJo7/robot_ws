import rclpy
from rclpy.node import Node
from class_test_interfaces.srv import MinusThreeInts

class Num_cli_minus(Node):
  def __init__(self):
    super().__init__('minus_int_client')
    self.cli = self.create_client(MinusThreeInts, 'minus_int')
    while not self.cli.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('service not available, waiting again...')
    self.req = MinusThreeInts.Request()
    self.var_a = 40
    self.var_b = 82
    self.var_c = 15

  def request_add(self):
    self.req.a = self.var_a
    self.req.b = self.var_b
    self.req.c = self.var_c
    self.future = self.cli.call_async(self.req)

def main(args = None):
  rclpy.init(args=args)
  node = Num_cli_minus()
  node.request_add()
  try:
    while rclpy.ok():
      rclpy.spin_once(node)
      print(node.future.done())
      if node.future.done():
        try:
          node.response = node.future.result()
        except Exception as e:
          node.get_logger().info('Service call failed %r'%(e,))
        else :
          node.get_logger().info(f'Result of minus_three_ints: {node.req.a} - {node.req.b} - {node.req.c} = {node.response.sum}')
        break
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()