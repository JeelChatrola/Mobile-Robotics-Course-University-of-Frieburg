import scipy
import numpy as np
import math
import matplotlib.pyplot as plt

######### EX-1 #########
def f(x):
    y = np.cos(x)*np.exp(x)  # np takes x as input in radians
    return  y

"""
x = float(input("Enter the value of x to calculate f(x) :"))
print("Solution of function is ",f(x))
"""

######### EX-2 #########
"""
x = np.arange(-2*np.pi,2*np.pi,0.01) # x values are stored in a array arange() function has three argument: Start,stop,step 

plt.plot(x,f(x))
plt.xlabel('x values from -2pi to 2pi')
plt.ylabel('f(x) = cos(x)*exp(x)')
plt.title('Plot of f(x) over interval -2pi to 2pi')
plt.legend(['f(x)'])

save_results_to = '/MOOC/Introduction to Mobile Robots - Uni of Frieberg/New folder/1/'
plt.savefig(save_results_to+'plot.jpg',dpi=300)
plt.show()
"""

########## EX-3 ############

#a
"""
x =np.random.normal(5, 2, size=(100000, 1))
print(x)
"""

#b
"""
y=np.random.uniform(0,10, size=(100000,1))
print(y)
"""

#c
"""
x=np.random.rand(2,1)

y=np.random.rand(3,1)

print(x)
print(y)

std_x =np.std(x)
std_y =np.std(y)

mean_x =np.mean(x)
mean_y =np.mean(y)

print(std_x,mean_x, "\n" ,std_y, mean_y)
"""

#d
"""
a=np.random.rand(1000, 1)
plt.hist(a,color='green', rwidth=0.5,alpha=0.8)
plt.show()

"""