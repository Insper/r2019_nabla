#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Veja soluções em:
# https://youtu.be/9YEUiWudyAU


from __future__ import print_function, division
import rospy
import numpy as np
import cv2
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3
import math

x = None
y = None

def recebe_odometria(data):
    global x
    global y

    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    print("Posicao do robo ", x, " ", y)


def desenha(cv_image, xs, ys):
    """
        Use esta funcão como exemplo de como desenhar na tela
    """
    # Usamos a função linha para desenhar um ponto
    cv2.line(cv_image,(xs-1,ys-1),(xs+1,ys+1),(255,0,0),5)


if __name__=="__main__":

    rospy.init_node("breadcrumbs")

    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )

    ref_odometria = rospy.Subscriber("/odom", Odometry, recebe_odometria)


    cv2.namedWindow("Saida")

    branco_bgr = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    # Cria uma imagem 512 x 512
    zero = (256, 256) # ponto considerado ponto zero

    fator = 50

    def escala(x,y):
        xs = x*fator+zero[0]
        ys = y*fator+zero[1]
        return int(xs), int(ys)


    while not rospy.is_shutdown():
        # Funcão que deve atualizar o desenho com as novas informacos de odometria
        
        xs, ys = escala(x,y)

        desenha(branco_bgr, xs, ys)

        # Imprime a imagem de saida
        cv2.imshow("Saida", branco_bgr)
        cv2.waitKey(40) # Esperar 40 millisegundos
        rospy.sleep(0.1)



