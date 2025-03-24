import numpy as np

#%% punto c
a = np.array([[1j,-1+1j,0],[1,-2,1],[1,2j,-1]])
b = np.array([-1,0,2j])
sol = np.linalg.solve(a, b)
sol

#%%