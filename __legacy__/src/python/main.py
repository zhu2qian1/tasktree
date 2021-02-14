from json import load, dump
from typing import Type, Union

path_id_json = ".\\src\\json\\ids.json"


class Unit:
    def __init__(self, name: str) -> None:
        self.name: str = name
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
    pass


class Project(UnitBase):
    pass


class User(UnitBase):
    pass


class Team(UnitBase):
    pass


def give_id(target: Union[Task, Project, Team, User], datapool=path_id_json):
    """give a unique id to Task, Project, Team, or User.
    The id pool can be configured."""

    setting = {"file": datapool, "mode": "r", "encoding": "utf-8"}

    if type(target) not in (Task, Project, Team, User):
        raise TypeError
    else:
        from json import load

    if type(target) == Task:
        with open(**setting) as f:
            d = load(fp=f)
            l = d["task"]
            s = l[-1].removeprefix("tk-")
            i = int(s) + 1
            return f"tk-{str(i).zfill(12)}"

    elif type(target) == Project:
        pass
    elif type(target) == User:
        pass
    elif type(target) == Team:
        pass
