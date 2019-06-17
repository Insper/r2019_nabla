
### Gazebo Turtlebot

Certifique-se de que seu `.bashrc` têm as variáveis `ROS_IP` e `ROS_MASTER_URI` desabilitadas antes de rodar o Gazebo


Você pode iniciar o Gazebo usando **uma** das opções:

    roslaunch turtlebot3_gazebo turtlebot3_stage_4.launch

    roslaunch turtlebot3_gazebo turtlebot3_stage_1.launch

    roslaunch turtlebot3_gazebo turtlebot3_stage_2.launch

    roslaunch turtlebot3_gazebo turtlebot3_stage_3.launch

    roslaunch turtlebot3_gazebo turtlebot3_house.launch

    roslaunch turtlebot3_gazebo turtlebot3_world.launch

O Gazebo já abre um `roscore` implicitamente




Executar `catkin_make` após fazer o download do projeto: 

    cd ~/catkin_ws/
    catkin_make


Certifique-se de que seus scripts Python são executáveis

    roscd p1_nabla
    cd scripts
    chmod a+x *py

Para executar, faça:

    rosrun p1_nabla breadcrumbs.py


Certifique-se de que seus scripts ROS rodam com Python 2 e têm sempre as linhas a seguir no começo:

    #! /usr/bin/env python
    # -*- coding:utf-8 -*-

