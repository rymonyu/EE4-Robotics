#!/usr/bin/env python

# Steps to run this code
# 1) roslaunch baxter_moveit_tutorial moveit_init.launch
# 2) rosrun baxter_moveit_tutorial example.py
import sys
import copy
import rospy
import moveit_commander
import geometry_msgs.msg

print("HEY MAN")


def moveit_baxter_example():
    # initialize moveit_commander and rospy.
    joint_state_topic = ['joint_states:=/robot/joint_states']
    moveit_commander.roscpp_initialize(joint_state_topic)
    rospy.init_node('moveit_baxter_example', anonymous=True)

    # Instantiate a RobotCommander object.  This object is
    # an interface to the robot as a whole.
    robot = moveit_commander.RobotCommander()
    print("ROBOT current state: ", robot.get_current_state())
    group = moveit_commander.MoveGroupCommander("both_arms")
    joints = group.get_current_joint_values()
    print("JOINTS: ",joints)
    #left_current_joints = group.get_current_joint_values(end_effector_link='left_gripper').joint
    #right_current_joints = group.get_current_joint_values(end_effector_link='right_gripper').joint
    #print("LEFT JOINTS: ",left_current_joints)
    #print("RIGHT JOINTS: ",right_current_joints)


    # When finished shut down moveit_commander.
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)


if __name__ == '__main__':
    try:
        moveit_baxter_example()
    except rospy.ROSInterruptException:
        pass
