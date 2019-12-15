import rospy
from std_msgs.msg import String

def talk():
    rospy.init_node('talke2r',anonymous = True)
    pub = rospy.Publisher('grabbed', String, queue_size=10)
    rate = rospy.Rate(5)
    counter = 0

    while not rospy.is_shutdown():
        counter = counter + 1
        print(counter)
        if counter == 2:
            pub.publish("1")
            break
        pub.publish("1")

        rate.sleep()



if __name__ == '__main__':
    talk()
