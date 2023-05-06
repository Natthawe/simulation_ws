vcs import . < deps.repos       In Directory
vcs import src < deps.repos     In Directory src   

<!-- Launch -->
ros2 launch basic_mobile_robot basic_mobile_bot_v5.launch.py

ros2 topic pub /goal_pose geometry_msgs/PoseStamped "{header: {stamp: {sec: 0}, frame_id: 'map'}, pose: {position: {x: 5.0, y: -2.0, z: 0.0}, orientation: {w: 1.0}}}"

<!-- Change Parameter nav2_params.yaml -->
<!-- Just change something , Then change another thing, and watch what happens, etc. -->
-robot_radius
-inflaition_radius
-expected_planner_frequency
-update_frequency
-publish_frequency
-width/height of the rolling window in the local_costmap
-try modifying the update_rate in the LIDAR sensor inside your robot model.sdf file

<!-- coordinate frames -->
ros2 run tf2_tools view_frames
evince frames.pdf

<!-- Image of the architecture of our ROS system -->
rqt_graph

<!-- Launch the Robot With SLAM -->
sudo apt install ros-<ros2-distro>-slam-toolbox
sudo apt-get install ros-<ros-distribution>-rqt-robot-steering
ros2 launch basic_mobile_robot basic_mobile_bot_v5.launch.py slam:=True
ros2 run rqt_robot_steering rqt_robot_steering --force-discover OR Click “Navigation2 Goal” button in RVIZ

<!-- Save the Map -->
ros2 run nav2_map_server map_saver_cli -f <map_name>

ROTATION CONVERTER
https://www.andre-gaschler.com/rotationconverter/

# TURTLEBOT3
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

ros2 launch turtlebot3_navigation2 navigation2.launch.py