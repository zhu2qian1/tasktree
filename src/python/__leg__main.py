from typing import Union
from datetime import date, datetime


class User:
    def __init__(self, name: str, mail: str = "(No email address provided)"):
        self.__id = "ur-xxxxxxxxxxxx"
        self.name: str = name
        self.mail: str = mail
        self.profile: str = ""
        self.affiliation: list = []
        self.assigned_task: list = []
        self.assigned_proj: list = []


class Project:
    def __init__(
        self,
        name: str = "(Unnamede proeject)",
        goal: str = "(No goal provied)",
        desc: str = "(No description provided)",
    ) -> None:
        self.__id: str = "pj-xxxxxxxxxxxx"
        self.name: str = name
        self.goal: str = goal
        self.desc: str = desc
        self.isstarted: bool = False
        self.isfinished: bool = False
        self.plan: list[date, date] = [None, None]
        self.duration: list[date, date] = [None, None]
        self.childof: list = []
        self.parentof: list = []


class Task:
    def __init__(
        self,
        name: str = "(Unnamed task)",
        goal: str = "(No goal provided)",
        desc: str = "(No description provided)",
    ) -> None:
        """"""
        self.__id: str = self.setid()
        self.name: str = name
        self.goal: str = goal
        self.desc: str = desc
        self.isstarted: bool = False
        self.isfinished: bool = False
        self.plan: list[date, date] = [None, None]
        self.duration: list[date, date] = [None, None]
        self.parentof: list = []
        self.childof: list = []

    def __str__(self) -> str:
        return self.name

    def info(self) -> dict:
        return {"type": "Task", "name": self.name, "goal": self.goal, "id": self.__id}

    def setid(self) -> str:
        from random import choices
        from string import ascii_letters, digits

        l = ascii_letters + digits + "-_."
        return "tk-" + "".join(choices(l, k=12))

    def showid(self) -> str:
        return self.__id


if __name__ == "__main__":
    taska = Task("A task", "A goal", "A description")
    taskb = Task("Bnother task", "Bnother goal", "Bnother description")
    proja = Project("A project", "A goal", "A description")
    projb = Project("Bnother project", "Bnother goal", "Bnother description")
    usera = User("Sato Tailor")
    userb = User("Suzuki Gyro")
