import numpy as np
from jedi.plugins import pytest


def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    product = np.prod(data)
    return mean, median, product

def test_calculate_statistics():
    data = [10, 20, 30, 40, 50]
    mean, median, product = calculate_statistics(data)

    assert np.isclose(mean, 30.0)
    assert np.isclose(median, 30.0)
    assert np.isclose(product, 12000000)


def test_single_value():
    data = [123]
    mean, median, product = calculate_statistics(data)

    assert np.isclose(mean, 123.0)
    assert np.isclose(median, 123.0)
    assert np.isclose(product, 123.0)


if __name__ == "__main__":
    pytest.main()