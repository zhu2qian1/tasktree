class Unit:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__id: str = ""
        self.__child: list = []
        self.__parent: list = []


class UnitBase(Unit):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def adopt(self, child: Unit) -> None:
        if child is self:
            raise ValueError(f"{self} cannot adopt itself.")
        elif child in self.__child:
            raise ValueError(f"{child} is already a child of {self}.")
        else:
            self.__child.append(child)
            child.__parent.append(self)

    def abandon(self, child: Unit) -> None:
        if child is self:
            raise ValueError(f"{self} cannot abandon itself.")
        elif child not in self.__child:
            raise ValueError(f"{child} is not a child of {self}.")
        else:
            self.__child.remove(child)
            child.__parent.remove(self)

    def join(self, parent: Unit) -> None:
        if parent is self:
            raise ValueError
        elif parent in self.__parent:
            raise ValueError
        else:
            pass

    def leave(self, parent: Unit) -> None:
        if parent is self:
            raise ValueError
        elif parent not in self.__parent:
            raise ValueError

        else:
            pass


class Task:
    pass


class Project:
    pass


class Person:
    pass


class Team:
    pass
