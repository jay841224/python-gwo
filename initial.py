from wolf import partical
import random

def ran_partical(n):
    wolfs = []
    for _ in range(n):
        wolfs.append(-100 + random.random() * 100 * 2)
    wolfs = partical(wolfs)
    return wolfs