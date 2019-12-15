import rospy
from std_msgs.msg import String

from gtts import gTTS
import os
from mutagen.mp3 import MP3
import time

from tuning import Tuning
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

state = -1
message = "global"
pub = rospy.Publisher('output', String, queue_size=10)
language = 'en'

arrived = "global"
grabbed = "global"
doa_in = "global"


Mic_tuning = Tuning(dev)

audio1 = MP3("graby.mp3")
audio2 = MP3("coffee.mp3")
audio3 = MP3("bottle.mp3")
audio4 = MP3("orange.mp3")
audio5 = MP3("grabbed.mp3")
audio6 = MP3("else.mp3")
audio7 = MP3("bye.mp3")
audio8 = MP3("grabbing.mp3")

def callback1(data):
    global state
    global message
    global arrived
    global grabbed
    # global pub
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)

    message = data.data

    print('message: ')
    print(message)


    print('state: ')
    print(state)

    # pub.publish(str(state))

def process():
    rospy.init_node('listener1', anonymous = True)
    rospy.Subscriber("hotword_detection",String, callback1)
    # rospy.init_node('listener2', anonymous = True)
    rospy.Subscriber("arrived",String,callback2)
    rospy.Subscriber("grabbed",String,callback3)

    # pub.publish(str(state))
    while True:
        fsm()
    rospy.spin()

def callback2(data):
    global arrived
    rospy.loginfo(rospy.get_caller_id() + " data2 = %s", data.data)
    arrived = data.data

def callback3(data):
    global grabbed
    rospy.loginfo(rospy.get_caller_id() + " data3 = %s", data.data)
    grabbed = data.data

def fsm():
    global state
    global message
    global arrived
    global grabbed
    # process ##################################################################
    if message == 'graby_detected' and state == -1:#Graby
        state = 0
        doa_in = Mic_tuning.direction
        print(doa_in)


    if arrived == "1" and state == 0:#Graby
        state = 1
        arrived = "0"
        print('state1 entered')
        os.system("mpg321 graby.mp3")
        time.sleep(audio1.info.length)

    elif message == 'apple_detected' and state == 1: # apple = coffed
        state = 2
        print('state2 entered')
        os.system("mpg321 coffee.mp3")
        time.sleep(audio2.info.length)

    elif message == 'banana_detected' and state == 1: # banana = bottle
        state = 3
        print('state3 entered')
        os.system("mpg321 bottle.mp3")
        time.sleep(audio3.info.length)

    elif message == 'orange_detected' and state == 1:
        state = 4
        print('state4 entered')
        os.system("mpg321 orange.mp3")
        time.sleep(audio4.info.length)

    elif message == 'yes_detected' and state == 2:
        state = 5
        print('state5 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)
        pub.publish("coffee")

    elif message == 'yes_detected' and state == 3:
        state = 6
        print('state6 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)
        pub.publish("bottle")

    elif message == 'yes_detected' and state == 4:
        state = 7
        print('state7 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)

    elif grabbed == '1' and (state == 5 or state == 6 or state == 7):
        state = 1
        grabbed = '0'
        print('state5 entered')
        os.system("mpg321 grabbed.mp3")
        time.sleep(audio5.info.length)

    elif message == 'no_detected' and (state == 2 or state == 3 or state == 4):
        state = 1
        print('state1 entered')
        os.system("mpg321 else.mp3")
        time.sleep(audio6.info.length)
        message = 'waiting' # need testing

    elif message == 'no_detected' and state == 1:
        state = -1
        print('state0 entered')
        os.system("mpg321 bye.mp3")
        time.sleep(audio7.info.length)

    ############################################################################



if __name__ == '__main__':
    # try:
    process()

    # except rospy.ROSInterruptException:
    #     pass
