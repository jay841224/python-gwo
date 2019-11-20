import math
from os.path import isfile
class partical():
    def __init__(self, A):
        self._A = A
        self._density = 0.1
        self._lenth = []
        #位移
        self._u = None
        #應力
        self._strs = None
        self._pbest = None
        self._fit = None
        self._pbestfit = None


    @property
    def A(self):
        return self._A
    @A.setter
    def A(self, A):
        self._A = A

    @property
    def u(self):
        return self._u
    @u.setter
    def u(self, u):
        self._u = u

    @property
    def strs(self):
        return self._strs
    @strs.setter
    def strs(self, strs):
        self._strs = strs

    def fit(self, count):
        temp_fit = 0
        #讀取桿件長度
        with open('Length.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                self._lenth.append(float(line))

        for x, y in zip(self._A, self._lenth):
            x = float(x)
            temp_fit += self._density * x * y + 100 * ((2 - self._u )**2 + (25 - self._strs)**2)
        self._fit = temp_fit
        
        if isfile('pbest0.txt'):
            with open('pbest{}.txt'.format(str(count)), 'r') as file:
                lines = file.readlines()
                if self._fit < float(lines[1]):
                    self._pbest = lines[0].split()
                    self._pbest = [float(i) for i in self._pbest]
                    self._pbestfit = float(lines[1])
                else:
                    self._pbest = self._A
                    self._pbestfit = self._fit
        else:
            self._pbest = self._A
            self._pbestfit = self._fit
            