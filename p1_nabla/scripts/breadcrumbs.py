#! /usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function, division
import rospy
import numpy as np
import cv2
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3
import math

def recebe_odometria(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    print("Posicao do robo ", x, " ", y)


def desenha(cv_image):
    """
        Use esta funcão como exemplo de como desenhar na tela
    """
    cv2.circle(cv_image,(256,256),64,(0,255,0),2)
    cv2.line(cv_image,(256,256),(400,400),(255,0,0),5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_image,'Boa sorte!',(0,50), font, 2,(255,255,255),2,cv2.LINE_AA)

if __name__=="__main__":

    rospy.init_node("breadcrumbs")

    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )

    ref_odometria = rospy.Subscriber("/odom", Odometry, recebe_odometria)


    cv2.namedWindow("Saida")

    branco_bgr = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    # Cria uma imagem 512 x 512
    zero = (256, 256) # ponto considerado ponto zero

    while not rospy.is_shutdown():
        # Funcão que deve atualizar o desenho com as novas informacos de odometria
        desenha(branco_bgr)
        # Imprime a imagem de saida
        cv2.imshow("Saida", branco_bgr)
        cv2.waitKey(40) # Esperar 40 millisegundos
        rospy.sleep(0.1)



