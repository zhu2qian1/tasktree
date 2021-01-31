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
            raise ValueError(f"{self} has already adopted {child}.")
        else:
            self.__child.append(child)
            child.__parent.append(self)

    def abandon(self, child: Unit) -> None:
        if child is self:
            raise ValueError(f"{self} cannot abandon itself.")
        elif child not in self.__child:
            raise ValueError(f"{self} is not a parent of {child}.")
        else:
            self.__child.remove(child)
            child.__parent.remove(self)

    def join(self, parent: Unit) -> None:
        if parent is self:
            raise ValueError(f"{self} cannot join itself.")
        elif parent in self.__parent:
            raise ValueError(f"{self} has already joined {parent}.")
        else:
            self.__parent.append(parent)
            parent.__child.append(self)

    def leave(self, parent: Unit) -> None:
        if parent is self:
            raise ValueError(f"{self} cannot leave itself.")
        elif parent not in self.__parent:
            raise ValueError(f"{self} is not a child of {parent}.")
        else:
            self.__parent.remove(parent)
            parent.__child.remove(self)


class Task(UnitBase):
    def __init__(self) -> None:
        super().__init__(UnitBase)


class Project:
    pass


class Person:
    pass


class Team:
    pass
