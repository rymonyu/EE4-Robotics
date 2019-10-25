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

# Baxter_Ridgeback
This is a guidance of setting up network and ROS for baxter robot on ridgeback. Baxter is ethernet wired to lab internet. Ridgeback is wifi connected. As we cannot change code on Baxter, we have to modify Ridgeback to use Baxter ROScore.

### Ridgeback only network setup:
In PC bash file:
1. export ROS_MASTER_URI=http://cpr-ridgeback-0001:11311
2. export ROS_IP=10.0.0.XXX  # Your PC's wireless IP address

Add in /etc/hosts file:
1. 10.0.0.XXX cpr-ridgeback-0001
2. 10.0.0.XXX CPR-R100-0065

### Ridgeback-Baxter ROS setup:
1. SSH into Ridgeback (ssh administrator@10.0.0.157  password:clearpath)
2. sudo service ros stop
3. cd ./baxter_ws/
4. ./baxter.sh
5. roslaunch ridgeback_base base.launch
6. roslaunch ridgeback_bringup accessories.launch

For more information, please look:
1. Tutorial    https://www.clearpathrobotics.com/assets/guides/ridgeback/index.html
2. Network     https://github.com/ibaranov-cp/baxter_ridgeback

### Acknowledgement:
Dr. Tobias Fischer, Rodrigo Chacon Quesada, and Fan Zhang have spent time on setting up network and ROS, tuning parameters for navigation.

### Finally:
To whoever will use the robot later, follow the commands above and the websites provided for tutorial. 



## Work Distribution
Navigation: Vincent Luo, Che Zhang, JinMing Hu, Haojun Zhang <br>
Speech Recognition: Haojun Zhang, JinMing Hu <br>
Vision + Classification: Rymon Yu, Yuzhuo Tan <br>
Robotics Arm Control: Rymon Yu  <br>
ROS: Vincent Luo, Rymon Yu  <br>
Report: Che Zhang  <br>
