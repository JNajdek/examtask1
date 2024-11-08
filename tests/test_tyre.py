"""
Module for testing the functionality of the methods and properties of the 'Tyre' class.

Author: Jakub Najdek
Date: 2023-11-06
Version: 1.0
"""

import pytest

from circles.tyre import Tyre


@pytest.fixture
def tyre():
    """
    Fixture for creating a Tyre object with specific attributes.
    Returns:
        Tyre: A Tyre object with radius 130 and the tyre label "123/21R21"
    """
    tyre = Tyre(130, "123/21R21")
    return tyre


def test_correct_arguments(tyre):
    """
    Tests tire initialization from fixture and verifies its properties.

    Parameters:
        tyre (Tyre): A tyre object created from a fixture.
    """
    assert tyre.tyre_size == 123
    assert tyre.get_necessary_ring_diameter() == 21


def test_incorrect_arguments():
    """
    Tests various invalid Tyre initialization arguments and exception handling.
    """
    # testing non string arg
    with pytest.raises(ValueError):
        Tyre(130, 123)
    # testing without slash
    with pytest.raises(ValueError):
        Tyre(130, "123?21R21")
    # testing without R
    with pytest.raises(ValueError):
        Tyre(130, "123/21T21")
    # testing non numeric values
    with pytest.raises(ValueError):
        Tyre(130, "AAA/BBRCC")
