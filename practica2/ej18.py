import numpy as np
import matplotlib.pyplot as plt

#%%
def estima(A):
    V = np.random.rand(2, 100) - 0.5
    for v in range(len(V[0])):
      norma = np.linalg.norm((V[0][v],V[1][v]), ord=2)
      V[0][v]=V[0][v]/norma
      V[1][v]=V[1][v]/norma
      
    #plt.scatter(V[0], V[1], label = "v")
    #plt.axis('equal')
    #plt.legend()    
    
    s = []
    s.append(0)
    for i in range(1,100):
        x = (V[0][i],V[1][i])
        Ax = A@x
        valor =  np.linalg.norm(Ax, ord=2) / np.linalg.norm(x, ord=2)
        s.append(max(s[i-1], valor))

    plt.plot(s)
    plt.hlines(y =np.linalg.norm(A,ord=2), xmin = 0, xmax = 100, color='r')
    plt.show()
    
A = np.array([[0,1],[3,2]])
estima(A)