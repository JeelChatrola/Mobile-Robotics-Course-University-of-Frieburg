#! /usr/bin/env python3
# coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt
pi = math.pi

scan = np.loadtxt('./laserscan.dat')
angle = np.linspace(-pi/2,pi/2, np.shape(scan)[0], endpoint='true')

# getting x and y coordinates of laser scan values 
x = scan* np.cos(angle)
y = scan* np.sin(angle)

plt.plot(x,y,'.k',markersize=4)

plt.gca().set_aspect('equal', adjustable='box') # having same scale on both axes

plt.savefig('scan1.pdf')

global_frame_robot = np.array([[np.cos(pi/4), -np.sin(pi/4), 1], [np.sin(pi/4), np.cos(pi/4), 0.5],[0, 0, 1]])

laserscanner_frame = np.array([[np.cos(pi), -np.sin(pi), 0.2],[np.sin(pi), np.cos(pi), 0.0], [0, 0, 1]])

global_laser = np.dot(global_frame_robot,laserscanner_frame)

w = np.ones(len(x))
laser_scan = np.array([x,y,w])
global_scan = np.dot(global_laser,laser_scan)

plt.figure()
plt.plot(global_scan[0,:],global_scan[1,:],'.k',markersize=3)

plt.plot(global_frame_robot[0,2],global_frame_robot[1,2],'+r')
plt.plot(global_laser[0,2],global_laser[1,2],'+b')

plt.gca().set_aspect('equal')
plt.savefig('scan2.pdf')
plt.show()
