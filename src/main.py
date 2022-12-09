import pyray as r

from src.Classes.Entities import *

# "Beckham and I did the work for you, because you guys are lazy and didn't join the discord server or
# didn't join the voice call. We didn't use Pygame like a group of pussies, we used raylib (https://www.raylib.com/)
# and its Python bindings. Would've used C# or C++ (the good languages) but you guys are python kiddies. have a nice
# time using the framework we created"
# - Andrew, creator of https://github.com/AW1534/NeutronEngine

# "fuck you, except for josh"
# - Beckham, co-creator of https://github.com/AW1534/rpgtogether

# "i love men"
# - probably Josh, lover of men

# "insert quote here"
# - probably Karina, cs student

entities: list[Entity] = []
entities.append(Player())

timestamp = 1669507200

r.init_window(800, 450, "Hello")
while not r.window_should_close():
    timestamp += r.get_frame_time() * 10

    r.begin_drawing()
    r.clear_background(r.BLACK)
    [e.draw() for e in entities if e.enabled]

    # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    # -------------------
    # https://docs.python.org/3/tutorial/datastructures.html
    # This is a list comprehension.
    # It is equivalent to te following:
    # -------------------
    # for e in entities:
    #    if e.enabled:
    #        e.draw()
    # ------------------

    r.end_drawing()
r.close_window()
