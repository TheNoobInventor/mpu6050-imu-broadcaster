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
- Suggest using the extended kalman filter in the robot_localization package to IMU data with other data sources like
wheel odometry and GPS

## RViz visualization

```
ros2 launch mpu6050_imu_broadcaster view_rviz_launch.py
```

- Include demo
