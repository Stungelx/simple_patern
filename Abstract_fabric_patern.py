from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_table(self) -> Table:
        pass

    def some_operation(self) -> str:
        product = self.create_table()
        result = f"Operation finished. Product {product.fabric()} creted."
        return result

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    def some_operation1(self) -> str:
        product = self.create_chair()
        result = f"Operation finished. Product {product.fabric()} creted."
        return result


class ModernFactory(AbstractFactory):
    def create_table(self) -> Table:
        return ModernTable()

    def create_chair(self) -> Chair:
        return ModernChair()


class VictorianFactory(AbstractFactory):
    def create_table(self) -> Table:
        return VictorianTable()

    def create_chair(self) -> Chair:
        return VictorianChair()


class Table(ABC):
    @abstractmethod
    def useful_function_table(self) -> str:
        pass

    @abstractmethod
    def fabric(self) -> str:
        pass


class ModernTable(Table):
    def useful_function_table(self) -> str:
        return "The result of the product Modern Table"

    def fabric(self) -> str:
        return "Modern Table"


class VictorianTable(Table):
    def useful_function_table(self) -> str:
        return "The result of the product Victorian Table."

    def fabric(self) -> str:
        return "Victorian Table"


class Chair(ABC):
    @abstractmethod
    def useful_function_chair(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_chair(self, collaborator: Table) -> None:
        pass

    @abstractmethod
    def fabric(self) -> str:
        pass


class ModernChair(Chair):
    def useful_function_chair(self) -> str:
        return "The result of the product Modern Chair."

    def another_useful_function_chair(self, collaborator: Table) -> str:
        result = collaborator.fabric()
        return f"The result of the Modern Chair collaborating with the {result}"

    def fabric(self) -> str:
        return "Modern Chair"


class VictorianChair(Chair):
    def useful_function_chair(self) -> str:
        return "The result of the product Victorian Chair."

    def another_useful_function_chair(self, collaborator: Table):
        result = collaborator.fabric()
        return f"The result of the Victorian Chair collaborating with the {result}"

    def fabric(self) -> str:
        return "Victorian Chair"


def client_code(factory: AbstractFactory) -> None:
    table = factory.create_table()
    chair = factory.create_chair()
    text_table = factory.some_operation()
    text_chair = factory.some_operation1()

    print(f"{chair.useful_function_chair()}")
    print(f"{text_chair}")
    print(f"{text_table}")
    print(f"{chair.another_useful_function_chair(table)}")



print("\n")
print("Client: Testing client code with the Modern factory type:")
client_code(ModernFactory())

print("\n")

print("Client: Testing the same client code with the Victorian factory type:")
client_code(VictorianFactory())
#https://app.diagrams.net/#HStungelx%2Fsimple_patern%2Fmaster%2FAbstract_factory_diagram.drawio