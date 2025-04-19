"""
Eliminacion Gausianna
"""
import numpy as np
import matplotlib.pyplot as plt

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()

    if m!=n:
        print('Matriz no cuadrada')
        return

    ## desde aqui -- CODIGO A COMPLETAR
    for j in range(n-1):
        for i in range(j+1, n):
            assert(Ac[j,j] != 0)
            coef = Ac[i,j]/Ac[j,j]
            Ac[i,j:] = Ac[i,j:] - coef*Ac[j,j:]
            Ac[i,j] = coef
            cant_op+= 1 + (n-j)*2 + 1


    ## hasta aqui

    L = np.tril(Ac,-1) + np.eye(A.shape[0])
    U = np.triu(Ac)

    return L, U, cant_op

def sol_triang_inf(A,b):
    n = A.shape[0]
    y_vector = []
    for i in range(n):
        suma = 0
        for j in range(i):
            suma += y_vector[j]*A[i][j]
        assert(A[i,i] != 0)
        y_actual = (b[i] - suma)/A[i][i]
        y_vector.append(y_actual)
    return y_vector

def sol_triang_sup(A,b):
    n = A.shape[0]
    y_vector = np.zeros(n)
    for i in range(n-1,-1,-1):
        suma = 0
        for j in range(n-1,i,-1):
            suma += y_vector[j]*A[i][j]
        assert(A[i,i] != 0)
        y_actual = (b[i] - suma)/A[i][i]
        y_vector[i]=y_actual
    return y_vector

def sol_sistema(A,b):
    L,U,c=elim_gaussiana(A)
    y = sol_triang_inf(L,b)
    x = sol_triang_sup(U, y)
    return x

def pruebas_aleatorias(n):
    for d in range(1,n):
        B = np.eye(d) - np.tril(np.ones((d,d)),-1)
        B[:d,d-1] = 1
        vectores = np.random.randint(0, 10, size=(20, d))
        for v in vectores:
            print(sol_sistema(B, v))

#%%
def main():
    #n = 7
    #B = np.eye(n) - np.tril(np.ones((n,n)),-1)
    #B[:n,n-1] = 1
    B = np.array([[2,1,2,3],[4,3,3,4],[-2,2,-4,-12],[4,1,8,-3]])
    #print('Matriz B \n', B)

    L,U,cant_oper = elim_gaussiana(B)

    """print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )
    #print(L@U)"""
    graficar_operaciones(30)
    #print(sol_triang_inf(np.array([[4,0,0,0],[2,5,0,0],[1,3,6,0],[2,1,4,7]]), np.array([8,16,18,30])))
    A = np.array([[3, 5, 2, 1],
              [0, 4, 6, 3],
              [0, 0, 7, 8],
              [0, 0, 0, 9]])

    b = np.array([10, 15, 20, 25])
    #print(sol_triang_sup(A, b))
    #print(np.linalg.solve(A, b))

    A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])

    b = np.array([6, 15, 25])

    # Resolver el sistema Ax = b

    #print(sol_sistema(A, b))
    #print(np.linalg.solve(A, b))
    #pruebas_aleatorias(5)
def graficar_operaciones(cant):
    dim = []
    op = []
    for n in range(1,cant):
        B = np.eye(n) - np.tril(np.ones((n,n)),-1)
        B[:n,n-1] = 1
        l, u, c = elim_gaussiana(B)
        dim.append(n)
        op.append(c)
        norm_inf = np.max(np.sum(np.abs(u), axis=1))
        norm_esperada = 2**(n-1)
        print(norm_inf,norm_esperada)
    plt.plot(dim, op)
    plt.title("Gráfico de dimension contra cantidad de operaciones")
    plt.xlabel("Dimension")
    plt.ylabel("Cantidadd de operaciones")


if __name__ == "__main__":
    main()