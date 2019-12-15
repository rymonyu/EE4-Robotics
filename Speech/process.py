import rospy
from std_msgs.msg import String

from gtts import gTTS
import os
from mutagen.mp3 import MP3
import time

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

state = -1
message = "global"
pub1 = rospy.Publisher('output', String, queue_size=10)
pub2 = rospy.Publisher('start', String, queue_size=10)
pub3 = rospy.Publisher('thank', String, queue_size=10)
language = 'en'

#arrived = "global"
grabbed = "global"

audio1 = MP3("graby.mp3")
audio2 = MP3("coffee.mp3")
audio3 = MP3("bottle.mp3")
audio4 = MP3("orange.mp3")
audio5 = MP3("grabbed.mp3")
audio6 = MP3("else.mp3")
audio7 = MP3("bye.mp3")
audio8 = MP3("grabbing.mp3")
audio9 = MP3("hereur.mp3")
audio_human = MP3("human.mp3")
audio_welcome = MP3("welcome.mp3")
audio_introduce = MP3("introduce.mp3")

def callback1(data):
    global state
    global message
#    global arrived
    global grabbed
    # global pub
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)

    message = data.data

    print('message(callback): ')
    print(message)


    print('state(callback): ')
    print(state)

    # pub.publish(str(state))

def process():
    rospy.init_node('listener1', anonymous = True)
    rospy.Subscriber("hotword_detection",String, callback1)
    # rospy.init_node('listener2', anonymous = True)
    #rospy.Subscriber("arrived",String,callback2)
    rospy.Subscriber("grabbed",String,callback3)

    # pub.publish(str(state))
    while True:
        fsm()
    rospy.spin()

#def callback2(data):
#    global arrived
#    rospy.loginfo(rospy.get_caller_id() + " data2 = %s", data.data)
#    arrived = data.data

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
        pub2.publish("1")

    if state == 0:#Graby
        state = 1
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

    elif message == 'introduce_detected' and state == 1:
        print('state4 entered')
        os.system("mpg321 introduce.mp3")
        time.sleep(audio_introduce.info.length)

    elif message == 'yes_detected' and state == 2:
        state = 5
        print('state5 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)
        pub1.publish("coffee")
        time.sleep(7)
        os.system("mpg321 human.mp3")
        time.sleep(audio_human.info.length)

    elif message == 'yes_detected' and state == 3:
        state = 5
        print('state5 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)
        pub1.publish("bottle")
        time.sleep(7)
        os.system("mpg321 human.mp3")
        time.sleep(audio_human.info.length)

    elif message == 'yes_detected' and state == 4:
        state = 5
        print('state5 entered')
        os.system("mpg321 grabbing.mp3")
        time.sleep(audio8.info.length)
        time.sleep(7)
        os.system("mpg321 human.mp3")
        time.sleep(audio_human.info.length)


    elif grabbed == '1' and state == 5:
        state = 6
        grabbed = '0'
        print('state6 entered')
        os.system("mpg321 hereur.mp3")
        time.sleep(audio9.info.length)

    elif message == 'thank_you_detected' and state == 6:
        state = 1
        pub3.publish("1")
        print('state1 entered')
        os.system("mpg321 welcome.mp3")
        time.sleep(audio_welcome.info.length)

    elif message == 'no_detected' and (state == 2 or state == 3 or state == 4):
        state = 1
        print('state1 entered')
        os.system("mpg321 else.mp3")
        time.sleep(audio6.info.length)

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
