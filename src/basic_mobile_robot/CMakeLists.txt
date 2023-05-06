cmake_minimum_required(VERSION 3.8)
project(basic_mobile_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

install(
  DIRECTORY config launch maps meshes models params rviz src worlds scripts basic_mobile_robot
  DESTINATION share/${PROJECT_NAME}
)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS
  scripts/run_inspection.py
  scripts/lift_controller.py
  scripts/nav_to_pose.py
  scripts/nav_to_zero.py
  scripts/nav_through_poses.py
  scripts/pick_and_deliver.py
  scripts/robot_navigator.py
  scripts/security_demo.py
  scripts/waypoint_follower.py
  scripts/battery_state/battery_state_pub.py
  scripts/navigate_to_charging_dock.py
  scripts/navigate_to_charging_dock_v2.py
  scripts/transforms/map_to_base_link_transform.py
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
