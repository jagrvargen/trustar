#!/usr/bin/env python3
"""
   Contains unit tests for the flatten function.
"""
import unittest
from flatten import flatten


class TestFlatten(unittest.TestCase):
    """ A series of tests for the flatten function. """

    def test_no_non_lists(self):
        """ Tests that non-lists cannot be passed as initial parameter. """
        with self.assertRaises(TypeError):
            flatten(1)
            flatten("hi")
            flatten({"1": 2})
            flatten((1, 2))

    def test_no_non_ints(self):
        """ Tests that non-integers are not returned. """
        with self.assertRaises(TypeError):
            flatten([1, "hi", 2])
        with self.assertRaises(TypeError):
            flatten([[1.0], [6], [6.0]])
        with self.assertRaises(TypeError):
            flatten([1, (1, 2)])

    def test_array(self):
        """ Tests various types of nested arrays. """
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([0, [[2, 3], [[4, 5]], 6]]), [0, 2, 3, 4, 5, 6])
        self.assertEqual(flatten([[1, 2, [3]], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten([[[[[[7]]]]]]), [7])
        self.assertEqual(flatten([999999999999999]), [999999999999999])
