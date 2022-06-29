#!/usr/bin/env python
# Copyright (c) 2022, KEIN CHANBOCHHIN.

import rospy
from std_msgs.msg import Float64
from time import sleep
import math
import numpy as np
# def range_float(start, stop, step):
# 	x = start
# 	while x <= stop:
# 		yield x
# 		x = x + step
def talker():
	rospy.init_node("spideyBot_move_node")

	hip2_pub = rospy.Publisher('/my_spideybot/joint4_position_controller/command', Float64, queue_size=10)
	hip4_pub = rospy.Publisher('/my_spideybot/joint10_position_controller/command', Float64, queue_size=10)
	hip6_pub = rospy.Publisher('/my_spideybot/joint16_position_controller/command', Float64, queue_size=10)

	hip1_pub = rospy.Publisher('/my_spideybot/joint1_position_controller/command', Float64, queue_size=10)
	hip3_pub = rospy.Publisher('/my_spideybot/joint7_position_controller/command', Float64, queue_size=10)
	hip5_pub = rospy.Publisher('/my_spideybot/joint13_position_controller/command', Float64, queue_size=10)

	position_joint1,position_joint2,position_joint3 = Float64(),Float64(),Float64()
	position_joint1.data = 0.5
	position_joint2.data = -0.5
	position_joint3.data = -0.5
	
	rate = rospy.Rate(10)
	i = 0
	while not rospy.is_shutdown():
		
		hip1_pub.publish(position_joint1)
		hip3_pub.publish(position_joint1)
		hip5_pub.publish(position_joint1)
		sleep(1.5)
		hip2_pub.publish(position_joint1)
		hip4_pub.publish(position_joint2)
		hip6_pub.publish(position_joint3)
		
		# rate.sleep()
		# position_joint1.data = math.sin(i)
		# i =+ 0.1
		# leg1_pub.publish(position_joint3)
		# rate.sleep()
		position_joint1.data *= -1
		position_joint2.data *= -1
		position_joint3.data *= -1
		rate.sleep()
		
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
	



