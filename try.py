class abc():
    def __init__(self, a):
        self._a = a
        self._b = 0
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, a):
        self._a = a
        self._b = self._a * 5

c = abc(3)
c._a = 5
print(c._a)