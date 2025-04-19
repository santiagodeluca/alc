import numpy as np
import scipy

def construye_adyacencia(D,m):
    # Funci√≥n que construye la matriz de adyacencia del grafo de museos
    # D matriz de distancias, m cantidad de links por nodo
    # Retorna la matriz de adyacencia como un numpy.
    D = D.copy()
    l = [] # Lista para guardar las filas
    for fila in D: # recorriendo las filas, anexamos vectores l√≥gicos
        l.append(fila<=fila[np.argsort(fila)[m]] ) # En realidad, elegimos todos los nodos que est√©n a una distancia menor o igual a la del m-esimo m√°s cercano
    A = np.asarray(l).astype(int) # Convertimos a entero
    np.fill_diagonal(A,0) # Borramos diagonal para eliminar autolinks
    return(A)

def calculaLU(A):
    # matriz es una matriz de NxN
    # Retorna la factorizaci√≥n LU a trav√©s de una lista con dos matrices L y U de NxN.
    # Completar! Have fun
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()

    if m!=n:
        print('Matriz no cuadrada')
        return

    for j in range(n-1):
        for i in range(j+1, n):
            assert(Ac[j,j] != 0)
            coef = Ac[i,j]/Ac[j,j]
            Ac[i,j:] = Ac[i,j:] - coef*Ac[j,j:]
            Ac[i,j] = coef

    L = np.tril(Ac,-1) + np.eye(A.shape[0])
    U = np.triu(Ac)

    return [L, U]

def calcula_matriz_C(A):
    # Funci√≥n para calcular la matriz de trancisiones C
    # A: Matriz de adyacencia
    # Retorna la matriz C
    n = A.shape[0]
    Kinv = np.zeros((n, n))# Calcula inversa de la matriz K, que tiene en su diagonal la suma por filas de A
    Atr = np.zeros((n,n))
    for fila in range(n):
        valor = 0
        for col in range(n):
            valor += A[fila][col]
            Atr[col][fila] = A[fila][col]
        Kinv[fila][fila] = 1/valor

    C = Atr@Kinv # Calcula C multiplicando Kinv y A
    return C


def calcula_pagerank(A,alfa):
    # Funci√≥n para calcular PageRank usando LU
    # A: Matriz de adyacencia
    # d: coeficientes de damping
    # Retorna: Un vector p con los coeficientes de page rank de cada museo
    C = calcula_matriz_C(A)
    N = A.shape[0] # Obtenemos el n√∫mero de museos N a partir de la estructura de la matriz A
    M = np.subtract(np.eye(N),((1-alfa)*C))
    L, U = calculaLU(M) # Calculamos descomposici√≥n LU a partir de C y d
    b = (alfa/N)*np.ones(N) # Vector de 1s, multiplicado por el coeficiente correspondiente usando d y N.
    Up = scipy.linalg.solve_triangular(L,b,lower=True) # Primera inversi√≥n usando L
    p = scipy.linalg.solve_triangular(U,Up) # Segunda inversi√≥n usando U
    return p

def calcula_matriz_C_continua(D):
    # Funci√≥n para calcular la matriz de trancisiones C
    # A: Matriz de adyacencia
    # Retorna la matriz C en versi√≥n continua
    D = D.copy()
    n = D.shape[0]
    temp = D + np.eye(n)
    F = 1/temp
    F = F - np.eye(n)
    np.fill_diagonal(F,0)
    Kinv = np.zeros((n, n))# Calcula inversa de la matriz K, que tiene en su diagonal la suma por filas de F
    for fila in range(n):
        valor = F[fila].sum()
        Kinv[fila][fila] = 1/valor

    C = Kinv@F # Calcula C multiplicando Kinv y F
    return C
#%%
def calcula_B(C,cantidad_de_visitas):
    # Recibe la matriz T de transiciones, y calcula la matriz B que representa la relaci√≥n entre el total de visitas y el n√∫mero inicial de visitantes
    # suponiendo que cada visitante realiz√≥ cantidad_de_visitas pasos
    # C: Matirz de transiciones
    # cantidad_de_visitas: Cantidad de pasos en la red dado por los visitantes. Indicado como r en el enunciado
    # Retorna:Una matriz B que vincula la cantidad de visitas w con la cantidad de primeras visitas v
    B = np.eye(C.shape[0])
    Cc = np.eye(C.shape[0])
    for i in range(cantidad_de_visitas-1):
        # Sumamos las matrices de transici√≥n para cada cantidad de pasos
        Cc = C@Cc
        B = np.add(B,B@Cc)
    return B
#%%
#A = np.array([[5,5,1,0],[1,2,0,3],[2,1,5,0],[2,1,1,2]])
#print(calcula_matriz_C(A))
