import numpy as np
#%%
1 + 3
a = 7
b = a + 1
print ( 'b = '  , b )
#%% V e c t o r e s
v = np.array([ 1 , 2 , 3 , -1] )
w = np.array( [ 2 , 3 , 0 , 5 ] )
print( 'v + w = ' , v + w)
print( '2*v = ' , 2*v )
print( 'v**2 = ' , v **2 )
#%% Matrices(ejecutarlos comandos uno a uno para ver los resultados)
A = np.array( [ [ 1 , 2 , 3 , 4 , 5 ] , [ 0 , 1 , 2 , 3 , 4 ] , [ 2 , 3 , 4 , 5 , 6 ] , [ 0 , 0 , 1 , 2 , 3 ] , [ 0 , 0 , 0 , 0 , 1 ] ] )
print(A)
A[ 0 : 2 , 3 : 5 ]
A[ : 2 , 3 : ]
A[ [ 0 , 2 , 4 ] , : ]
ind = np.array( [ 0 , 2 , 4 ] )
A[ ind , ind ]
A[ ind , ind [ : , None ] ]
#%% Numeros complejos
1j *1j
(1+2j ) *1j
