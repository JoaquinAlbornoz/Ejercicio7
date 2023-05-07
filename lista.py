from Viajero import ViajeroFrecuente
import csv
class lista_viajeros:
    def __init__(self):
        self.__listav=[]
    def agregarviajero(self,v):
        self.__listav.append(v)
    def viaj(self):
        f=open("C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio 7\\viajeros.csv",'r')
        reader=csv.reader(f,delimiter=',')
        for fila in reader:
            if fila[0]!='' and fila[1]!='' and fila[2]!='' and fila[3]!='' and fila[4]!='':
                num=int(fila[0])
                dni=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                millas= int(fila[4])
                viajero=ViajeroFrecuente(num,dni,nombre,apellido,millas)
                self.agregarviajero(viajero)
        f.close()
  
    def buscarviajero(self,num):
        i=0
        b=True
        j = None
        while b and i<len(self.__listav):
            nv=self.__listav[i].getnum()
            if nv==num:
                b=False
                j = i
            else:
                i+=1
        return j
    def getlen(self):
        return len(self.__listav)
    def getcantmillas(self):
        num = int(input('Ingrese numero de viajero:'))
        i=self.buscarviajero(num)
        return self.__listav[i].cantidadTotaldeMillas()
    def acumillas(self,i,l):
        l+self.__listav[i]
        return self.__listav[i].cantidadTotaldeMillas()
    def canjmillas(self,i,l):
        if(self.__listav[i]>=l):
            l-self.__listav[i]
        else:
            print("\n---Error al canjear millas---\n")
        return self.__listav[i].cantidadTotaldeMillas()
    def Mayormillas(self):
        m=ViajeroFrecuente()
        lm=[]
        for i in range(len(self.__listav)):
            if self.__listav[i]>m:
                m=self.__listav[i]
        n=m.cantidadTotaldeMillas()
        for i in range(len(self.__listav)):
            if self.__listav[i]==n:
                lm.append(self.__listav[i])
        for i in range(len(lm)):
            print(lm[i])

