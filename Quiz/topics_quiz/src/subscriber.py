#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
def callback(msg):
	print(msg.data)

rospy.init_node('topic_subscriber')
sub=rospy.Subscriber('/scan',Odometry,callback)

rospy.spin()
