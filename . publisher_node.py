#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.count = 0
        self.get_logger().info("Publisher node started!")

    def publish_message(self):
        msg = String()
        msg.data = f"Hello ROS2! Message {self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
