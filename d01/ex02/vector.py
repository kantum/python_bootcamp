class Vector:
    def __init__(self, param=0):
        self.values = []
        self.length = 0
        if isinstance(param, tuple):
            if len(param) == 2:
                self.length = param[1] - param[0]
                for i in range(param[0], param[1]):
                    self.values.append(float(i))
            else:
                raise ValueError("ERROR, range do not have 2 int")
        elif isinstance(param, int):
            self.length = param
            for i in range(self.length):
                self.values.append(float(i))
        elif isinstance(param, list):
            self.values = param
            self.length = len(param)
        else:
            self.values = []
            self.length = 0

    def __str__(self):
        txt = "{:s} ({:d}) [".format(self.__class__.__name__, self.length)
        txt += ', '.join(map(str, self.values))
        txt += ']'
        return txt

    def __repr__(self):
        txt = "'{:s}([".format(self.__class__.__name__)
        txt += ", ".join(map(str, self.values))
        txt += "])'"
        return txt

    def __add__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] + other)
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] + other.values[i])
            return tmp
        else:
            raise ValueError("ERROR, __add__ failed")

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] + other)
            return tmp
        if (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(other.values[i] + self.values[i])
            return tmp
        else:
            raise ValueError("ERROR, __radd__ failed")

    # add : scalars and vectors, can have errors with vectors.
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] - other)
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(self.values[i] - other.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __sub__ failed")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(other - self.values[i])
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(other.values[i] - self.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __rsub__ failed")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] / other)
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(self.values[i] / other.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __truediv__ failed")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(other / self.values[i])
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(other.values[i] / self.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __rtruediv__ failed")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(self.values[i] * other)
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(self.values[i] * other.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __mul__ failed")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(other * self.values[i])
            return tmp
        elif (self.length == other.length):
            tmp = Vector()
            tmp.length = self.length
            tmp.values = []
            for i in range(self.length):
                tmp.values.append(round(other.values[i] * self.values[i]))
            return tmp
        else:
            raise ValueError("ERROR, __rmul__ failed")
