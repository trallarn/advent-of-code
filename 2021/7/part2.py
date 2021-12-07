import numpy as np
import pandas as pd

def distance_to_fuel(distance: float) -> float:
    sum = 0
    for i in range(1, int(distance) + 1):
        sum += i
    return sum


lines = []
with open('input.txt', 'r') as f:
    line = f.readline()
    for line in line.split(','):
        lines.append(float(line))

df: pd.DataFrame = pd.DataFrame(lines, columns=['input'])

min = df['input'].min()
max = df['input'].max()

distances = []
for i in range(int(min), int(max + 1)):
    df['distance'] = (df['input'] - i).abs()
    fuel = df['distance'].map(distance_to_fuel).sum()
    distances.append({
        'index': i,
        'fuel': fuel
    })

df_sum: pd.DataFrame = pd.DataFrame(data=distances)

res = df_sum[df_sum['fuel'] == df_sum['fuel'].min()]
print(res)
