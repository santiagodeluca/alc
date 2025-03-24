import numpy as np
import matplotlib.pyplot as plt #l i b r e r i a para g r a f i c a r
#%% Soluciono el sistema
m = np.array([[1,1,1],[4,2,1],[9,3,1]])
s = np.array([1,2,0])
sol = np.linalg.solve(m, s)

a=sol[0]
b=sol[1]
c=sol[2]

#%% Grafico
xx = np.array( [ 1 , 2 , 3 ] )
yy = np.array( [ 1 , 2 , 0 ] )
x = np.linspace( 0 , 4 , 100 ) #gene r a 100 puntos e q ui e s p a ci a d o s e n t r e 0 y 4 .
f = lambda t : a*t **2+b* t+c #es t o gene r a una f u n ci o n f de t .
plt.plot( xx , yy , '*' )
plt.plot( x , f ( x ) )
plt.show()
