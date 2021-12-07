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
class Lanterns:
    def __init__(self, items: List[Lantern]):
        self.items = items
        self.ticks = 0
    def __repr__(self):
        return f'After {self.ticks} days: {self.items}'
    def __str__(self):
        return f'After {self.ticks} days: {self.items}'
    def tick(self):
        newboarns = []
        for it in self.items:
            baby = it.tick()
            if baby is not None:
                newboarns.append(baby)
        self.items.extend(newboarns)
        self.ticks += 1
    def count(self):
        return len(self.items)

def execute(filename: str, days: int):
    with open(filename, 'r') as f:
        line = f.readline()
        items = list(map(Lantern, map(int, line.split(','))))
    lanterns = Lanterns(items)
    print(lanterns)
    for day in range(days):
        lanterns.tick()
        # print(lanterns)
    print(lanterns.count())
    return lanterns.count()

if __name__ == '__main__':
    execute('input1.txt', 80)
