# EE4-Robotics
This Github project documents our work for the coursework of EE4-Human Centered Robotics 

# Kris The Robot 
## Objectives
* Detects item </n>
```shell
This could pontentially involve SLAM where we need to perform mapping and mark object location on the map.
The lab offers Lidar sensor to perform SLAM implementations, however VSLAM could also be considered using RGB-D camera and IMU.
Performance needs to be tested and compared.
Does the robot detects garbage and move OR Does the robot move and detects garbage on its route

```
* Classify item </n>
```shell
Using torchvision pre-trained model (FasterRCNN / MaskRCNN / Others) + openCV
Use GPU accelerations CUDA + cudnn and try TensorRT if using tensorflow
```
* Collect item </n>
```shell
Control joints with ROS/Robot packages after object localisation
```

* Navigate to item </n>
```shell
Navigation 
```

## Architecture
Master
> * Laptop/Nvidia TX2

Middleware
> * ROS Framework wired/wifi

Remote Servers
> * ABB YuMi?
>
> * PLC if already embedded within the robot

## Docker
Linux Ubuntu 16.04 <br>
ROS Kinetic <br>


## Work Distribution
Navigation: Vincent Luo, Che Zhang, JinMing Hu, Haojun Zhang <br>
Speech Recognition: Haojun Zhang, JinMing Hu <br>
Vision + Classification: Rymon Yu, Yuzhuo Tan <br>
Robotics Arm Control: Rymon Yu  <br>
ROS: Vincent Luo, Rymon Yu  <br>
Report: Che Zhang  <br>
