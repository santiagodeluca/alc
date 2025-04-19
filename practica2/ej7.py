import numpy as np
e = np.finfo(float).eps
#%%

p = 1e34
q = 1
p + q - p

p = 100
q = 1e-15
(p + q) + q
((p + q) + q) + q
p + 2*q
p + 3*q
p + 8*q

0.1+0.2 == 0.3
0.1+0.3 == 0.4

1e-323 
1e-324

e/2
e

(1 + e/2) + e/2
1 + (e/2 + e/2)

((1 + e/2) + e/2)-1
(1 + (e/2 + e/2))-1

for j in range(1,26):
    print(np.sin(np.pi*(10**j)))

for j in range(1,26):
    print((np.pi/2) + np.pi*(10**j))
    print(np.sin((np.pi/2) + np.pi*(10**j)))


