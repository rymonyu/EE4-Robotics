import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard z = %s", data.data)
    move_cmd.angular.z = data.data

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "i heard x = %s", data.data)
    move_cmd.linear.x = data.data



def Obj():
    print("running listener-object")

    #print(message)
    #angular = message
    #move_cmd.angular.z = angular
    rospy.spin()

def Pos():
    print("running listener")
    rospy.init_node('Pos',anonymous=True)
    #rospy.Subscriber("object", String)
    message = rospy.Subscriber("Coordinates",Point)
    #print(message)
    #angular = message
    #move_cmd.angular.z = angular
    rospy.spin()

def talker():
    print("running talker")
    rospy.init_node('talker', anonymous = False)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("ForwardMessage",Float64, callback2)
    rospy.Subscriber("ControlMessage",Float64, callback)

    #print(type(message))
    #print(type(move_cmd.angular.z))
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        print("x1:",move_cmd.linear.x)
        print("z2:",move_cmd.angular.z)
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    Pos()
    #Obj()
    #listener()
