import numpy as np
import matplotlib.pyplot as plt
#a

def diffdrive(x, y, theta,v_l, v_r, t, l):

    if (v_l == v_r):
        theta_n = theta
        x_n = x + v_l*t*np.cos(theta)
        y_n = y + v_l*t*np.sin(theta)
    
    else:    
        r = (l/2)*((v_l+ v_r)/(v_r-v_l))

        ICC_x = x - r*np.sin(theta)
        ICC_y = y + r*np.cos(theta)
        
        omega = (v_r - v_l)/l
        
        dtheta = omega*t

        x_n = (x - ICC_x)*np.cos(dtheta) - (y - ICC_y)*np.sin(dtheta) + ICC_x
        y_n = (x - ICC_x)*np.sin(dtheta) + (y - ICC_y)*np.cos(dtheta) + ICC_y
        theta_n = theta + dtheta
        
    return x_n,y_n,theta_n
    
#b
x = 1.5
y = 2.0
theta = (np.pi)/2
l = 0.5

plt.quiver(x,y,np.cos(theta),np.sin(theta))


#first command
v_l = 0.3
v_r = 0.3
t = 3.0

x,y,theta = diffdrive(x,y,theta,v_l,v_r,t,l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after first command: x: %f, y: %f,theta: %f"% (x,y,theta))

#second command
v_l = 0.1
v_r = -0.1
t = 1.0

x,y,theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after second command: x: %f, y: %f,theta: %f" % (x,y,theta))

# third command
v_l = 0.2
v_r = 0.0
t = 2

x,y,theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after third command: x: %f, y: %f,theta: %f" % (x,y,theta))

plt.show()
