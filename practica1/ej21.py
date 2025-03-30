import numpy as np
#%% a)
def tr(m):
    res = 0
    for fila in range(len(m)):
        res += m[fila][fila]
    return res

m1 = np.array([[1,1,1],[0,1,1],[0,0,1]])
m2 = np.array([[19,31,1],[0,1,1],[0,0,-20]])
print(tr(m1))
print(tr(m2))
#%% b)
def sum_mat(m):
    res = 0
    cant_columnas = len(m[0])
    for fila in range(len(m)):
        for col in range(cant_columnas):
            res += m[fila][col]
    return res
m1 = np.array([[1,1,1],[0,1,1],[0,0,1]])
print(sum_mat(m1))
m2 = np.array([[9,1,-9],[11,1,1],[0,0,1]])
print(sum_mat(m2))
#%% c) 
def mas_positivos(m):
    return sum_mat(m)>=0
m1 = np.array([[1,1,1],[0,1,1],[0,0,1]])
m2 = np.array([[-19,31,1],[0,1,1],[0,0,-29]])
print(mas_positivos(m1))
print(mas_positivos(m2))
