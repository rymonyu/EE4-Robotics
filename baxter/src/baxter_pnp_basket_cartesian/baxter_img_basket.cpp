// Copyright (C) 2017 Maik Heufekes, 05/07/2017.
// License, GNU LGPL, free software, without any warranty.

#include "ros/ros.h"
#include "sensor_msgs/Image.h"
#include <sstream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <cmath>
#include <geometry_msgs/PoseArray.h>
#include <geometry_msgs/Pose.h>
#define uchar unsigned char
#define _r(x, y, image) ((uchar *)((image)->imageData + ((image)->widthStep) * (x)))[3 * y + 2]
#define _g(x, y, image) ((uchar *)((image)->imageData + ((image)->widthStep) * (x)))[3 * y + 1]
#define _b(x, y, image) ((uchar *)((image)->imageData + ((image)->widthStep) * (x)))[3 * y]
#define _Ma(x, y, mat) ((mat)->data.fl + (mat)->step / 4 * (x))[y]

using namespace cv;
uchar *temp;
int flag = 1;
int size_ = 0;
char name[30]; 
IplImage *head;
IplImage *left_hand;
IplImage *right_hand;
IplImage *red;
IplImage *green;
IplImage *blue;
IplImage *src_result;

CvMat *TRANS = cvCreateMat(3, 3, CV_32FC1);
CvMat *INVTRANS = cvCreateMat(3, 3, CV_32FC1);
CvMat *DIS = cvCreateMat(1, 4, CV_32FC1);
int WIDTH, HEIGHT, STEP;
int NUM_OBJ = 0;

// Low hsv values for pink colors.
uchar COLOR_pink_low[3] = {160, 93, 25}; 
// High hsv values for pink values.
uchar COLOR_pink_high[3] = {179, 210, 230};

extern void GetPosition(IplImage *, uchar*, uchar*, int num);
extern int GetColor(IplImage *);
extern void FilterColor(IplImage *, IplImage *, uchar *, uchar *);

ros::Publisher pos_pub;
// The center postion and size of object in image frame.
typedef struct pos 
{
  int x, y;
  float angle;
  float size;
}pos;
// The center position and size of one object in world frame.
typedef struct re_pos 
{
  float x, y, z;
  float angle;
  int flag;
  float size;
}pos_;

// Convert the coordinate from the image frame to world frame.
extern void Get3DPos(pos *src, pos_ *dis);
// Get object center position in world frame which called by Get3DPos.
extern void GetRealPos(float, float, float, float, float, float, float, float, pos_*);
// Buffer for obj pos in img frame.
pos *pos_head = (pos *)malloc(sizeof(pos) * 100);
// Buffer for the points pos in world frame.
pos_ *rel_pos = (pos_ *)malloc(sizeof(pos_) * 100);
// Convert image topic data into IplImage data structure.
void ImageToIpl(uchar *src, IplImage *dis)
{
  for(int i = 0; i != HEIGHT; i ++)
  {
    for(int j = 0; j != WIDTH; j++)
    {
      ((uchar *)(dis->imageData) + (dis->widthStep) * i)[3 * j] = src[dis->widthStep / 3 * 4 * i + 4 * j + 0];
      ((uchar *)(dis->imageData) + (dis->widthStep) * i)[3 * j + 1] = src[dis->widthStep / 3 * 4 * i + 4 * j + 1];
      ((uchar *)(dis->imageData) + (dis->widthStep) * i)[3 * j + 2] = src[dis->widthStep / 3 * 4 * i + 4 * j + 2];    
    }
  }
}

// Subscriber call back function.
void ImageCallBack(const sensor_msgs::Image &msg)
{
  if (flag == 1)
  {
    // Set the global parameters for the image.
    WIDTH = msg.width;
    HEIGHT = msg.height;
    STEP = msg.step;
    size_ = msg.step * msg.height;
    temp = (uchar *)malloc(size_);
    flag ++;
    head = cvCreateImage(cvSize(msg.width, msg.height), IPL_DEPTH_8U, 3);
    red = cvCreateImage(cvSize(msg.width, msg.height), IPL_DEPTH_8U, 3);
    green = cvCreateImage(cvSize(msg.width, msg.height), IPL_DEPTH_8U, 3);
    blue = cvCreateImage(cvSize(msg.width, msg.height), IPL_DEPTH_8U, 3);
    src_result = cvCreateImage(cvSize(msg.width, msg.height), IPL_DEPTH_8U, 3);
  }
  for(int i = 0; i != size_; i++)
  {
    temp[i] = msg.data[i];
  }
  ImageToIpl(temp, head);
  src_result = cvCloneImage(head);
  GetPosition(head, COLOR_pink_low, COLOR_pink_high, 1);
  geometry_msgs::PoseArray points;
  geometry_msgs::Pose pose;
  for(int i = 0; i != NUM_OBJ; i++)
  {
    // Assign values to pose and add offsets (in cm) to get the position 
    // in the baxter coordinate system (blue).
    pose.position.x = rel_pos[i].x / 1000+0.07+0.57-0.015;
    pose.position.y = rel_pos[i].y / 1000-0.032;
    pose.position.z = rel_pos[i].angle;
    pose.orientation.x = rel_pos[i].size; 
    // Publish the obj pos and orientation and size.
    points.poses.push_back(pose);
  }
  // src_result is the image with the lined circle around the basket.
  //cvShowImage("detected basket", src_result);
  //cvSaveImage("/home/maik/Schreibtisch/save/detected basket.jpg", src_result);
  pos_pub.publish(points);
}

