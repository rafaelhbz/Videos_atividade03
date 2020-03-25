#! /usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

v = 2  # Velocidade linear
w = 1  # Velocidade angular

if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():
            vel = Twist(Vector3(0.33,0,0), Vector3(0,0,3))
            pub.publish(vel)
            rospy.sleep(0.5)
            vel = Twist(Vector3(0.33,0,0), Vector3(0,0,0))
            pub.publish(vel)
            rospy.sleep(0.5)
            vel = Twist(Vector3(0.33,0,0), Vector3(0,0,3))
            pub.publish(vel)
            rospy.sleep(0.5)
            vel = Twist(Vector3(0.33,0,0), Vector3(0,0,0))
            pub.publish(vel)
            rospy.sleep(0.5)


    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")