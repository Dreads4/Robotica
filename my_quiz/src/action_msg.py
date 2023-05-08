#! /usr/bin/env python
import rospy
import time
import actionlib

from my_quiz.msg import ActionMsgFeedback, ActionMsgResult, ActionMsgAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class ActionMsgClass(object):
    
  _feedback = ActionMsgFeedback()
  _result   = ActionMsgResult()

  def _init_(self):
    self._as = actionlib.ActionServer("action_msg_as", ActionMsgAction, self.goal_callback, False)
    self._as.start()

    
  def goal_callback(self, goal):
    
    success = True
    r = rospy.Rate(1)
    
    
    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self._takeoff_msg = Empty()
    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self._land_msg = Empty()
    
 
    up_or_down = goal.goal
    
    i = 0
    for i in xrange(0, 4):
  
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
       
        self._as.set_preempted()
        success = False

        break
    

      if up_or_down == 'UP':
        
        self._pub_takeoff.publish(self._takeoff_msg)
        self._feedback.feedback = 'Going UP'
        self._as.publish_feedback(self._feedback)
    
      if up_or_down == 'DOWN':
        
        self._pub_land.publish(self._land_msg)
        self._feedback.feedback = 'Going DOWN'
        self._as.publish_feedback(self._feedback)
    

      r.sleep()
    

    if success:
      self._result = Empty()
      self._as.set_succeeded(self._result)
      
      
if _name_ == '_main_':
  rospy.init_node('action_msg')
  ActionMsgClass()
  rospy.spin()
