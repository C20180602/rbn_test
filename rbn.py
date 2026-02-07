import json
import random as rd
import numpy as np 
n = 10
k = 2
step = 30
state = np.random.randint(0, 2, size=(n))
conn = np.random.randint(0, n, size=(n, k))
func = np.random.randint(0, 2, size=(n, int(pow(2,k))))

while True:
    for _ in range(step):
        print(state)
        new_state = []
        for i in range(n):
            bit = 0
            for j in range(k):
                bit = (bit<<1)|state[conn[i][j]]
            new_state.append(func[i][bit])
        state = np.array(new_state)
    pos = int(input("toggle pos:"))
    state[pos] ^= 1
