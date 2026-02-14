# This file launches an RViz node to visualize the IMU data published on /imu_broadcaster/imu topic.

import os

from launch import LaunchDescription

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Set rviz file path
    pkg_path = FindPackageShare(package="mpu6050_imu_broadcaster").find(
        "mpu6050_imu_broadcaster"
    )
    rviz_config_file = os.path.join(pkg_path, "rviz/mpu6050.rviz")

    return LaunchDescription(
        [
            Node(
                package="rviz2",
                executable="rviz2",
                output="screen",
                arguments=["-d", rviz_config_file],
            )
        ]
    )
