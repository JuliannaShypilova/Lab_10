class Rational:
    def __init__(self, a, b=None):
        if isinstance(a, Rational):
            self.n = a.n
            self.d = a.d
        elif isinstance(a, str):
            if '/' in a:
                self.n, self.d = map(int, a.strip().split('/'))
            else:
                self.n = int(a.strip())
                self.d = 1
        elif isinstance(a, int):
            if b is None:
                self.n = a
                self.d = 1
            else:
                self.n = a
                self.d = b
        else:
            raise TypeError("Не належить до класу Rational")

        if self.d == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")

        self._reduce()

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, Rational):
            nom = self.n * other.d + self.d * other.n
            denom = self.d * other.d
            return Rational(nom, denom)
        elif isinstance(other, int):
            return Rational(self.n + other * self.d, self.d)
        else:
            raise TypeError("Цей тип непідтримуваний  для додавання")

    def __sub__(self, other):
        if isinstance(other, Rational):
            nom = self.n * other.d - self.d * other.n
            denom = self.d * other.d
            return Rational(nom, denom)
        elif isinstance(other, int):
            return Rational(self.n - other * self.d, self.d)
        else:
            raise TypeError("Цей тип непідтримуваний  для віднімання")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        elif isinstance(other, int):
            return Rational(self.n * other, self.d)
        else:
            raise TypeError("Цей тип непідтримуваний  для множення")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError("Ділення на 0")
            nom = self.n * other.d
            denom = self.d * other.n
            return Rational(nom, denom)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Ділення на 0")
            return Rational(self.n, self.d * other)
        else:
            raise TypeError("Цей тип непідтримуваний  для ділення")

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _reduce(self):
        g = self._gcd(abs(self.n), abs(self.d))
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Ключ повинен бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ValueError("Знаменник не може дорівнювати нулю")
            self.d = value
        else:
            raise KeyError("Ключ повинен бути 'n' або 'd'")

if __name__ == "__main__":
    r1 = Rational(1, 2)
    print(r1)

    r2 = Rational(r1)
    print(r2)

    r3 = Rational(2)
    print(r3)

    r4 = Rational("2/3")
    print(r4)

    r5 = Rational(6, 8)
    print(r5)