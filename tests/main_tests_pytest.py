"""Tests using pytest"""
from main import get_six_random_numbers


def test_get_six_random_numbers():
    """Simple test of get_six_random_numbers function."""
    rand_numbers = get_six_random_numbers()
    for _ in range(500):
        assert len(rand_numbers) == 6
        assert rand_numbers[0] >= 1
        assert rand_numbers[-1] <= 49
