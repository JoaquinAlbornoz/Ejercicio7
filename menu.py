from Viajero import ViajeroFrecuente
from lista import lista_viajeros

def Menu(lista):
    lista.viaj()
    b=True
    while b:
         n=int(input('Ingrese numero de viajero: '))
         i=lista.buscarviajero(n)
         if i==lista.getlen():
            print('\nError ingrese de nuevo el numero de viajero:\n')
         else:
          b=False
    m=1
    while m!=0:
          m=int(input('\n1.Consultar cantidad de millas\n2.Acumular Millas\n3.Canjear Millas\n4.Mostrar viajeros con mayor cant de millas\nIngrese opcion elegida, para terminar ingrese 0:'))
          if m==1:
              millas=lista.getcantmillas()
              print("\nCantidad de millas:{0}".format(millas))
          elif m==2:
              l=int(input('\nIngrese millas a acumular:'))
              k=lista.acumillas(i,l)
              print('Cantidad de millas: {0}'.format(k))
          elif m==3:
              l=int(input('\nIngrese numero de millas a canjear:'))
              print('Millas restantes:{0}'.format(lista.canjmillas(i,l)))
          elif m==4:
              lista.Mayormillas()

if __name__== '__main__':
    lista=lista_viajeros()
    Menu(lista)