import pyrealsense2 as rs
import torchvision
import torch
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
# geometry_msgs/Point.msg
from std_msgs.msg import Float64
from std_msgs.msg import String
import rospkg
# Import Numpy for easy array manipulation
import numpy as np
import sys

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# Import OpenCV for easy image rendering
import cv2
# import matplotlib.pyplot as plt
# from PIL import Image
from torchvision import transforms
import _thread
import threading
import time


print("Torch CUDA Version: ", torch.version.cuda)
print("Torch Cudnn Version: ", torch.backends.cudnn.version())
use_gpu = torch.cuda.is_available()
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
if (use_gpu):
    print("Use GPU?: ", use_gpu)

    model = model.cuda()

print("Is Torch Cuda available: ", torch.cuda.is_available())
print("Current Cuda Device being used: ", torch.cuda.current_device())

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Create a pipeline
pipeline = rs.pipeline()

# Create a config and configure the pipeline to stream
#  different resolutions of color and depth streams
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = config.resolve(pipeline)
# Start streaming
profile = pipeline.start(config)
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth scale: ", depth_scale)

align_to = rs.stream.color
align = rs.align(align_to)


rospy.init_node('Robert', anonymous=True)

pub = rospy.Publisher('Coordinates', Point, queue_size=10)

message = Point()

pickarrival = False
processing = False
goal = None

def callback(data):
    global goal, processing
    print("im in callback1")
    rospy.loginfo(rospy.get_caller_id() + "I need to grab = %s", data.data)
    goal = data.data
    print("goal: ",goal)
    if goal == 'bottle':
        processing = True
    if goal == 'coffee':
        goal = 'cup'
        processing = True

def callback3(data):
    global pickarrival
    print("im in callback3")
    if (data.data == "2"):
        pickarrival = True


def listener2():
    global goal, processing
    rospy.Subscriber("arrived", String, callback3)
    #print("Subscriber built")
    r = rospy.Rate(1)
    r.sleep()

def listener():
    global goal, processing
    rospy.Subscriber("output", String, callback)
    #rospy.Subscriber("arrived", String, callback3)
    #print("Subscriber built")
    r = rospy.Rate(1)
    r.sleep()





