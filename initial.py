from wolf import partical
import random

def ran_partical(n):
    #bar 數量
    bar = 10
    wolfs = []
    for _ in range(n):
        wolf = []
        for _ in range(bar):
            wolf.append(0.1 + random.random() * 26)
        wolfs.append(partical(wolf))
    return wolfs