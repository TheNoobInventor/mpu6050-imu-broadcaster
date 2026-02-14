# mpu6050-imu-broadcaster

MPU6050 IMU broadcaster for `ros2_control`.

*Docs in progress*

## Package setup and install

## Package launch

```
ros2 launch mpu6050_imu_broadcaster mpu6050_bringup_launch.py
```

TODO:
- Install dependencies for the package
- List package and file structure
- Steps on how to use the package
- Reference Alex Nous' library (RPi4)

Note:
- Tested with ROS2 Jazzy running on Ubuntu 24.04

## RViz visualization

On the Raspberry Pi run this command to start the MPU6050 IMU broadcaster:
```
ros2 launch mpu6050_imu_broadcaster mpu6050_bringup_launch.py
```

Then on a PC, with RViz installed, run this command to start RViz to visualize the IMU data

```
ros2 launch mpu6050_imu_broadcaster view_rviz_launch.py
```

A demo of this is shown in the GIF below.

<p align='center'>
    <img src=images/rviz_demo.gif width='600'>
</p>

## robot_localization
- Suggest using the extended kalman filter in the robot_localization package to IMU data with other data sources like wheel odometry and GPS