def pos(obj):

    xold = 0
    yold = 0
    zold = 0

    xlist = []
    ylist = []
    zlist = []

    for a in range(25):
        frames = pipeline.wait_for_frames()
        # frames.get_depth_frame() is a 640x360 depth image

        # Align the depth frame to color frame
        aligned_frames = align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame()  # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            continue

        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        transform = transforms.Compose([transforms.ToTensor()])  # Defining PyTorch Transform
        img = transform(color_image)  # Apply the transform to the image
        img = img.cuda()
        pred = model([img])  # Pass the image to the model
        pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in
                      list(pred[0]['labels'].cpu().numpy())]  # Get the Prediction Score

        pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in
                      list(pred[0]['boxes'].detach().cpu().numpy())]  # Bounding boxes
        pred_score = list(pred[0]['scores'].detach().cpu().numpy())
        # pred_t = [pred_score.index(x) for x in pred_score if x > 0.5][-1]  # Get list of index with score greater than threshold.
        pred_index = [pred_score.index(x) for x in pred_score if x > 0.5]
        # print(np.array(pred_index).shape)
        if (len(pred_index) != 0):
            pred_t = pred_index[-1]

            pred_boxes = pred_boxes[:pred_t + 1]

            pred_class = pred_class[:pred_t + 1]

            if (obj in pred_class):
                for i in range(len(pred_boxes)):
                    if (pred_class[i] == obj)&(obj == 'cup'):
                        val = pred_boxes[i][0][0].item()
                        y_val = pred_boxes[i][0][1].item()
                        val2 = pred_boxes[i][1][0].item()
                        y_val2 = pred_boxes[i][1][1].item()
                        diff = (val + val2) / 2
                        y_diff = (y_val + y_val2) / 2
                        y = int(round(y_diff))
                        x = int(round(val))
                        x1 = int(round(diff))

                        depth = depth_image[y, x1].astype(float)
                        z = depth * depth_scale
                        print("CUP Z:", z)
                        if (-3.0 < (x - xold) < 3.0):
                            xlist.append(x)
                        if (-3.0 < (y - yold) < 3.0):
                            ylist.append(y)
                        if (-0.005 < (z - zold) < 0.005) & (z!= 0):
                            if(a >= 2):
                                zlist.append(z)

                        # cv2.rectangle(color_image, pred_boxes[i][0], pred_boxes[i][1], color=(0, 255, 0),
                        #               thickness=2)  # Draw Rectangle with the coordinates
                        # cv2.putText(color_image, pred_class[i], pred_boxes[i][0], cv2.FONT_HERSHEY_SIMPLEX, 2,
                        #             (0, 255, 0),
                        #             thickness=2)  # Write the prediction class
                        xold = x
                        yold = y
                        zold = z

                    elif (pred_class[i] == obj):
                        val = pred_boxes[i][0][0].item()
                        y_val = pred_boxes[i][0][1].item()
                        val2 = pred_boxes[i][1][0].item()
                        y_val2 = pred_boxes[i][1][1].item()
                        diff = (val + val2) / 2
                        y_diff = (y_val + y_val2) / 2
                        y = int(round(y_diff))
                        x = int(round(diff))
                        depth = depth_image[y, x].astype(float)
                        z = depth * depth_scale
                        # print("x coordinate:", x)
                        # print("y coordinate:", y)
                        # print("z coordinate:", distance)
                        if (-3.0 < (x - xold) < 3.0):
                            xlist.append(x)
                        if (-3.0 < (y - yold) < 3.0):
                            ylist.append(y)
                        if (-0.005 < (z - zold) < 0.005) & (z!= 0):
                            if(a >= 2):
                                zlist.append(z)

                        cv2.rectangle(color_image, pred_boxes[i][0], pred_boxes[i][1], color=(0, 255, 0),
                                      thickness=2)  # Draw Rectangle with the coordinates
                        cv2.putText(color_image, pred_class[i], pred_boxes[i][0], cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (0, 255, 0),
                                    thickness=2)  # Write the prediction class
                        xold = x
                        yold = y
                        zold = z

        # cv2.namedWindow('Align Example', cv2.WINDOW_AUTOSIZE)
        # cv2.imshow('Align Example', color_image)
        # key = cv2.waitKey(1)
        # #Press esc or 'q' to close the image window
        # if key & 0xFF == ord('q') or key == 27:
        #     cv2.destroyAllWindows()
        #     pipeline.stop()
        #     break
    print("xlist:", xlist)
    print("ylist:", ylist)
    print("zlist:", zlist)
    posx = np.mean(xlist)
    posy = np.mean(ylist)
    posz = np.mean(zlist)

    # if (obj == 'bottle'):
    #     message.x = posz + 0.17
    #     message.z = 0.079425
    #     if(message.x >= 0.8):
    #         if (posx > 320):
    #             temp = (posx - 320) / 320
    #             message.y = -(0.01 + (temp * 0.25))
    #         else:
    #             temp = (320 - posx) / 320
    #             message.y = (0.01 + temp * 0.25)
    #     else:
    #         if (posx > 320):
    #             temp = (posx - 320) / 320
    #             message.y = -(0.02 + (temp * 0.1))
    #         else:
    #             temp = (320 - posx) / 320
    #             message.y = (0.02 + temp * 0.1)


    if(obj == 'cup'):
        message.x = posz + 0.17
        message.z = -0.05
        if (posx > 320):
            temp = (posx - 320) / 320
            message.y = -(0.01 + temp*0.2)
        else:
            temp = (320 - posx) / 320
            message.y = 0.01 + temp*0.2

    if(obj == 'bottle'):
        message.x = posz + 0.17
        message.z = 0.079425
        if (posx > 320):
            temp = (posx - 320) / 320
            message.y = -(0.01+(temp*0.25))
        else:
            temp = (320 - posx) / 320
            message.y = (0.01+temp*0.25)

    pub.publish(message)

    return posx, posy, posz


