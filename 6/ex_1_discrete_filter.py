import numpy as np
import matplotlib.pyplot as plt
import time


def discrete_filter(bel, d):


    """Calculate new belief Bel(x).
    Arguments:
    bel -- current belief of robot position x
    d -- move command -1=backward, 1=forward
    See lecture on discrete filters slide 4 for details.
    """
    bel_prime = np.zeros(bel.shape[0])
    if d == 1:  # move forward
        for x in range(bel.shape[0]):
            if x >= 2:
                bel2 = bel[x-2]
            else:           
                bel2 = 0
        
            if x >= 1:
                bel1 = bel[x-1]
            else:
                bel1 = 0
            
            bel0 = bel[x]
        
            if x < bel.shape[0]-1:
                bel_prime[x] = 0.25*bel2+0.50*bel1+0.25*bel0
            
            elif x == bel.shape[0]-1:  # last cell
                bel_prime[x] = 0.25*bel2+0.75*bel1+1.00*bel0
        
    if d == -1:  # move backward
        for x in range(bel.shape[0]):
            if x < bel.shape[0]-2:
                bel2 = bel[x+2]
            else:
                bel2 = 0
    
            if x < bel.shape[0]-1:
                bel1 = bel[x+1]
            else:
                bel1 = 0
            
            bel0 = bel[x]
            
            if x > 0:
                bel_prime[x] = 0.25*bel2+0.50*bel1+0.25*bel0
            elif x == 0:  # first cell
                bel_prime[x] = 0.25*bel2+0.75*bel1+1.00*bel0
    
    return bel_prime


def plot_historgram(bel):

    plt.cla()
    plt.bar(range(0, bel.shape[0]), bel, width=1.0)
    plt.axis([0, bel.shape[0]-1, 0, 1])
    plt.draw()
    time.sleep(1)


def main():


    bel = np.hstack((np.zeros(10), 1, np.zeros(9)))
    plt.figure()
    plt.ion()
    plt.show()
    
    for i in range(0, 9):
        plot_historgram(bel)
        bel = discrete_filter(bel, 1)
        print(np.sum(bel))
    
    for i in range(0, 3):
        plot_historgram(bel)
        bel = discrete_filter(bel, -1)
        print(np.sum(bel))
    
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
