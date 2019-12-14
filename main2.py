from wolf import partical
from os.path import isfile
import random
import numpy as np
import math
total_iter = 1000
def get_key(w):
    return (w._fit)
def import_files(wolfs):
    #讀取最大應力 位移
    for wolf, count in zip(wolfs, range(len(wolfs))):
        file_disp = open('DISP_{}.txt'.format(str(count)), 'r')
        file_strs = open('S{}.txt'.format(str(count)), 'r')
        disp = file_disp.read()
        strs = file_strs.read()
        file_disp.close()
        file_strs.close()
        wolf._u = float(disp)
        wolf._strs = float(strs)
        wolf.fit(count)#*****************************************
    return wolfs


def bad_fit(wolfs, wolf):
    a = [random.randint(0, len(wolfs) - 1) for _ in range(3)]
    tempa = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[a[0]]._A]) - np.array([wolf._A]))
    tempb = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[a[1]]._A]) - np.array([wolf._A]))
    tempc = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[a[2]]._A]) - np.array([wolf._A]))
    
    sa = 2
    ba = [sa * 2 * random.random() - sa for _ in range(3)]
    tempa = np.array(wolfs[a[0]]._A - ba[0] * tempa)
    tempb = np.array(wolfs[a[1]]._A - ba[1] * tempb)
    tempc = np.array(wolfs[a[2]]._A - ba[2] * tempc)

    tempfinal = (tempa + tempb + tempc) / 3
    tempfinal = tempfinal.tolist()
    for n, x in enumerate(tempfinal[0]):
        if x < 0.1:
            tempfinal[0][n] = 0.1
        elif x > 26:
            tempfinal[0][n] = 26
    return partical(tempfinal[0])
    #partical
    
def nice_fit(wolfs, wolf, iter_times):
    tempa = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[0]._A]) - np.array([wolf._A]))
    tempb = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[1]._A]) - np.array([wolf._A]))
    tempc = np.abs(np.random.random((1, 10)) * 2 * np.array([wolfs[2]._A]) - np.array([wolf._A]))

    sa = 2 * (1 - (iter_times**2) / total_iter**2)
    ba = [sa * 2 * random.random() - sa for _ in range(3)]
    tempa = np.array(wolfs[0]._A - ba[0] * tempa)
    tempb = np.array(wolfs[1]._A - ba[1] * tempb)
    tempc = np.array(wolfs[2]._A - ba[2] * tempc)

    tempfinal = (1.5 * tempa + 1.3*tempb + tempc)/(1.5 + 1.3 + 1) + 0.3 * np.random.random((1, 10)) * np.array(wolf._pbest)
    tempfinal = tempfinal.tolist()
    for n, x in enumerate(tempfinal[0]):
        if x < 0.1:
            tempfinal[0][n] = 0.1
        elif x > 26:
            tempfinal[0][n] = 26
    return partical(tempfinal[0])
    #partical

def update(wolfs):
    #檢查迭代次數
    if not isfile('iter_times.txt'):
        with open('iter_times.txt', 'w') as file:
            iter_times = 1
            file.write(str(iter_times))
    else:
        with open('iter_times.txt', 'r+') as file:
            iter_times = int(file.read()) + 1
        with open('iter_times.txt', 'w') as file:
            file.write(str(iter_times))
    temp_wolfs = wolfs[0: 3]
    total_fit = 0
    for w in wolfs:
        total_fit += w._fit
    average_fit = total_fit / len(wolfs)
    for w in wolfs[3: ]:
        if w._fit > average_fit:
            temp_wolf = bad_fit(wolfs, w)
            
        else:
            temp_wolf = nice_fit(wolfs, w, iter_times)
        
        temp_wolfs.append(temp_wolf)
    return temp_wolfs




def main():
    number = 30
    wolfs = []
    #讀取粒子
    for x in range(number):
        wolf = []
        with open('partical{}.txt'.format(str(x)), 'r') as file:
            lines = file.readlines()
            for line in lines:
                wolf.append(float(line))
            wolf = partical(wolf)
            wolfs.append(wolf)
    #計算適應值
    wolfs = import_files(wolfs)
    #排列
    wolfs.sort(key=get_key)
    #紀錄pbest 
    for x, count in zip(wolfs, range(len(wolfs))):
        with open('pbest{}.txt'.format(str(count)), 'w') as file:
            for xp in x._pbest:
                file.write('{}\n'.format(xp))
            file.write('{}\n'.format(x._pbestfit))
    
    wolfs = update(wolfs)
    
    #寫入新粒子
    for x, count in zip(wolfs, range(len(wolfs))):
        file = open('partical{}.txt'.format(str(count)), 'w+')
        for y in x._A:
            file.write('{}\n'.format(y))
        file.close()


if __name__ == '__main__':
    main()