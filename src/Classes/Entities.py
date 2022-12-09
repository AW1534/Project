from enum import Enum

from src.Classes.Vector2 import Vector2

import pyray as rl


# region primary class (Entity)

class Shape(Enum):
    SQUARE = 1
    CIRCLE = 0
    TRIANGLE = 2


class Entity:
    name: str
    idt: int

    scale: int = 1
    color: tuple = rl.WHITE
    shape: Shape = Shape.CIRCLE

    base_max_health: int = 6
    max_health: int = base_max_health
    health: int = max_health

    base_damage: int = 1
    damage: int = base_damage

    base_speed: int = 100
    speed: int = base_speed

    enabled: bool = True
    position: Vector2 = Vector2(0, 0)

    def __init__(self, position: Vector2 = Vector2(0, 0), enabled=True):
        self.position = position
        self.enabled = enabled

    def __str__(self) -> str:
        return self.name

    def __int__(self):
        return self.idt

    def __eq__(self, other) -> bool:
        return self.idt == other.idt

    def __ne__(self, other) -> bool:
        return not self.idt == other.idt

    def __bool__(self) -> bool:
        return self.enabled

    def __vec2__(self) -> Vector2:
        return Vector2(self.position.x, self.position.y)

    def mod_health(self, heal: int) -> int:
        ph = self.health
        th = self.health + heal

        if th > self.max_health:
            self.health = self.max_health

        elif th < self.max_health:
            self.health = 0

        return abs(self.health - ph)

    def draw(self):
        print(self.shape)
        match self.shape:
            case Shape.SQUARE:
                rl.draw_rectangle(
                    self.position.x,
                    self.position.y,
                    self.scale,
                    self.scale,
                    rl.Color(*self.color)
                )

            case Shape.CIRCLE:
                rl.draw_circle(
                    self.position.x,
                    self.position.y,
                    self.scale,
                    rl.Color(*self.color)
                )

            case Shape.TRIANGLE:
                rl.draw_triangle(
                    rl.Vector2(*(Vector2(0, -self.scale) + self.position).tuple()),
                    rl.Vector2(*(Vector2(self.scale, -self.scale) + self.position).tuple()),
                    rl.Vector2(*(Vector2(-self.scale, -self.scale) + self.position).tuple()),
                    rl.Color(*self.color)
                )


# endregion primary class

# region secondary classes (Entity Types)

class NpcMode(Enum):
    NEUTRAL = 0
    FRIENDLY = 1
    HOSTILE = 2


class NpcType(Enum):
    OTHER = 0
    VENDOR = 1
    ACCESS = 2
    ENEMY = 3
    GUIDE = 4


class Npc(Entity):
    target_pos: Vector2 = None
    mode: int = NpcMode.NEUTRAL
    type: int = NpcType.OTHER

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Player(Entity):
    name: str
    idt: int

    scale: int
    color: tuple
    shape: Shape

    health: int
    max_health: int
    base_max_health: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.inventory: list[object] = kwargs["inventory"] if "inventory" in kwargs.keys() else []


# endregion secondary classes

# region tertiary classes (Individual Entities)
"""       
    self.name = name
    self.idt = idt
    self.scale = scale
    self.color = color

    self.shape = shape
    self.health = self.max_health = self.base_max_health = base_max_health
    self.speed = speed
    self.damage = self.base_damage = base_damage
    self.position = position
    self.enabled = enabled
"""


class Headteacher(Npc):
    name: str = "Mr McNaughton"
    idt: int = 1

    scale: int = 1
    color: tuple = rl.WHITE
    shape: Shape = Shape.CIRCLE

    health: int = 150
    max_health: int = health
    base_max_health: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EnglishT(Npc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MathT(Npc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ScienceT(Npc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HistoryT(Npc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GeographyT(Npc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# endregion tertiary classes
