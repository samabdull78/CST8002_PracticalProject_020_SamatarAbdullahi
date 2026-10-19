# Author: Samatar Ali Abdullahi
# Reference:
#[2]
#“Unit testing in Python: Quick tutorial and 4 best practices,” Octopus.com, 2026. https://octopus.com/devops/unit-testing/unit-testing-in-python/ 
# (accessed Oct. 10, 2026).
#Professor: Stanley Pieda

"""Displaying a sucessful test and a unsucessful test"""

import unittest

from shapes.square import area


class TestSquareArea(unittest.TestCase):
    """Test a square's area calculation using unittest."""

    def test_01_expected_value(self):
        """Pass because the expected value matches the actual area."""
        actual = area(4, 4)
        self.assertEqual(actual, 16)

    def test_02_incorrect_expected_value(self):
        """This test fails because the values are purposefully wrong."""
        actual = area(4, 4)
        self.assertEqual(actual, 32)