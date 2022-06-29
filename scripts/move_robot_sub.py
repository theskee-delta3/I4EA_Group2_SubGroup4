#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback(data):
	print("hip1=%f"%(data.data))

rospy.init_node("subscriber_node")
sub_1 = rospy.Subscriber("/my_spideybot/joint1_position_controller/command", Float64, callback)
sub_2 = rospy.Subscriber("/my_spideybot/joint4_position_controller/command", Float64, callback)
sub_3 = rospy.Subscriber("/my_spideybot/joint7_position_controller/command", Float64, callback)
sub_4 = rospy.Subscriber("/my_spideybot/joint10_position_controller/command", Float64, callback)
sub_5 = rospy.Subscriber("/my_spideybot/joint13_position_controller/command", Float64, callback)
sub_6 = rospy.Subscriber("/my_spideybot/joint16_position_controller/command", Float64, callback)





rospy.spin()



