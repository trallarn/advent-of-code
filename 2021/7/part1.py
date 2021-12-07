import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lines = []
with open('input.txt', 'r') as f:
    line = f.readline()
    for line in line.split(','):
        lines.append(float(line))

df: pd.DataFrame = pd.DataFrame(lines, columns=['input'])

min = df['input'].min()
max = df['input'].max()

distances = []
for i in range(int(min), int(max + 2)):
    dist = (df['input'] - i).abs().sum()
    distances.append({
        'index': i,
        'distance': dist
    })

df_sum: pd.DataFrame = pd.DataFrame(data=distances)

res = df_sum[df_sum['distance'] == df_sum['distance'].min()]
print(res)

#df_sum.plot()
#plt.show()
