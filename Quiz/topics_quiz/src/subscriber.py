#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(sensor_msgs):
    print (sensor_msgs.ranges)

rospy.init_node('topic_subscriber')  
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()

pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
rate=rospy.Rate(2)

count = Twist()
count.linear.x=0
count.angular.z=0

while not rospy.is_shutdown():
	if sensor_msgs.ranges >1:
	pub.publisher(count)
	count.linear.z +=0.5
	rate.sleep()
	if sensor_msgs.ranges<1:
	pub.publisher(count)
	count.angular.z +=180
	rate.sleep()
	if sensor_msgs.ranges.count.angular<360:
	pub.publisher(count)
	count.angular.z +=180
	rate.sleep()
	if sensor_msgs.ranges.count.angular>360:
	pub.publisher(count)
	count.angular.z -=180
	rate.sleep()

rospy.spin()
