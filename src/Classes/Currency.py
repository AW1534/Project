import math


class Currency:
    integer: int
    decimal: int

    def __init__(self, num: float | int = 0):
        self.integer = int(math.floor(num))
        self.decimal = int(str(float(num)).split(".")[1])

    def __float__(self) -> float:
        return float(f"{self.integer}.{self.decimal}")

    def __int__(self) -> int:
        return int(round(float(self)))

    def __str__(self) -> str:
        return str(float(self))

    def __add__(self, other):
        return Currency(float(self) + float(other))

    def __sub__(self, other):
        return Currency(float(self) - float(other))

    def __truediv__(self, other):
        return float(self) / float(other)

    def __floordiv__(self, other):
        return float(self) // float(other)

    def __mul__(self, other):
        return Currency(float(self) * float(other))

    def __abs__(self):
        return Currency(abs(float(self)))

    def __eq__(self, other: object | float | int):
        return (self.integer == other.integer and self.decimal == other.decimal) if isinstance(other, Currency) else float(other) == float(self)

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return float(self) <= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __floor__(self):
        return Currency(self.integer)

    def __ceil__(self):
        return Currency(math.ceil(float(self.integer)))

    def __pow__(self, power, modulo=None):
        pow(float(self), power, modulo)

    def __round__(self, n=None):
        return round(float(self), n)
