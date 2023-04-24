#! /usr/bin/env python3
import rospy
# Import the service message used by the service /trajectory_by_name
from services_pkg.srv import CustomServMess, CustomServMessRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client_quiz')
# Wait for the service client /move_in_square to be running
rospy.wait_for_service('/move_tb_in_square')
time= rospy.get_param('time')
# Create the connection to the service
move_tb_in_circle_service = rospy.ServiceProxy('/move_tb_in_square', CustomServMess)
# Create an object of type MoveInSquareRequest
move_tb_in_circle_object = CustomServMessRequest()
move_tb_in_circle_object.duration=10
  
# Send through the connection the name of the request
result = move_tb_in_circle_service(move_tb_in_circle_object)
# Print the result given by the service called
print(result)
