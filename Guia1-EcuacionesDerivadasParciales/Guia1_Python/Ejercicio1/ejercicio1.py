import numpy as np
import matplotlib.pyplot as plt
import tycc
import valcc
import geo
import MakeA as lib
import time


def makensolve(mygeo,  mytycc, myvalcc):
    vertices = (0,  mygeo.Nx-1,  mygeo.Nx*(geo.Ny-1),  mygeo.Nx*geo.Ny-1)
#  borde de abajo
    kc = np.linspace(vertices[0],  vertices[1], mygeo.Nx).astype(int)
# borde de arriba
    kd = np.linspace(vertices[2],  vertices[3], mygeo.Nx).astype(int)
# borde de la izquierda
    ka = np.linspace(vertices[0],  vertices[2], mygeo.Ny).astype(int)
# borde de la derecha
    kb = np.linspace(vertices[1],  vertices[3], mygeo.Ny).astype(int)
#  Solucion
    A, B = lib.makeA(ka, kb, kc, kd, mygeo, tycc, valcc)
    to = time.time()
    T = np.linalg.solve(A, B)
    dt = time.time()-to

    return T, dt


def maketmat(T, mygeo):
    myTmat = np.zeros([geo.Nx, geo.Ny])
    for i in np.linspace(0, mygeo.Nx-1, mygeo.Nx).astype(int):
        for j in np.linspace(0, mygeo.Ny-1, mygeo.Ny).astype(int):
            k = i+j*mygeo.Nx
            myTmat[j, i] = T[k]
    return myTmat


def makeplots(myTmat, mygeo, case):
    x = np.linspace(0, mygeo.Lx, geo.Nx).astype(float)
    y = np.linspace(0, mygeo.Ly, geo.Ny).astype(float)
    X, Y = np.meshgrid(x, y)

    CS = plt.contourf(X, Y, myTmat)
    CS2 = plt.contour(CS, levels=CS.levels, colors='k', linewidth=5)
    plt.xlabel('X')
    plt.ylabel('Y')
    cbar = plt.colorbar(
            CS,
            ticks=np.linspace(np.min(np.min(myTmat)),
                np.max(np.max(myTmat)),
                10).astype(int),
            boundaries=[np.min(np.min(myTmat)), np.max(np.max(myTmat))]
            )
    cbar.ax.set_ylabel('Temperature')
    plt.title(case)
    plt.show()
    plt.savefig('Temps-'+case+'.pdf')
    plt.close()

    return x, y


def makeFlujos(myTmat, myx, myy, case):
    dTy,  dTx = lib.migrad(myTmat)
    X, Y = np.meshgrid(myx, myy)
    plt.streamplot(X, Y, -dTx, -dTy, color='k', linewidth=3, density=1)

    plt.show()
    plt.savefig('Temps-'+case+'-Flujos.pdf')

    return dTx, dTy


def main():
    """
    Este módulo Python resuelve el problema 1 de la guia.
    Funciones:

    main() : llamado a las funciones de los distintos pasos ,
    con opciones por omisión

    makeFlujos(myTmat, myx, myy, case)
    construye los flujos, retorna  dTx, dTy

    maketmat(T, mygeo)
    pasa del vector temp a la matriz temp, devuelve mtTmat

    makeplots():
    como su nombre lo indica, construye los gráfcos con el nombre de 'case'
    indicado
    """
    T, dt = makensolve(geo, tycc, valcc)
    Tmat = maketmat(T, geo)

    x, y = makeplots(Tmat, geo, tycc.abajo)
    dTy, dTx = makeFlujos(Tmat, x, y, tycc.abajo)


def escaleo():
    """
    esta función calcula los tiempos para resolver el problema 
    ( para invertir la matriz )
    llama a makemat y makeplot
    guarda Temps-case.dat
    """
    Nx = 3**np.linspace(2.5, 4, 10)
    Nx = Nx.astype(int)
    t = []
    filetiempos = open('tabla-tiempos.dat','w')
    for size in Nx:
        geo.Nx = size
        geo.Ny = size
        case = '{:03d}'.format(size)
        T, dt = makensolve(geo, tycc, valcc)
        t.append(dt)
        print(case, dt)
        Tmat = maketmat(T, geo)
        np.savetxt('Temps-'+case+'.dat', Tmat)
        x, y = makeplots(Tmat, geo, case)
        filetiempos.write('{:d}  {:10e} \n'.format(size, dt))
    filetiempos.close()


def fitescaleo(datafile):
    n, dt = np.loadtxt(datafile, unpack=True)
    x = np.log(n)
    y = np.log(dt)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, y, 'ok')
    plt.plot(x, m*x+b, '--k')
    plt.xlabel(r'$log(N)$')
    plt.ylabel(r'$log(t)$')
    plt.show()
    plt.savefig('fitescaleo.pdf')


def plotchapa(tempsfile):
    Tmat = np.loadtxt(tempsfile)
    geo.Nx, geo.Ny = np.shape(Tmat)
    case = '{:03d}x{:03d}'.format(geo.Nx, geo.Ny)
    makeplots(Tmat, geo, case)


if __name__ == "__main__":
    main()
