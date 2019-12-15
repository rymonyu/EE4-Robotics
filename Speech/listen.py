import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard z = %s", data.data)

def listen():
    rospy.init_node('listener', anonymous = True)
    message = rospy.Subscriber("hotword_detection",String,callback)

    print(message)
    rospy.spin()

if __name__ == '__main__':
    listen()
