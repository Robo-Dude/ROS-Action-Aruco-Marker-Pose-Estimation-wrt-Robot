#!/usr/bin/python3

import rospy
import actionlib

from geometry_msgs.msg import PoseStamped

from pose_msgs.msg import PoseAction
from pose_msgs.msg import PoseGoal


class Pose_client:

    def __init__(self):

        self.pose_x = 0
        self.pose_y = 0
        self.pose_z = 0
        self.q_x = 0
        self.q_y = 0
        self.q_z = 0
        self.q_w = 0

        self.action_client = actionlib.SimpleActionClient(
            '/aruco_pose', PoseAction)

        self.action_client.wait_for_server()
        rospy.loginfo('Action server is up, we can send new goal')

        rospy.Subscriber('/single/pose', PoseStamped,
                         self.aruco_pose, queue_size=10)

    def aruco_pose(self, msg):

        self.pose_x = msg.pose.position.x
        self.pose_y = msg.pose.position.y
        self.pose_z = msg.pose.position.z
        self.q_x = msg.pose.orientation.x
        self.q_y = msg.pose.orientation.y
        self.q_z = msg.pose.orientation.z
        self.q_w = msg.pose.orientation.w

        # self.send_goal_and_result()

        goal = PoseGoal(x=self.pose_x, y=self.pose_y, z=self.pose_z,
                        qx=self.q_x, qy=self.q_y, qz=self.q_z, qw=self.q_w)

        rate = rospy.Rate(1.0/0.05)

        self.action_client.send_goal(goal)
        rospy.loginfo("Goal has been sent.")
        self.action_client.wait_for_result()
        # rospy.loginfo(self.action_client.get_result())
        result = self.action_client.get_result()
        print(result)

        # print(self.pose_y)

        rate.sleep()

if __name__ == '__main__':

    rospy.init_node('aruco_pose_client')

    client = Pose_client()

    rospy.spin()
