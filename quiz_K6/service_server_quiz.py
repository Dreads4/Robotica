#! /usr/bin/env python

import rospy
import time
# you import the service message python classes generated from Empty.srv
from services_pkg.srv import CustomServMess, CustomServMessResponse
from geometry_msgs.msg import Twist
rospy.init_node('service_server_quiz')
tb_publisher = rospy.Publisher('/volta_base_controller/cmd_vel',Twist,queue_size=1)
vel = Twist()

def my_callback(request):
	print(f"turtlebot moving in circles for {request.duration} seconds")
	current_time = time.time()
	while (time.time() < current_time + request.duration):
		vel.angular.z = 1
		vel.linear.x = 0.2
		tb_publisher.publish(vel)
	else:
		vel.angular.z = 0
		vel.linear.x = 0
		tb_publisher.publish(vel)
	return CustomServMessResponse(True)
	
my_service= rospy.Service('/move_tb_in_square', CustomServMess, my_callback)
rospy.spin()
