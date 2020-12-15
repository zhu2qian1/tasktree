DEBUG = True


class Unit:
    def __init__(self, name: str):
        self.name: str = name
        self.parentof: list = []
        self.childof: list = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def adopt(self, child):
        # nobody can either adopt somebody who have already existed or adopt oneself.
        if child is self:
            raise ValueError(f"{self} cannot adopt itself.")
        elif child in self.parentof:
            raise ValueError(
                f"{self} cannot adopt {child} for {self} is already parent of {child}"
            )
        else:
            self.parentof.append(child)
            child.childof.append(self)
        if DEBUG:
            print(f"{self} adopted {child}. Children of {self} are {self.parentof}.")

    def abandon(self, child):
        # nobody can abandon somebody who does not exist or abandon oneself.
        if child is self:
            raise ValueError(f"{self} cannot abandon itself")
        elif child not in self.parentof:
            raise ValueError(
                f"{self} cannot abandon {child} for {self} is not parent of {child}"
            )
        else:
            self.parentof.remove(child)
            child.childof.remove(self)
        if DEBUG:
            print(f"{self} abandoned {child}. Children of {self} are {self.parentof}.")

    def _tellfamily(self):
        print(f"{self} is parent of {self.parentof} and child of {self.childof}.")


units = []
units.append((aunit := Unit("Unit A")))
units.append((bunit := Unit("Unit B")))
units.append((cunit := Unit("Unit C")))
units.append((dunit := Unit("Unit D")))

aunit.adopt(bunit)
aunit.adopt(dunit)
aunit.adopt(cunit)
cunit.adopt(aunit)
bunit.adopt(cunit)
aunit.abandon(bunit)
cunit.abandon(aunit)
print("------------")
for unit in units:
    unit._tellfamily()
