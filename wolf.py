import math
class partical():
    def __init__(self, A):
        self._A = A

        temp_fit = 0
        for x in self._A:
            temp_fit += x
        self._fit = temp_fit   
        self._pbfit = None
        if self._pbfit:
            if self._pbfit > self._fit:
                self._pbfit = self._fit
        else:
            self._pbfit = self._fit
        self._density = 2
        self._lenth = 5

    @property
    def A(self):
        return self._A
    @A.setter
    def A(self, A):
        self._A = A