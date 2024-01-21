from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):

        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Operation finished. {product.operation()}"

        return result


class CreatorChair(Creator):
    def factory_method(self) -> Product:
        return Chair()


class CreatorTable(Creator):
    def factory_method(self) -> Product:

        return Table()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Table(Product):
    def operation(self) -> str:
        return str('Table was created')


class Chair(Product):
    def operation(self) -> str:
        return "{Chair was created}"


def client_code(creator: Creator) -> None:
    print(f"Client: Starting operation of the creating Product.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the CreatorChair.")
    client_code(CreatorChair())
    print("\n")

    print("App: Launched with the CreatorTable.")
    client_code(CreatorTable())

#https://app.diagrams.net/#HStungelx%2Fsimple_patern%2Fmaster%2F%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.drawio

