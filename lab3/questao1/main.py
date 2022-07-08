from __future__ import annotations
from abc import ABC, abstractmethod

"""from nomedoarquivo import *"""
class Padaria(ABC):
    @abstractmethod
    def Fazer_bolo_Aniversario(self) -> Bolo:
        pass

    @abstractmethod
    def Fazer_bolo_Casamento(self) -> Bolo:
        pass

    @abstractmethod
    def Fazer_bolo_Festa_informal(self) -> Bolo:
        pass


class FazerBoloChocolate(Padaria):
    def Fazer_bolo_Aniversario(self) -> Bolo:
        return Bolo_chocolate_aniversario()

    def Fazer_bolo_Casamento(self) -> Bolo:
        return Bolo_chocolate_casamento()

    def Fazer_bolo_Festa_informal(self) -> Bolo:
        return Bolo_chocolate_festa_informal()


class FazerBoloMandioca(Padaria):
    def Fazer_bolo_Aniversario(self) -> Bolo:
        return Bolo_mandioca_aniversario()

    def Fazer_bolo_Casamento(self) -> Bolo:
        return Bolo_mandioca_casamento()

    def Fazer_bolo_Festa_informal(self) -> Bolo:
        return Bolo_mandioca_festa_informal()


class FazerBoloCenoura(Padaria):
    def Fazer_bolo_Aniversario(self) -> Bolo:
        return Bolo_cenoura_aniversario()

    def Fazer_bolo_Casamento(self) -> Bolo:
        return Bolo_cenoura_casamento()

    def Fazer_bolo_Festa_informal(self) -> Bolo:
        return Bolo_cenoura_festa_informal()


class Bolo(ABC):
    def __int__(self):
        self.tipo = None
        self.ocasiao = None

    def tipo(self) -> str:
        return self.tipo()

    def ocasiao(self) -> str:
        return self.ocasiao()


class Bolo_aniversario(Bolo):
    def __init__(self):
        self.tipo = None
        self.ocasiao = 'Aniversario'


class Bolo_casamento(Bolo):
    def __init__(self):
        self.tipo = None
        self.ocasiao = 'Casamento'


class Bolo_festa_informal(Bolo):
    def __init__(self):
        self.tipo = None
        self.ocasiao = 'Festa informal'


class Bolo_chocolate_aniversario(Bolo_aniversario):
    def __init__(self):
        super.__init__()
        self.tipo = 'Chocolate'


class Bolo_chocolate_casamento(Bolo_casamento):
    def __init__(self):
        super.__init__()
        self.tipo = 'Chocolate'


class Bolo_chocolate_festa_informal(Bolo_festa_informal):
    def __init__(self):
        super.__init__()
        self.tipo = 'Chocolate'


class Bolo_mandioca_aniversario(Bolo_aniversario):
    def __init__(self):
        super.__init__()
        self.tipo = 'Mandioca'


class Bolo_mandioca_casamento(Bolo_casamento):
    def __init__(self):
        super.__init__()
        self.tipo = 'Mandioca'


class Bolo_mandioca_festa_informal(Bolo_festa_informal):
    def __init__(self):
        super.__init__()
        self.tipo = 'Mandioca'

class Bolo_cenoura_aniversario(Bolo_aniversario):
    def __init__(self):
        super.__init__()
        self.tipo = 'Cenoura'


class Bolo_cenoura_casamento(Bolo_casamento):
    def __init__(self):
        super.__init__()
        self.tipo = 'Cenoura'


class Bolo_cenoura_festa_informal(Bolo_festa_informal):
    def __init__(self):
        super.__init__()
        self.tipo = 'Cenoura'

"""
def client_code(factory: Padaria) -> None:
   
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
   
    product_a = factory.Fazer_bolo_Casamento()
    a = product_a.tipo()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
  
    The client code can work with any concrete factory class.
   
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

   
    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
 """