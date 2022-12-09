import math
import pyray as rl

class Vector2:
    def __init__(self, x: int | float | object = 0, y: int | float = 0):
        try:
            v = x.__vec2__()
            self.x = v.x
            self.y = v.y

        except AttributeError:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> int:
        return(self.x * other.x) + (self.y * other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def __vec2__(self):
        return self

    def tuple(self) -> tuple:
        return self.x, self.y

    def set(self) -> set:
        return {self.x, self.y}

    def rl(self) -> rl.Vector2:
        return rl.Vector2(self.x, self.y)

    @property
    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    @property
    def normalized(self):
        mag = self.magnitude
        target_magnitude = 1

        return self if mag == 0 else Vector2(self.x * (target_magnitude / mag), self.y * (target_magnitude / mag))
