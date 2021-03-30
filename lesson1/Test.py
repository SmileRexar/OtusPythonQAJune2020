import pandas as pd
import time

import numpy as np
from numba import njit

df = pd.DataFrame(np.random.randn(10000000,8)+452)

print(df)

df.columns = ['C', 'd', 'A', 'E', 'B', 'Q', 'W', 'T']

def divide(a, b):
    if b == 0:
        return 0.0
    return float(a)/b

@njit
def div(a, b):
    res = np.empty(a.shape)
    for i in range(len(a)):
        if b[i] != 0:
            res[i] = a[i] / b[i]
        else:
            res[i] = 0
    return res

np.random.seed(0)
N = 10**5

start_time = time.time()
#[divide(row['A'], row['B']) for _, row in df[['A', 'B']].iterrows()]
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
np.vectorize(divide)(df['A'], df['B'])
print("---vectorize %s seconds ---" % (time.time() - start_time))

start_time = time.time()
list(map(divide, df['A'], df['B']))
print("--- map %s seconds ---" % (time.time() - start_time))


start_time = time.time()
div(df['A'].values, df['B'].values)
print("---njit %s seconds ---" % (time.time() - start_time))


start_time = time.time()
[divide(a, b) for a, b in df[['A', 'B']].itertuples(index=False)]
print("---itertuples %s seconds ---" % (time.time() - start_time))