from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def legs(self) -> None:
        pass

    @abstractmethod
    def tabletop(self) -> None:
        pass

    @abstractmethod
    def chairs(self) -> None:
        pass

    @abstractmethod
    def lamination(self) -> None:
        pass


class ModernCreator(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = ModernSet()

    @property
    def product(self) -> ModernSet:
        product = self._product
        self.reset()
        return product

    def legs(self) -> None:
        self._product.add({"number of legs": 4})

    def tabletop(self) -> None:
        self._product.add({"tabletop": 'glass'})

    def chairs(self) -> None:
        self._product.add({"number of chairs": 2})

    def lamination(self) -> None:
        self._product.add({"shade of lamination": 'black'})


class VictorianCreator(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = VictorianSet()

    @property
    def product(self) -> VictorianSet:
        product = self._product
        self.reset()
        return product

    def legs(self) -> None:
        self._product.add({"number of legs": 3})

    def tabletop(self) -> None:
        self._product.add({"tabletop": 'tree'})

    def chairs(self) -> None:
        self._product.add({"number of chairs": 3})

    def lamination(self) -> None:
        self._product.add({"shade of lamination": 'brown'})


class VictorianSet():
    def __init__(self) -> None:
        self.parts = {}

    def add(self, part: dict) -> None:
        self.parts.update(part)

    def list_parts(self) -> None:
        print(f"Product parts: {self.parts}", end="")


class ModernSet():
    def __init__(self) -> None:
        self.parts = {}

    def add(self, part: dict) -> None:
        self.parts.update(part)

    def list_parts(self) -> None:
        print(f"Product parts: {self.parts}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.legs()
        self.builder.tabletop()

    def build_full_featured_product(self) -> None:
        self.builder.legs()
        self.builder.tabletop()
        self.builder.chairs()
        self.builder.lamination()


if __name__ == "__main__":
    director = Director()
    type_of_set = [ModernCreator(), VictorianCreator()]

    for i in type_of_set:
        builder = i
        director.builder = builder

        print("Standard basic", str(type(builder).__name__)[:-7], "table: ")
        director.build_minimal_viable_product()
        builder.product.list_parts()

        print("\n")

        print("Standard full", str(type(builder).__name__)[:-7], "set: ")
        director.build_full_featured_product()
        builder.product.list_parts()

        print("\n")

        print("Custom product: ")
        builder.legs()
        builder.tabletop()
        builder.lamination()
        builder.product.list_parts()
        print("\n")
