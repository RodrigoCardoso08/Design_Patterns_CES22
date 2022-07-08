from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Contexto: Transitição para {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class EstadoRascunho(State):
    def handle1(self) -> None:
        print("Rascunho foi publicado pelo usuário")
        print("Rascunho quer mudar para o estado moderação")
        self.context.transition_to(EstadoModeracao())

    def handle2(self) -> None:
        print("Rascunho foi publicado pela administração")
        print("Rascunho quer mudar para o estado Publicado")
        self.context.transition_to(EstadoPublicado())


class EstadoModeracao(State):
    def handle1(self) -> None:
        print("Moderação foi aprovado pela administração")
        print("EstadoModeração quer mudar para o EstadoPublicado")
        self.context.transition_to(EstadoPublicado())

    def handle2(self) -> None:
        print("Moderação foi recusado pela Revisão")
        print("EstadoModeração quer mudar para o EstadoRascunho")
        self.context.transition_to(EstadoRascunho())

class EstadoPublicado(State):
    def handle1(self) -> None:
        print("Publicação expirou.")
        print("EstadoPublicado quer mudar para o EstadoRascunho")
        self.context.transition_to(EstadoRascunho())

    def handle2(self) -> None:
        print("Publicação não expirou")
        print("Estado Publicado mantém publicado")


if __name__ == "__main__":
    # The client code.

    context = Context(EstadoRascunho())
    print("\n")
    context.request1()
    print("\n")
    context.request1()
    print("\n")
    context.request1()