int main(int arg, char** argv)
{  
  // The Intrinsic Matrix (calibration paramter)
  // Focal length: fx
  _Ma(0, 0, TRANS) = 411.78954;	
  _Ma(0, 1, TRANS) = 0;
  // Principal point offset: cx
  _Ma(0, 2, TRANS) = 307.70709;	
  _Ma(1, 0, TRANS) = 0;
  // Focal length: fy
  _Ma(1, 1, TRANS) = 411.10182;
  // Principal point offset: cy
  _Ma(1, 2, TRANS) = 236.83502;
  _Ma(2, 0, TRANS) = 0;	
  _Ma(2, 1, TRANS) = 0;
  _Ma(2, 2, TRANS) = 1;  
  // The inverse of the parameter matrix.   
  _Ma(0, 0, INVTRANS) = 0.0022042;
  _Ma(0, 1, INVTRANS) = 0;
  _Ma(0, 2, INVTRANS) = -0.74724;
  _Ma(1, 0, INVTRANS) = 0;
  _Ma(1, 1, INVTRANS) = 0.0022049;
  _Ma(1, 2, INVTRANS) = -0.57610;
  _Ma(2, 0, INVTRANS) = 0;
  _Ma(2, 1, INVTRANS) = 0;
  _Ma(2, 2, INVTRANS) = 1;
  // The distortion matrix.
  _Ma(0, 0, DIS) = 0.01386;
  _Ma(0, 1, DIS) = -0.058;
  _Ma(0, 2, DIS) = 0.00134;
  _Ma(0, 3, DIS) = 0.00227;
 
  ros::init(arg, argv, "test");
  ros::NodeHandle n;
  pos_pub = n.advertise<geometry_msgs::PoseArray>("detected_basket", 2);
  ros::Subscriber sub = n.subscribe("/cameras/right_hand_camera/image", 1, ImageCallBack);
  ros::spin();
  return 0;
}

// Get object center position in world frame which called by Get3DPos.
void GetPosition(IplImage *src, uchar* COLOR, uchar* COLOR_, int num)
{
  IplImage *temp_ = cvCreateImage(cvGetSize(src), IPL_DEPTH_8U, 3);
  IplImage *src_copy = cvCreateImage(cvGetSize(src), IPL_DEPTH_8U, 3);
  IplImage *gray_ = cvCreateImage(cvGetSize(src), IPL_DEPTH_8U, 1);
  IplImage *con = cvCreateImage(cvGetSize(src), IPL_DEPTH_8U, 1);
  IplImage *con_;
  // Copy the original image to use for every color the same one.
  src_copy = cvCloneImage(src);
  NUM_OBJ = 0;
  // Do the gaussian filtering for the noise.
  cvSmooth(src_copy, src_copy, CV_GAUSSIAN, 5, 5);
  // Pick up the object and make everything else black.
  FilterColor(src_copy, blue, COLOR, COLOR_);
  /*
  // The variable num is only for looking at one specific color (example: green=2)
  if (num==1){
      cvSaveImage("/home/maik/Schreibtisch/save/black.jpg", blue );
      }
  */
  // Remove the little holes on the object.
  cvErode(blue, temp_, NULL, 4);
  IplImage *gray = cvCreateImage(cvGetSize(src_copy), IPL_DEPTH_8U, 1);
  // Convert coloful img into mono.
  cvCvtColor(temp_, gray, CV_BGR2GRAY);
  // Convert the mono image into binary image.
  cvThreshold(gray, gray_, 20, 255, CV_THRESH_BINARY);
  con_ = cvCloneImage(gray_);
  CvMemStorage *st = cvCreateMemStorage(0);
  CvSeq *first = NULL;
  // Find the connective areas in the image.
  cvFindContours(con_, st, &first, sizeof(CvContour), CV_RETR_LIST);
  // CvSeq is a dynamic data structures to represent growable 1d arrays.
  for(CvSeq *c = first; c != NULL; c = c->h_next) 
  {
    CvPoint2D32f center;
    float radius=0;
    // Use a circle to fit the connective area.
    cvMinEnclosingCircle(c, &center, &radius);
    // Ignore very small and very big objects.
    if(radius>90){
            //printf("Radius: %f \n", radius);
	    CvPoint cent;
	    cent.x=center.x;
	    cent.y=center.y;
	    CvScalar color_frame = CV_RGB(0, 0, 0);
	    cvCircle(src_result, cent, radius, color_frame, 3, 8, 0 );
            // Assume that the real center is the same like the center of the image.
            pos_head[NUM_OBJ].x = (int) center.x- WIDTH / 2; 
            pos_head[NUM_OBJ].y = -((int) center.y- HEIGHT / 2);   
            // The diameter of the circle in pixels.
            pos_head[NUM_OBJ].size = radius*2;
            // Get the world frame postions.
            Get3DPos(pos_head + NUM_OBJ, rel_pos + NUM_OBJ); 
            NUM_OBJ++; 
	}
  }
  waitKey(1);
  // Release the memory we have malloced.
  cvReleaseMemStorage(&st); 
  cvReleaseImage(&gray);
  cvReleaseImage(&temp_);
  cvReleaseImage(&gray_);
  cvReleaseImage(&src_copy);
  cvReleaseImage(&con);
  cvReleaseImage(&con_);
  //ROS_INFO("Detect [%d] objects", NUM_OBJ);
}

