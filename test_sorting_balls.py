from rack import Rack
from sorting_balls import inc


def test_rack():
    rack = Rack()
    rack.add(10)

    assert rack.balls() == [10] 