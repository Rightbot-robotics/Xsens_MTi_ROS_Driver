#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3Stamped
from sensor_msgs.msg import Imu
from std_msgs.msg import Header

class Vector3ToImuConverter(Node):
    def __init__(self):
        super().__init__('imu_msg_publisher')
        self.subscription = self.create_subscription(
            Vector3Stamped,
            '/imu/angular_velocity_hr',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Imu, '/imu/data_hr', 10)
    
    def listener_callback(self, msg):
        imu_msg = Imu()
        imu_msg.header = Header(stamp=self.get_clock().now().to_msg(), frame_id='imu_link')
        imu_msg.angular_velocity = msg.vector  # Assuming the Vector3 contains angular velocity
        # Set other fields of imu_msg as needed
        self.publisher.publish(imu_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Vector3ToImuConverter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