def process():
    val_last = 0
    while True:
        frames = pipeline.wait_for_frames()
        # frames.get_depth_frame() is a 640x360 depth image

        # Align the depth frame to color frame
        aligned_frames = align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame()  # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            continue

        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # img = Image.open(img_path)  # Load the image
        # print("i need to transform image")
        transform = transforms.Compose([transforms.ToTensor()])  # Defining PyTorch Transform
        img = transform(color_image)  # Apply the transform to the image
        img = img.cuda()
        # print("passing to model")
        pred = model([img])  # Pass the image to the model
        pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in
                      list(pred[0]['labels'].cpu().numpy())]  # Get the Prediction Score

        # print("Original class length:")
        # print(len(pred_class))
        pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in
                      list(pred[0]['boxes'].detach().cpu().numpy())]  # Bounding boxes
        pred_score = list(pred[0]['scores'].detach().cpu().numpy())
        # pred_t = [pred_score.index(x) for x in pred_score if x > 0.5][-1]  # Get list of index with score greater than threshold.
        pred_index = [pred_score.index(x) for x in pred_score if x > 0.5]
        # print(np.array(pred_index).shape)
        if (len(pred_index) != 0):
            pred_t = pred_index[-1]
            # print (pred_t)
            # print("ok!")

            pred_boxes = pred_boxes[:pred_t + 1]

            pred_class = pred_class[:pred_t + 1]

            # if(len(pred_class) != 0):
            if ('teddy bear' in pred_class):
                # print("PERSON")
                # forwardmessage.publish(forward)
                for i in range(len(pred_boxes)):
                    if (pred_class[i] == 'teddy bear'):
                        val = pred_boxes[i][0][0].item()
                        y_val = pred_boxes[i][0][1].item()
                        val2 = pred_boxes[i][1][0].item()
                        y_val2 = pred_boxes[i][1][1].item()
                        diff = (val + val2) / 2
                        y_diff = (y_val + y_val2) / 2
                        y = int(round(y_diff))
                        x = int(round(diff))

                        depth = depth_image[y, x].astype(float)
                        distance = depth * depth_scale
                        print("x coordinate:", x)
                        print("y coordinate:", y)
                        print("z coordinate:", distance)
                        # message.x = x
                        # message.y = y
                        # message.z = distance
                        # pub.publish(message)
                        # dif = val_last - val
                        # if(diff < 280.0):
                        #     print("moved left")
                        #     pub.publish(left)
                        # 444444
                        # if(diff > 380.0):
                        #     print("moved right")
                        #     pub.publish(right)
                        #
                        # if(280.0 < diff < 380.0):
                        #     print("straight")
                        #     pub.publish(0.0)

                        # val_last = val
                        #rate.sleep()

                        cv2.rectangle(color_image, pred_boxes[i][0], pred_boxes[i][1], color=(0, 255, 0),
                                      thickness=2)  # Draw Rectangle with the coordinates
                        cv2.putText(color_image, pred_class[i], pred_boxes[i][0], cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (0, 255, 0),
                                    thickness=2)  # Write the prediction class


            #else:
                # forwardmessage.publish(0.0)
                # pub.publish(none)
                # rate.sleep()

        #else:
            # forwardmessage.publish(0.0)
            # pub.publish(none)
            # rate.sleep()

        cv2.namedWindow('Align Example', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('Align Example', color_image)
        key = cv2.waitKey(1)
        # Press esc or 'q' to close the image window
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            pipeline.stop()
            break


def main():
    global processing, goal, pickarrival
    listener()
    listener2()

    # while not rospy.is_shutdown():
    #     if (processing == False):
    #         print("Waiting for input...")
    #     else:
    #         thing = goal
    #         print("thing:", thing)
    #         # if(thing == "coffee"):
    #         #     thing = "cup"
    #         #     print("THING:", thing)
    #         x, y, z = pos(thing)
    #         print("x: ", x)
    #         print("y: ", y)
    #         print("z: ", z)
    #         processing = False

    while not rospy.is_shutdown():



        if(processing == False):
            print("Waiting for input...")

        else:
            if(pickarrival == False):
                print("Waiting to arrive at desk")

            else:
            #thing = input("What would you like: ")
            #print(thing)
            #x,y,z = pos(thing)
                thing = goal
                print("thing:", thing)
                # if(thing == "coffee"):
                #     thing = "cup"
                #     print("THING:", thing)
                x,y,z = pos(thing)
                print("x: ", x)
                print("y: ", y)
                print("z: ", z)
                processing = False
                pickarrival = False

#process()
main()
