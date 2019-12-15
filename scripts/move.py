import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


vel_vec = Twist()

def callback(data):
    global sub
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)
    sub = data.data

def move():
    global sub
    pub = rospy.Publisher('arrive', String, queue_size=10)
    movepub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('move', anonymous=True)
    rate = rospy.Rate(1000)  # 10hz

    while not rospy.is_shutdown():
        # sub = rospy.Subscriber("start", String, callback)
        #sub = '1'
        if(sub == '1'):
        # start = rospy.get_time()
            start = rospy.Time.now()
            while (rospy.Time.now()-start < rospy.Duration(4)):
                vel_vec.linear.x = 0.0
                vel_vec.linear.y = 0.0
                vel_vec.linear.z = 0.0
                vel_vec.angular.x = 0.0
                vel_vec.angular.y = 0.0
                vel_vec.angular.z = 0.1
                rospy.loginfo(vel_vec)
                movepub.publish(vel_vec)
            arrive_str = "1"
            sub = '0'
            rospy.loginfo(arrive_str)
            pub.publish(arrive_str)

        # sub = '2'
        if (sub == '2'):
            start = rospy.Time.now()
            while (rospy.Time.now() - start < rospy.Duration(7)):
                vel_vec.linear.x = 0.0
                vel_vec.linear.y = 0.0
                vel_vec.linear.z = 0.0
                vel_vec.angular.x = 0.0
                vel_vec.angular.y = 0.0
                vel_vec.angular.z = -0.15
                rospy.loginfo(vel_vec)
                movepub.publish(vel_vec)
            start = rospy.Time.now()
            while (rospy.Time.now() - start < rospy.Duration(10)):
                vel_vec.linear.x = 0.17
                vel_vec.linear.y = 0.0
                vel_vec.linear.z = 0.0
                vel_vec.angular.x = 0.0
                vel_vec.angular.y = 0.0
                vel_vec.angular.z = 0.0
                rospy.loginfo(vel_vec)
                movepub.publish(vel_vec)
            arrive_str = "2"
            sub = '0'
            rospy.loginfo(arrive_str)
            pub.publish(arrive_str)

        # sub = '3'
        if (sub == '3'):
            start = rospy.Time.now()
            while (rospy.Time.now() - start < rospy.Duration(11)):
                vel_vec.linear.x = 0.0
                vel_vec.linear.y = 0.0
                vel_vec.linear.z = 0.0
                vel_vec.angular.x = 0.0
                vel_vec.angular.y = 0.0
                vel_vec.angular.z = 0.2
                rospy.loginfo(vel_vec)
                movepub.publish(vel_vec)
            start = rospy.Time.now()
            while (rospy.Time.now() - start < rospy.Duration(5)):
                vel_vec.linear.x = 0.1
                vel_vec.linear.y = 0.0
                vel_vec.linear.z = 0.0
                vel_vec.angular.x = 0.0
                vel_vec.angular.y = 0.0
                vel_vec.angular.z = 0.0
                rospy.loginfo(vel_vec)
                movepub.publish(vel_vec)
            arrive_str = "3"
            sub = '0'
            rospy.loginfo(arrive_str)
            pub.publish(arrive_str)
        rate.sleep()

        # spin() simply keeps python from exiting until this node is stopped
        # rospy.spin()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass