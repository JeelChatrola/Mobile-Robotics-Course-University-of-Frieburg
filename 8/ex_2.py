import numpy as np
import matplotlib.pyplot as plt

def log_inv_sensor_model(z, c):
    if c > z - 10:
        
        return np.log(0.6 / (1 - 0.6))
    
    return np.log(0.3 / (1 - 0.3))


c = range(0, 201, 10)

logodds = np.zeros(len(c))

meas = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]

prior = np.log(0.5 / (1 - 0.5))
print("prior:", prior)

for i in range(len(meas)):
    for j in range(len(c)):
        
        if c[j] > meas[i] + 20:
            continue
        
        logodds[j] = logodds[j] - prior + log_inv_sensor_model(meas[i], c[j])


m = 1 - 1. / (1 + np.exp(logodds))

plt.plot(c, m)
plt.xlabel("x-position [cm]")
plt.ylabel("occupancy p(x)")
plt.savefig("graph.pdf")
plt.show()