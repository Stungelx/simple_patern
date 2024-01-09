from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
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
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """

    def create_table(self) -> Table:
        return Modern_Table()

    def create_chair(self) -> Chair:
        return Modern_chair()

    def operation(self) -> str:
        pass


class ConcreteFactory2(AbstractFactory):
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_table(self) -> Table:
        return Victorian_Table()

    def create_chair(self) -> Chair:
        return Victorian_Chair()


class Table(ABC):
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def useful_function_table(self) -> str:
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class Modern_Table(Table):
    def useful_function_table(self) -> str:
        return "Modern_Table" #Modern_Table


class Victorian_Table(Table):
    def useful_function_table(self) -> str:
        return "The result of the product Victorian_Table." #Victorian_Table


class Chair(ABC):
    """
    Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
    друг с другом, но правильное взаимодействие возможно только между продуктами
    одной и той же конкретной вариации.
    """
    @abstractmethod
    def useful_function_chair(self) -> None:
        """
        Продукт B способен работать самостоятельно...
        """
        pass

    @abstractmethod
    def another_useful_function_chair(self, collaborator: Table) -> None:
        """
        ...а также взаимодействовать с Продуктами A той же вариации.

        Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совместимы.
        """
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class Modern_chair(Chair):
    def useful_function_chair(self) -> str:
        return "Modern_Chair." #Modern_Chair

    """
    Продукт B1 может корректно работать только с Продуктом A1. Тем не менее, он
    принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
    """

    def another_useful_function_chair(self, collaborator: Table) -> str:
        result = collaborator.useful_function_table()
        return f"Modern_Chair collaborating with the ({result})" #Modern_Chair


class Victorian_Chair(Chair):
    def useful_function_chair(self) -> str:
        return "The result of the product Victorian_Chair." #Victorian_Chair

    def another_useful_function_chair(self, collaborator: Table):
        """
        Продукт B2 может корректно работать только с Продуктом A2. Тем не менее,
        он принимает любой экземпляр Абстрактного Продукта А в качестве
        аргумента.
        """
        result = collaborator.useful_function_table()
        return f"The result of the Victorian_Chair collaborating with the ({result})" #Victorian_Chair


def client_code(factory: AbstractFactory) -> None:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    product_a = factory.create_table()
    product_b = factory.create_chair()
    text_modern = factory.some_operation_table()

    print(f"{product_b.useful_function_chair()}")
    print(f"{product_b.another_useful_function_chair(product_a)}", end="")
    print(f"{text_modern}")

if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())