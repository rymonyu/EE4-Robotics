import rospy
import roslib; roslib.load_manifest("moveit_python")
from moveit_python import PlanningSceneInterface, MoveGroupInterface
from geometry_msgs.msg import PoseStamped, PoseArray
import baxter_interface
from moveit_python.geometry import rotate_pose_msg_by_euler_angles
from math import pi, sqrt
from operator import itemgetter

print("HEY")

def picknplace():
    # Define initial parameters
    p = PlanningSceneInterface("base")
    g = MoveGroupInterface("both_arms", "base")
    gr = MoveGroupInterface("right_arm", "base")
    gl = MoveGroupInterface("left_arm", "base")
    leftgripper = baxter_interface.Gripper('left')
    rightgripper = baxter_interface.Gripper('right')
    leftgripper.calibrate()
    leftgripper.open()
    rightgripper.calibrate()
    rightgripper.open()
    print("Left gripper opened")
    jts_both = ['left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2', 'right_e0', 'right_e1', 'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2']
    print(jts_both)
    jts_right = ['right_e0', 'right_e1', 'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2']
    jts_left = ['left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2']
    pos1 = [-1.641426162661994, 1.0389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 0.09225918246029519,1.7238109084167481, 1.7169079948791506, 0.36930587426147465, -0.33249033539428713, -1.2160632682067871, 1.668587600115967, -1.810097327636719]
    pos2 = [-0.949534106616211, 1.4994662184448244, -0.6036214393432617, -0.7869321432861328, -2.4735440176391603, -1.212228316241455, -0.8690001153442384, 1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]
    lpos1 = [-0.241426162661994, 1.5389151064712133, 0.14240920034028015, -0.44501001475655606, -1.5630090377446503, 1.3006376573674472, 0.09225918246029519]
    lpos2 = [-0.949534106616211, 1.4994662184448244, -0.6036214393432617, -0.7869321432861328, -2.4735440176391603, -1.212228316241455, -0.8690001153442384]    
    rpos1 = [1.7238109084167481, 1.7169079948791506, 0.36930587426147465, -0.33249033539428713, -1.2160632682067871, 1.668587600115967, -1.810097327636719]
    rpos2 = [1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]
    po1 = [0.58006189975, 0.361965114384, 0.0386818529894, 0.654907716007, -0.161913424302, 0.72904857993, 0.115620476767]
    start = [-0.10468392318695408, 1.6687308800546976, 1.665535499466193, 0.08636825754631428, -0.5560560989998127, 1.2900781495458382, 0.08648558273039608, -0.11973863030986642, 1.5719682230185015, -1.616293523716939, 0.05164275889892522,  0.8895846017295099, 1.5681515495963874, 0.002805434174079302]
    initpos = [-1.1746457883232555, 1.8676216092504911, -0.014956312681882784, -0.9633399347920398, 0.6818544602150665, 1.0668836379743052, -0.4529078276231684, 1.182699187459654, 1.899835205796085, -0.029912625363765568, -0.9717768291254096, -0.6799369842302097, 1.0500098493075658, 0.37007286507735604]
    
    # Clear planning scene
    p.clear()
    # Add table as attached object
    # p.attachBox('table', 0.7, 1.27, 0.54, 0.85, -0.2, -0.38, 'base', touch_links=['pedestal'])
    # p.addCube("my_cube", 0.05, 0.9, 0, 0.2)
    # p.removeCollisionObject("table")
    # p.removeAttachedObject("table")
    # p.waitForSync()
    # Move both arms to start state              
    g.moveToJointPosition(jts_both, initpos, plan_only=False)
    #gl.moveToJointPosition(jts_left, lpos1, plan_only=False)
    #gr.moveToJointPosition(jts_right, rpos2, plan_only=False)
    # print(joint_angles)


if __name__=='__main__':
    try:
        rospy.init_node('pnp', anonymous=True)
        picknplace()

    except rospy.ROSInterruptException:
        pass
