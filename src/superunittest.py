zqConstants = {}
zqConstants["DEBUG"] = True
zqConstants["SEPARATION"] = "-" * 32


class UnitBase:
    def __init__(self, name: str):
        self.name: str = name
        self.parentof: list = []
        self.childof: list = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def _tellfamily(self):
        print(f"{self} is a parent of {self.parentof} and a child of {self.childof}.")


class Unit(UnitBase):
    def adopt(self, child: UnitBase):
        # nobody can either adopt somebody who have already existed or adopt oneself.
        if child is self:
            raise ValueError(f"{self} cannot adopt itself.")
        elif child in self.parentof:
            raise ValueError(
                f"{self} cannot adopt {child} for {self} is already the parent of {child}."
            )
        else:
            self.parentof.append(child)
            child.childof.append(self)
        if zqConstants["DEBUG"]:
            print(f"{self} adopted {child}. Children of {self} are {self.parentof}.")

    def abandon(self, child: UnitBase):
        # nobody can abandon somebody who does not exist or abandon oneself.
        if child is self:
            raise ValueError(f"{self} cannot abandon itself.")
        elif child not in self.parentof:
            raise ValueError(
                f"{self} cannot abandon {child} for {self} is not a parent of {child}."
            )
        else:
            self.parentof.remove(child)
            child.childof.remove(self)
        if zqConstants["DEBUG"]:
            print(f"{self} abandoned {child}. Children of {self} are {self.parentof}.")

    def join(self, parent: UnitBase):
        # nobody can join himself or join the same family twice.
        if parent is self:
            raise ValueError(f"{self} cannot join itself.")
        elif parent in self.childof:
            raise ValueError(f"{self} cannot join the family under the same parent.")
        else:
            self.childof.append(parent)
            parent.parentof.append(self)
        if zqConstants["DEBUG"]:
            print(f"{self} joined {parent}. Parents of {self} are {self.childof}.")

    def leave(self, parent: UnitBase):
        # nobody can leave himself or a parent who does not even exist.
        if parent is self:
            raise ValueError()
        elif parent not in self.parentof:
            raise ValueError()
        else:
            parent.childof.remove(self)
            self.parentof.remove(parent)
        if zqConstants["DEBUG"]:
            print(f"{self} left {parent}. Parents of {self} are {self.childof}.")


if __name__ == "__main__":
    from random import choice

    units = []
    units.append((aunit := Unit("Unit A")))
    units.append((bunit := Unit("Unit B")))
    units.append((cunit := Unit("Unit C")))
    units.append((dunit := Unit("Unit D")))
    for i in range(10):
        try:
            choice(units).adopt(choice(units))
        except ValueError:
            print("(ValueError)")

    print(zqConstants["SEPARATION"])
    for unit in units:
        unit._tellfamily()
