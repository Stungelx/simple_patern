import copy


class VictorianSet:
    def __init__(self, tabletop_type, number_of_legs, number_of_chairs, lamination):
        self.tabletop_type = tabletop_type
        self.number_of_legs = number_of_legs
        self.number_of_chairs = number_of_chairs
        self.lamination = lamination

    def __copy__(self):
        lamination = copy.copy(self.lamination)

        new = self.__class__(self.tabletop_type, self.number_of_legs, self.number_of_chairs, lamination)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        lamination = copy.deepcopy(self.lamination, memo)

        new = self.__class__(self.tabletop_type, self.number_of_legs, self.number_of_chairs, lamination)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new

    def __str__(self):
        return f"tabletop type: {self.tabletop_type}, number of legs: {self.number_of_legs}, " \
               f"number of chairs: {self.number_of_chairs}, lamination: {self.lamination}"


if __name__ == "__main__":
    victorian_full_set = VictorianSet('tree', 3, 3, {'type': '3d'})
    print(f"Create object victorian_full_set: ({victorian_full_set})")
    victorian_full_set_copy = copy.copy(victorian_full_set)
    print(f"Create object victorian_full_set_copy: ({victorian_full_set_copy})")
    print("\n")

    print("Add new key and value to dictionary 'lamination' in object victorian_full_set_copy, "
          "and see, that change values in victorian_full_set too:")
    victorian_full_set_copy.lamination.update({'color': 'brown'})
    print(f"victorian_full_set_copy: ({victorian_full_set_copy})")
    print(f"victorian_full_set: ({victorian_full_set})")
    print("\n")

    print("But we can create new object with deepcopy, and add new key and value to dictionary 'lamination' in "
          "victorian_full_set_deepcopy, and see, that values in victorian_full_set not update")
    victorian_full_set_deepcopy = copy.deepcopy(victorian_full_set)
    victorian_full_set_deepcopy.lamination.update({'caption': 'AVADA'})
    print(f"victorian_full_set_deepcopy: ({victorian_full_set_deepcopy})")
    print(f"victorian_full_set: ({victorian_full_set})")
