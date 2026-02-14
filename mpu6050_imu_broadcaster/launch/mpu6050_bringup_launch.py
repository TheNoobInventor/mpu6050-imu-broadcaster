# This launch file starts the ros2_control IMU sensor broadcaster for the MPU6050 IMU sensor.
# The IMU data is published on the /imu_broadcaster/imu topic.

import os

from launch import LaunchDescription
from launch.substitutions import Command

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Set the path to different files and folders
    pkg_path = FindPackageShare(package="mpu6050_imu_broadcaster").find(
        "mpu6050_imu_broadcaster"
    )
    description_file = os.path.join(pkg_path, "urdf/mpu6050.urdf.xacro")
    controller_params_file = os.path.join(pkg_path, "config/controllers.yaml")

    # Get URDF via xacro
    robot_description_content = Command(["xacro ", description_file])

    robot_description = {"robot_description": robot_description_content}

    # Launch controller manager
    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[controller_params_file],
        output="both",
    )

    # Start robot_state_publisher node
    robot_state_pub_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="both",
    )

    # Spawn joint_state_broadcaster
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broadcaster"],
    )

    # Spawn imu_sensor_broadcaster
    imu_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["imu_broadcaster"],
    )

    return LaunchDescription(
        [
            robot_state_pub_node,
            controller_manager_node,
            joint_state_broadcaster_spawner,
            imu_broadcaster_spawner,
        ]
    )
