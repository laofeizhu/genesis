from geometry import Point, Vector
import pytest

def test_point_distance():
  _DIM = [10, 10]
  p1 = Point(0, 0, _DIM)
  p2 = Point(3, 4, _DIM)
  assert p1.distance_to(p2) == 5
  assert p2.distance_to(p1) == 5
