import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, PoseArray, Point

rospy.init_node('talke2r',anonymous = True)
    
pub4 = rospy.Publisher('Coordinates', Point, queue_size=10) 
arrived = Point()

def talk():
    
    pub = rospy.Publisher("arrived", String, queue_size=10) 
    arrived = "1"
    print(arrived)
    pub.publish(arrived)


def talk2():

    arrived.x = 0.1
    arrived.y = 0.1
    arrived.z = 0.1
    print(arrived)
    pub4.publish(arrived)
    print("published")
    pub4.publish(arrived)



talk2()
