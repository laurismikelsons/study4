import testing_target
import unittest

class TestTestingTarget(unittest.TestCase):
  def test_sum (self):
    result = testing_target.sum(10,5)
    self.assertEqual(result, 15)
