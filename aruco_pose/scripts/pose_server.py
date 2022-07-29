#!/usr/bin/python3

import rospy
import actionlib
import math

from pose_msgs.msg import PoseAction
from pose_msgs.msg import PoseResult


class pose_estimation:

    def __init__(self):
        self.pose_action = actionlib.SimpleActionServer(
            '/aruco_pose', PoseAction, execute_cb=self.on_goal, auto_start=False)
        
        self.pose_action.start()

        rospy.loginfo("Pose Estimation Server has been started")

    def on_goal(self, goal):
        rospy.loginfo("A Goal has been received")   
        # rospy.loginfo(goal)

        x = goal.x
        y = goal.y
        z = goal.z
        qx = goal.qx
        qy = goal.qy
        qz = goal.qz
        qw = goal.qw

        rate = rospy.Rate(1.0/0.05)

        theta = math.atan(2*(qx*qy)*qw - qx*qx - qy*qy + qz*qz)

        pi = 22/7

        theta = abs(theta*(180/pi))

        pose_x = x*math.cos(theta) - z*math.sin(theta)
        pose_y = z*math.cos(theta) - x*math.sin(theta)

        final_x = abs(round(pose_x*100))
        final_y = abs(round(pose_y*100))

        result = PoseResult()
        result.x = final_x
        result.y = final_y
        result.theta = theta

        rate.sleep()

        self.pose_action.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('aruco_pose_server')

    server = pose_estimation()

    rospy.spin()