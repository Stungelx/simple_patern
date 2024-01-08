class Factory:
    def manufacturing(self):
        pass


class Table(Factory):
    def manufacturing(self):
        print('Стіл зроблено')


class Chair(Factory):
    def manufacturing(self):
        print('Стілець виготовлено')


class Creator:
    def create(self) -> Factory:
        pass


class TableCreator(Creator):
    def create(self):
        return Table()


class ChairCreator(Creator):
    def create(self):
        return Chair()


table_creator = TableCreator()
table = table_creator.create()
table.manufacturing()

chair_creator = ChairCreator()
chair = chair_creator.create()
chair.manufacturing()
