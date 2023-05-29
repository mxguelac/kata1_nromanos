from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError('Debe incializarse con un entero o romano valido')
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)

    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self._numero = romano_a_entero(entrada)

    """
    metodos mágicos para lógica
    """
    def __eq__(self, other):
        return self.numero == other.numero
    """
    metodos mágicos para aritmética
    """
    def __mul__(self, otro):
        if not isinstance (otro, RomanNumber):
            otro = RomanNumber (otro)

        resultado = self.numero * otro.numero

        return RomanNumber(resultado)
    
    def __rmul__ (self, otro):
        return self.__mul__(otro)
    
    """
    metodos mágicos para representación
    """
    def __repr__(self):
        return f"{self.numero} - {self.simbolo}"

    def __str__(self):
        return self.__repr__()

   