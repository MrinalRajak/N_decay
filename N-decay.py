

import numpy as np
import random
from random import randint
import matplotlib.pyplot as plt


N=10000
tau=1000
dt=100
count=np.zeros(N)
ndecay=np.zeros(N)
ptime=np.zeros(N)
alpha=float(0.693/tau)
decay_prob=alpha*dt
nsteps=300
no=100
n=no


for i in range(nsteps):
    for j in range(n):
        decay_rand=random.random()
        if (decay_rand < decay_prob):
            n=n-1
            ndecay[i]=ndecay[i]+1
    count[i]=n

print (decay_prob)    
print (decay_rand)

for i in range(nsteps):
    ptime[i]=i*dt

plt.plot(ptime[0:nsteps],count[0:nsteps],"--",ms=2)
plt.title("Redioactive Decay")
plt.xlabel("Time")
plt.ylabel("Number")
plt.grid(True)
plt.show()

        


































