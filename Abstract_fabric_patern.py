from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_table(self) -> Table:
        pass

    def some_operation_table(self) -> str:
        product = self.create_table()
        result = f"\nOperation finished. Product {product.useful_function_table()} creted."
        return result

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    def some_operation_chair(self) -> str:
        product = self.create_chair()
        result = f"\nOperation finished. Product {product.useful_function_chair()} creted."
        return result


class ConcreteFactory1(AbstractFactory):
    def create_table(self) -> Table:
        return ModernTable()

    def create_chair(self) -> Chair:
        return ModernChair()

    def operation(self) -> str:
        pass


class ConcreteFactory2(AbstractFactory):
    def create_table(self) -> Table:
        return VictorianTable()

    def create_chair(self) -> Chair:
        return VictorianChair()


class Table(ABC):
    @abstractmethod
    def useful_function_table(self) -> str:
        pass


class ModernTable(Table):
    def useful_function_table(self) -> str:
        return "Modern Table"


class VictorianTable(Table):
    def useful_function_table(self) -> str:
        return "The result of the product Victorian Table."


class Chair(ABC):
    @abstractmethod
    def useful_function_chair(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_chair(self, collaborator: Table) -> None:
        pass


class ModernChair(Chair):
    def useful_function_chair(self) -> str:
        return "Modern Chair."

    def another_useful_function_chair(self, collaborator: Table) -> str:
        result = collaborator.useful_function_table()
        return f"Modern Chair collaborating with the ({result})"


class VictorianChair(Chair):
    def useful_function_chair(self) -> str:
        return "The result of the product Victorian Chair."

    def another_useful_function_chair(self, collaborator: Table):
        result = collaborator.useful_function_table()
        return f"The result of the Victorian Chair collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_table()
    product_b = factory.create_chair()
    text_modern = factory.some_operation_table()

    print(f"{product_b.useful_function_chair()}")
    print(f"{product_b.another_useful_function_chair(product_a)}", end="")
    print(f"{text_modern}")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
