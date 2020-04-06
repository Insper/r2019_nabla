#! /usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function, division


import rospy

import numpy as np


from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Imu
from tf import transformations
import math

angulos = [0,0,0]

def leu_imu(dado):
	global angulos
	quat = dado.orientation
	lista = [quat.x, quat.y, quat.z, quat.w]
	angulos = np.degrees(transformations.euler_from_quaternion(lista))
	mensagem = """
	Tempo: {:}
	Orientação: {:.2f}, {:.2f}, {:.2f}
	Vel. angular: x {:.2f}, y {:.2f}, z {:.2f}\

	Aceleração linear:
	x: {:.2f}
	y: {:.2f}
	z: {:.2f}


""".format(dado.header.stamp, angulos[0], angulos[1], angulos[2], dado.angular_velocity.x, dado.angular_velocity.y, dado.angular_velocity.z, dado.linear_acceleration.x, dado.linear_acceleration.y, dado.linear_acceleration.z)
	# print(mensagem)

	


if __name__=="__main__":

	rospy.init_node("le_imu")

	recebe_scan = rospy.Subscriber("/imu", Imu, leu_imu)
	pub = rospy.Publisher("/cmd_vel", Twist)

	while not rospy.is_shutdown():
		print("Main loop")
		vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
		
		
		if angulos[1] > 1:
			vel = Twist(Vector3(1.0,0,0), Vector3(0,0,0))
			print ("Inclinado para frente ", angulos[1])
		elif angulos[1] < -1:
			vel = Twist(Vector3(-1.0,0,0), Vector3(0,0,0))
			print("Inclinado para trás ", angulos[1])
		else:
			print("Nivelado")
		pub.publish(vel)		
		rospy.sleep(0.5)