// Filter the color.
void FilterColor(IplImage *src, IplImage *dis, uchar* COLOR, uchar* COLOR_)
{
 IplImage *temp_ = cvCreateImage(cvGetSize(src), IPL_DEPTH_8U, 3);
 cvCvtColor(src, temp_, CV_BGR2HSV);
  for(int i = 0; i != src->height; i++)
  {
    for(int j = 0; j != src->width; j++)
    {
      if(COLOR[0] <= _b(i, j, temp_) && COLOR_[0] >= _b(i, j,temp_) && COLOR[1] <= _g(i, j, temp_) && COLOR_[1] >= _g(i, j, temp_) && COLOR[2] <= _r(i, j, temp_) && COLOR_[2] >= _r(i, j, temp_))
      {
        _r(i, j, dis) = _r(i, j, src);
        _g(i, j, dis) = _g(i, j, src);
        _b(i, j, dis) = _b(i, j, src);
      }
      else
      {
         _r(i, j, dis) = 0;
         _g(i, j, dis) = 0;
         _b(i, j, dis) = 0;
      }
    }
  }
  cvReleaseImage(&temp_);
}

void Get3DPos(pos *src, pos_ *dis)
{
  // The factors 0.015 and 0.058 correct the small deviations from (int) rect.center.x- WIDTH / 2
  // and -((int) rect.center.y- HEIGHT / 2).
  float tempx = _Ma(0, 0, INVTRANS) * src->x + 0.015;  _Ma(0, 2, INVTRANS);
  float tempy = _Ma(1, 1, INVTRANS) * src->y + 0.058;  _Ma(1, 2, INVTRANS);
  // 315 mm is the distance from the camera to the basket
  GetRealPos(tempx, tempy, 0, 0, 1.0, 0, 1, 315, dis);
  dis->angle = src->angle;
  dis->flag = 1;
  // The sizes of the circles must be converted from pixels in cm in the real world.
  // real_size= image_size*(z/f), z: distance between camera and object, f: focal length
  // z/f=31,5/411.8= 0.076493 but the size of the detected objects is allways a bit smaller. 
  // This is the reason for the adjustment of the parameter (calculation in readme).
  dis->size = (src->size)*0.08;
}

void GetRealPos(float x, float y, float xz, float yz, float zz, float xp, float yp, float zp, pos_ *dis) 
  // xp ...zp is the coordinate of one point on the table, and the xz ...zz is the orientation of 
  // the  normal vector of the table, both of them are represented in the camera frame.
{
  // here x*zp. 
  dis->y = x * (xp * xz + yp * yz + zp * zz) / (x * xz + y * yz + zz); 
  // here -y*zp.
  dis->x = -y * (xp * xz + yp * yz + zp * zz) / (x * xz + y * yz + zz);
  // here zp.
  dis->z = -(-xp * xz - yp * yz -zp * zz) / (x * xz + y * yz + zz); 
}


