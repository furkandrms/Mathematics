"""Test functions of the metric space functions written in this file will be added."""

import unittest
from MetricSpaces import MetricSpace
import numpy as np 


class TestMetricSpace(unittest.TestCase): 

    def setUp(self): 
        """Create a metric space instance for testing"""

        self.metric_space = MetricSpace(n_points=10)

    def test_euclidean_distance(self): 
        point1 = np.array([0,0])
        point2 = np.array([3,4])
        expected_distance = 5
        calculated_distance = self.metric_space.euclidean_distance(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)

    def test_manhattan_distance(self): 
        point1 = np.array([0,0])
        point2 = np.array([3,4])
        expected_distance = 7
        calculated_distance = self.metric_space.manhattan_distance(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)

    def test_minkowski_distance(self): 
        point1 = np.array([0,0])
        point2 = np.array([3,4])
        p = 3
        expected_distance = 4.497941445275415
        calculated_distance = self.metric_space.minkowski_distance(point1,point2,p)
        self.assertEqual(expected_distance, calculated_distance)
    
    def test_distance_matrix(self): 
        expected_shape = (10,10)
        matrix = self.metric_space.distance_matrix()
        self.assertEqual(matrix.shape, expected_shape)

    def test_d1(self): 
        point1 = 1
        point2 = 2
        expected_distance = 1
        calculated_distance = self.metric_space.d1(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)
    
    def test_d2(self):
        point1 = 1
        point2 = 2
        expected_distance = 0.5
        calculated_distance = self.metric_space.d2(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)

    def test_d3(self):
        point1 = 1
        point2 = 2
        expected_distance = 1
        calculated_distance = self.metric_space.d3(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)
    def test_d4(self):
        point1 = np.array([0, 0])
        point2 = np.array([3, 4])
        expected_distance = np.log(1 + 5)  # For distance d4 (0,0) and (3,4)
        calculated_distance = self.metric_space.d4(point1, point2)
        self.assertAlmostEqual(calculated_distance, expected_distance)

    def test_d5(self):
        point1 = np.array([0, 0])
        point2 = np.array([3, 4])
        expected_distance = min(1, 5)  # For distance d4 (0,0) and (3,4)
        calculated_distance = self.metric_space.d5(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)


if __name__ == "__main__": 
    unittest.main() 

