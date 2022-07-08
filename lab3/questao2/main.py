from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produzir_recheio(self,recheio)->None:
        pass

    @abstractmethod
    def produzir_tipo(self,tipo)->None:
        pass

class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Bolo()

    @property
    def product(self) -> Bolo():
        product = self._product
        self.reset()
        return product

    def produzir_recheio(self,recheio) ->None:
        self._product.add(recheio)

    def produzir_tipo(self,tipo) ->None:
        self._product.add(tipo)


class Bolo():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Conteúdo: {', '.join(self.parts)}")


class Director:
    def __initt_(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def fazer_bolo_chocolate_aniversario(self) -> None:
        self.builder.produzir_tipo('Aniversario')
        self.builder.produzir_recheio('Chocolate')

    def fazer_bolo_chocolate_casamento(self) -> None:
        self.builder.produzir_tipo('Casamento')
        self.builder.produzir_recheio('Chocolate')

    def fazer_bolo_chocolate_informal(self) -> None:
        self.builder.produzir_tipo('Festa Informal')
        self.builder.produzir_recheio('Chocolate')

    def fazer_bolo_cenoura_aniversario(self) -> None:
        self.builder.produzir_tipo('Aniversario')
        self.builder.produzir_recheio('Cenoura')

    def fazer_bolo_cenoura_casamento(self) -> None:
        self.builder.produzir_tipo('Casamento')
        self.builder.produzir_recheio('Cenoura')

    def fazer_bolo_cenoura_informal(self) -> None:
        self.builder.produzir_tipo('Festa informal')
        self.builder.produzir_recheio('Cenoura')

    def fazer_bolo_mandioca_aniversario(self) -> None:
        self.builder.produzir_tipo('Aniversario')
        self.builder.produzir_recheio('Mandioca')

    def fazer_bolo_mandioca_casamento(self) -> None:
        self.builder.produzir_tipo('Casamento')
        self.builder.produzir_recheio('Mandioca')

    def fazer_bolo_mandioca_informal(self) -> None:
        self.builder.produzir_tipo('Festa informal')
        self.builder.produzir_recheio('Mandioca')


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Teste para a construção do bolo de chocolate para CASAMENTO")
    director.fazer_bolo_chocolate_casamento()
    builder.product.list_parts()
    print("\n")
    print("Teste para a construção do bolo de chocolate para CASAMENTO")
    director.fazer_bolo_mandioca_informal()
    builder.product.list_parts()
    print("\n")
    print("Teste para a construção do bolo de chocolate para CASAMENTO")
    director.fazer_bolo_cenoura_aniversario()
    builder.product.list_parts()
    print("\n")

