import pandas as pd
from typing import List

class Lantern:
    def __init__(self, days: int):
        self.days = days
    def __str__(self):
        return f'{self.days}'
    def __repr__(self):
        return f'{self.days}'
    def tick(self):
        old_days = self.days
        newborn = None
        if self.days == 0:
            self.days = 6
            newborn = Lantern(8)
        else:
            self.days -= 1
        return newborn
class Group:
    def __init__(self, days):
        self.days = days
        self.num_lanterns = 0
    def add(self, num: int):
        self.num_lanterns += num
    def remove(self):
        self.num_lanterns -= 1
    def __str__(self):
        return repr(self)
    def __repr__(self):
        return str(list(self.num_lanterns * str(self.days)))
class Lanterns:
    def __init__(self, items: List[Lantern]):
        self.ticks = 0
        self.groups: List[Group] = self._create_groups()
        self._add_to_groups(items)
    def _add_to_groups(self, lanters: List[Lantern]):
        for lantern in lanters:
            self.groups[lantern.days].add(1)
    def _remove_from_groups(self, lanters: List[Lantern]):
        for lantern in lanters:
            self.groups[lantern.days].remove()
    def _create_groups(self):
        return [Group(i) for i in range(9)]
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        groups_str = [g for g in self.groups]
        return f'After {self.ticks} days: {groups_str}'
    def tick(self):
        new_groups = self._create_groups()
        for i in range(len(self.groups)):
            group = self.groups[i]
            next_days = i - 1
            if i == 0:
                new_groups[8].add(group.num_lanterns)
                next_days = 6
            new_groups[next_days].add(group.num_lanterns)
        self.groups = new_groups
        self.ticks += 1
    def count(self):
        return sum(map(lambda x: x.num_lanterns, self.groups))


def execute(filename: str, days: int):
    with open(filename, 'r') as f:
        line = f.readline()
        items = list(map(Lantern, map(int, line.split(','))))
    lanterns = Lanterns(items)
    print(lanterns)
    for day in range(days):
        lanterns.tick()
        print(f'Num lanterns: {lanterns.count()}')
    print(f'After {days} days: {lanterns.count()}')
    return lanterns.count()

if __name__ == '__main__':
    filename = 'input1.txt'
    days = 256
    execute(filename, days)
