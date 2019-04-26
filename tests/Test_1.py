import pytest


from src.mypkg.Snake import snake
from src.mypkg.Snake import cube
from src.mypkg.Snake import randomMeal, randomPosion, randomBoost, randomSnack, main



def test_intial_location():
    s = snake((255, 0, 0), (10, 10))
    assert(s.body[0].pos == (10, 10))

def Snack():
    s = snake((255, 0, 0), (10, 10))
    rows = 20
    snack = cube(randomSnack(rows, s), color=(0, 0, 255))
    if s.body[0].pos == snack.pos:
        assert(len(s.body) == 2)


def Poison():
    s = snake((255, 0, 0), (10, 10))
    rows = 20
    poison = cube(randomPosion(rows, s), color=(0, 0, 255))
    if s.body[0].pos == poison.pos:
        assert(len(s.body) == 0)

def Meal():
    s = snake((255, 0, 0), (10, 10))
    rows = 20
    meal = cube(randomMeal(rows, s), color=(0, 0, 255))
    if s.body[0].pos == Meal.pos:
        assert(len(s.body) == 3)

def Boost():
    s = snake((255, 0, 0), (10, 10))
    rows = 20
    speed = 10
    Boost = cube(randomBoost(rows, s), color=(0, 0, 255))
    if s.body[0].pos == Boost.pos:
        assert(speed == 15)