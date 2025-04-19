import numpy as np

#%%
x = 16.69531126585727
ultimo = 0 
for i in range(int(5.6294994999999999999999999999e14),int(1e18)):
    x+= 1/i
    if ultimo != x:
        print("i = " + str(i) + " , x = " + str(x))
    if i % 10 == 0:
        ultimo = x
        
        
