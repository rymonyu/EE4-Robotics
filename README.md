# EE4-Robotics
This Github project documents our work for the coursework of EE4-Human Centered Robotics 

# Graby

GRABY (Genuine Robust Assistant that Benefits You) is an assistance robot that targets the disabled person. It interacts with the user through an audio input i.e. speech, perform daily tasks for the disabled person, bringing convenience to improve the quality of life to such a minority group. The initial focus of the project is to limit the tasks to retrieving and returning items. This design report aims to describe the hypotheses, high-level design, the algorithm used and validation to better illustrate the effectiveness of the robot in improving lives.  

<br>
<br>

## Design Overview

GRABY is split into 4 core modules, interconnected using the Robot Operating System (ROS) framework. These modules include: Vision, Speech, Navigation and Control, are used to interact, process, detect and respond to each task. Each of these core modules is further split into sub-modules as detailed in the system diagram [Fig.1].

The primary form of interaction is voice communication where the user commands GRABY to “Grab something”. GRABY then responds to the task with a facial expression on the screen to further enhance user experience. Depending on the task assigned, GRABY will perform a myriad of tasks including navigation, object detection and arm trajectory movements.



## Work Distribution
Navigation: Vincent Luo, Che Zhang<br>
Speech Recognition: Haojun Zhang, JinMing Hu <br>
Vision: Rymon Yu, Yuzhuo Tan <br>
Robotics Arm Control: Rymon Yu  <br>
ROS: Vincent Luo, Rymon Yu  <br>
