from wolf import partical
import random

def ran_partical(n):
    wolfs = []
    for _ in range(n):
        wolfs.append(0.1 + random.random() * 26)
    wolfs = partical(wolfs)
    return wolfs