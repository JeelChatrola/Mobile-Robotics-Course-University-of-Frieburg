# !/usr/bin/env python
import math
import matplotlib.pyplot as plt
import numpy as np
import ex1 as snd


def func_motion_model(x,u,alpha):
    delta_hat_rot1 = u[0] + snd.func_normal_sampling(0, alpha[0]*abs(u[0]) + alpha[1]*abs(u[2]))
    delta_hat_rot2 = u[1] + snd.func_normal_sampling(0, alpha[0]*abs(u[1]) + alpha[1]*abs(u[2]))
    delta_hat_trans = u[2] + snd.func_normal_sampling(0, alpha[2]*abs(u[2]) + alpha[3]*(abs(u[0])+abs(u[1])))

    x_prime = x[0] + delta_hat_trans * math.cos( x[2] + delta_hat_rot1)
    y_prime = x[1] + delta_hat_trans * math.sin( x[2] + delta_hat_rot1)
    theta_prime = x[2] + delta_hat_rot1 + delta_hat_rot2

    return np.array([x_prime,y_prime,theta_prime])


def main():

    x = [2, 4, 0]
    u = [np.pi/2, 0, 1]
    alpha = [0.1, 0.1, 0.01, 0.01]
   
    num_samples = 5000
    x_prime = np.zeros([num_samples, 3])
    
    for i in range(0, num_samples):
        x_prime[i,:] = func_motion_model(x,u,alpha)

    plt.plot(x[0], x[1], "bo")
    plt.plot(x_prime[:,0], x_prime[:,1], "r,")
    plt.xlim([1, 3])
    plt.axes().set_aspect('equal')
    
    plt.xlabel("x-position [m]")
    plt.ylabel("y-position [m]")
    plt.savefig("odometry_samples.pdf")
    plt.show()

if __name__ == "__main__":
    main()