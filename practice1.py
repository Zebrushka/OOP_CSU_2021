# Задача 1. Родственные связи
# Напишите программу, которая моделирует родственные связи. Программа позволяет создать объекты типа Person
# и указывать, кто из людей кому является родителем и кто с кем состоит в браке.
#
# Должны быть функции, позволяющие для каждого человека получить список:
#   - Родителей
#   - Двоюродных братьев и сестер
#   - Дядюшек и тетушек
#   - In-laws (cвекра и свекрови или тестя и тещи)
from typing import Dict, List
from enum import Enum


class Relative(str, Enum):
    parent = 'parent'
    cousin = 'cousin'
    aunt = 'aunt'
    in_law = 'in_law'
    child = 'child'


class Person:
    family: Dict[Relative, List['Person']]

    def __init__(self, name):
        self.name = name
        self.family = {}

    def add_relative(self, person: 'Person', relation: Relative) -> None:
        if relation not in self.family:
            self.family[relation] = []
        self.family[relation].append(person)

    def _get_relatives(self, relation: Relative) -> List['Person']:
        return print(self.family[relation])

    def get_parents(self) -> List['Person']:
        return self._get_relatives(Relative.parent.value)

    def add_parent(self, person: 'Person') -> None:
        self.add_relative(person, Relative.parent.value)

    def add_cousin(self, person: 'Person') -> None:
        self.add_relative(person, Relative.cousin.value)

    def add_aunt(self, person: 'Person') -> None:
        self.add_relative(person, Relative.aunt.value)

    def add_in_law(self, person: 'Person') -> None:
        self.add_relative(person, Relative.in_law.value)

    def add_child(self, person: 'Person') -> None:
        self.add_relative(person, Relative.child.value)


if __name__ == '__main__':
    Sara = Person('Sara')
    Sara.add_cousin('Maria')
    Sara.add_aunt('Jack')
    Sara.add_in_law('Boris')
    Sara.add_parent('Olga')
    Sara._get_relatives('parent')

    Boris = Person('Boris')
    Boris.add_child('Vika')
    Boris.add_child('Sara')
    Boris._get_relatives('child')