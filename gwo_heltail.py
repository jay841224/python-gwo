import numpy as np
from os.path import isfile
import random
total_iter = 100
min = 0.06
max = 1.5

bars = 18
class partical:
    def __init__(self, A=np.zeros((1, bars))):
        self.fits = 0
        self.A = A
        self.density = 0.1

        
        self.pbest = None
        self.pbest_fit = None

    def start(self):
        wolf = [min + np.random.random() * (max - min) for _ in range(bars)]
        self.A = np.array(wolf)

    def get_fit(self, count):
        file_disp = open('DISP_{}.txt'.format(str(count)), 'r')
        file_strs = open('fre{}.txt'.format(str(count)), 'r')
        disp = file_disp.read()
        strs = file_strs.read()
        file_disp.close()
        file_strs.close()
        u = float(disp)
        strs = float(strs)

        #read the bars lenth
        length = []
        with open('Length.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                length.append(line)
        
        tempfit = 0  
        le = [4, 8, 6]   #檢查此處!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        A = []
        for i, a in enumerate(self.A):
            A += [a]*le[i%3]
        self.A = A
        for x, y in zip(self.A, length):
            y = float(y)
            tempfit += self.density * x * y
        self.fits = tempfit + 1000 * (0.5 - np.abs(u))**2 + (np.abs(strs) - 29) * 100

    def get_pbest_and_pbestfit(self, count):
        if isfile('pbest0.txt'):
            with open('pbest{}.txt'.format(str(count)), 'r') as file:
                lines = file.readlines()
                lines = list(map(lambda x:float(x), lines))#let list(string) to list(float)
                if self.fits < lines[-1]:
                    self.pbest = self.A
                    self.pbest_fit = self.fits
                else:
                    self.pbest_fit = lines[-1]
                    self.pbest = np.array(lines[: -1])
        else:
            self.pbest = self.A
            self.pbest_fit = self.fits

    def write_best_file(self, count):
        with open('pbest{}.txt'.format(str(count)), 'w') as file:
            for xp in self.pbest:
                file.write('{}\n'.format(xp))
            file.write('{}\n'.format(self.pbest_fit))

    def write_new_partical_file(self, count):
        with open('partical{}.txt'.format(str(count)), 'w+') as file:
            for x in self.A:
                file.write('{}\n'.format(x))




def bad_fit(wolfs, wolf):
    a = [random.randint(0, len(wolfs) - 1) for _ in range(3)]
    tempa = np.abs(np.random.random((1, bars)) * 2 * [wolfs[a[0]].A] - [wolf.A])
    tempb = np.abs(np.random.random((1, bars)) * 2 * [wolfs[a[1]].A] - [wolf.A])
    tempc = np.abs(np.random.random((1, bars)) * 2 * [wolfs[a[2]].A] - [wolf.A])
    
    sa = 2
    ba = [sa * 2 * random.random() - sa for _ in range(3)]
    tempa = wolfs[a[0]].A - ba[0] * tempa
    tempb = wolfs[a[1]].A - ba[1] * tempb
    tempc = wolfs[a[2]].A - ba[2] * tempc

    tempfinal = (tempa + tempb + tempc) / 3
    tempfinal = tempfinal.tolist()
    for n, x in enumerate(tempfinal[0]):
        if x < min:
            tempfinal[0][n] = min
        elif x > max:
            tempfinal[0][n] = max
    return partical(np.array(tempfinal[0]))
    #partical
    
def nice_fit(wolfs, wolf, iter_times):
    tempa = np.abs(np.random.random((1, bars)) * 2 * [wolfs[0].A] - [wolf.A])
    tempb = np.abs(np.random.random((1, bars)) * 2 * [wolfs[1].A] - [wolf.A])
    tempc = np.abs(np.random.random((1, bars)) * 2 * [wolfs[2].A] - [wolf.A])

    sa = 2 * (1 - (iter_times**2) / total_iter**2)
    ba = [sa * 2 * random.random() - sa for _ in range(3)]
    tempa = wolfs[0].A - ba[0] * tempa
    tempb = wolfs[1].A - ba[1] * tempb
    tempc = wolfs[2].A - ba[2] * tempc

    tempfinal = (1.5 * tempa + 1.3*tempb + tempc)/(1.5 + 1.3 + 1)# + 0.3 * np.random.random((1, bars)) * np.array(wolf._pbest)
    tempfinal = tempfinal.tolist()
    for n, x in enumerate(tempfinal[0]):
        if x < min:
            tempfinal[0][n] = min
        elif x > max:
            tempfinal[0][n] = max
    return partical(np.array(tempfinal[0]))
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
    #temp_wolfs = []
    total_fit = 0
    for w in wolfs:
        total_fit += w.fits
    average_fit = total_fit / len(wolfs)
    for w in wolfs[3: ]:
    #for w in wolfs:
        if w.fits > average_fit:
            temp_wolf = bad_fit(wolfs, w)
            
        else:
            temp_wolf = nice_fit(wolfs, w, iter_times)
        
        temp_wolfs.append(temp_wolf)
    return temp_wolfs



def getkey(w):
    return(w.fits)

def main():
    number = 30
    
    wolfs = []
    #read particals from txt
    for x in range(number):
        with open('partical{}.txt'.format(str(x)), 'r') as file:
            lines = file.readlines()
            lines = list(map(lambda x:float(x), lines))#let list(string) to list(float)
            wolf = partical(np.array(lines))
            wolfs.append(wolf)
    
    for count, wolf in enumerate(wolfs):
        wolf.get_fit(count)#calculate fit
        wolf.get_pbest_and_pbestfit(count)

    wolfs.sort(key=getkey) #sort by fit from small to big

    for count, wolf in enumerate(wolfs):
        wolf.write_best_file(count)

    wolfs = update(wolfs)

    for count, wolf in enumerate(wolfs):
        wolf.write_new_partical_file

if __name__ == '__main__':
    main()