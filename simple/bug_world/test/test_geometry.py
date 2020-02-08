import unittest

from geometry import Point, Vector

class TestGeometry(unittest.TestCase):
  def test_point_distance(self):
    _DIM = [10, 10]
    p1 = Point(0, 0, _DIM)
    p2 = Point(3, 4, _DIM)
    self.assertEqual(p1.distance_to(p2), 5)
    self.assertEqual(p2.distance_to(p1), 5)


if __name__ == "__main__":
  unittest.main()
