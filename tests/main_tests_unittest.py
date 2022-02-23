"""Tests using unittest"""

import unittest
from unittest.mock import patch


from main import get_six_random_numbers, how_many_draws_to_hit_six


class TestGetRandomSix(unittest.TestCase):
    """Simple tests of get_six_random_numbers function."""
    def test_get_six_random_numbers_return_list_type(self):
        """Test get_six_random_numbers return list type."""
        actual = get_six_random_numbers()
        self.assertTrue(type(actual), list)

    def test_get_six_random_numbers_return_list_with_six_elements(self):
        """Test get_six_random_numbers return return list with six elements."""
        self.assertEqual(len(get_six_random_numbers()), 6)

    def test_get_six_random_numbers_return_unique_numbers(self):
        """Test get_six_random_numbers contain only unique numbers."""
        actual = get_six_random_numbers()
        self.assertTrue(actual, set(actual))


class TestHowManyDrawsToHitSix(unittest.TestCase):
    """Simple tests of how_many_draws_to_hit_six function."""
    @patch('random.sample')
    def test_how_many_draws_to_hit_six(self, mock_get_six):
        """Check return value with mock numbers."""
        mock_get_six.return_value = [2, 5, 12, 23, 24, 46]
        actual = how_many_draws_to_hit_six()
        expected = f"Ilość losowań: 1, " \
                   f"koszt wszytskich losowań: 3 pln, " \
                   f"lata potrzebne żeby trafić 6: 0 lat"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
