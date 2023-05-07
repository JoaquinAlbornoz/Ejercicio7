class ViajeroFrecuente:
    def __init__(self,num_viajero=0,dni= '',nombre= '',apellido='', millas_acumuladas=0):
        self.__num_viajero =num_viajero
        self.__dni =dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acumuladas=millas_acumuladas
    def __str__(self):
        return f'Num.viajero:{self.__num_viajero}\tDNI:{self.__dni}\tNombre y Apellido:{self.__nombre} {self.__apellido}\tMillas:{self.__millas_acumuladas}'
    def __gt__(self,otroviajero):
        return self.__millas_acumuladas>otroviajero.cantidadTotaldeMillas()
    def __eq__(self,otroviajero):
        if type(otroviajero)==type(self):
            b=self.__millas_acumuladas==otroviajero.cantidadTotaldeMillas()
        else:
            b=self.__millas_acumuladas==otroviajero
        return b
    def __req__(self,otroviajero):
        if type(otroviajero)==type(self):
            b=otroviajero.cantidadTotaldeMillas()==self.__millas_acumuladas
        else:
            b=otroviajero==self.__millas_acumuladas
        return b
    def __add__(self,n):
        self.__millas_acumuladas+=n
        return self.__millas_acumuladas
    def __radd__(self,n):
        self.__millas_acumuladas+=n
        return self.__millas_acumuladas
    def __sub__(self,n):
        self.__millas_acumuladas-=n
        return self.__millas_acumuladas
    def __rsub__(self,n):
        self.__millas_acumuladas-=n
        return self.__millas_acumuladas
    def __ge__(self,n):
        return self.__millas_acumuladas>=n
    def cantidadTotaldeMillas(self):
        return self.__millas_acumuladas
    def getnum(self):
        return self.__num_viajero
    