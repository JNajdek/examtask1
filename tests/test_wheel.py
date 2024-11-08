"""
Module for testing the functionality of the methods and properties of the 'Wheel' class
and interactions between its components.

Author: Jakub Najdek
Date: 2023-11-06
Version: 1.0
"""

import pytest

from circles.pizza import Pizza
from circles.rim import Rim
from circles.tyre import Tyre
from circles.wheel import Wheel


@pytest.fixture
def wheel():
    """
    Fixture to create and return a Wheel instance constructed using a `Tyre` and `Rim` objects.

    Returns:
        Wheel: An instance of the `Wheel` class with specific `Tyre`
        and `Rim` parameters for testing purposes.
    """
    tyre = Tyre(800, "235/19R19")
    rim = Rim(241.3)
    wheel = Wheel(tyre, rim)
    return wheel


def test_verify_sizes(wheel):
    """
    Tests that the Wheel's verify_sizes method works correctly

    Args:
        wheel (Wheel): Fixture providing an instance of the Wheel class.
    """
    verified = wheel.verify_rim_size()
    assert verified is True

    # rim with incorrect radius value (doesn't match necessary_radius_size)
    # method cannot be tested directly as it uses wheel internal parameters.
    # The wheel class cannot be initialised because the verify_sizes method
    # is placed in __init__.

    # Tests if incorrect sizes causes an error
    tyre = Tyre(800, "235/19R10")
    rim = Rim(241.3)
    with pytest.raises(ValueError):
        Wheel(tyre, rim)


def test_change_tyre(wheel):
    """
    Tests that the change_tyre method successfully changes the Wheel's tyre when
    the tyre's diameter in inches matches the remaining rim's necessary_rim_size.

    Args:
        wheel (Wheel): Fixture providing an instance of the Wheel class.
    """
    other_tyre = Tyre(800, "250/19R19")
    old_tyre = wheel.tyre
    wheel.change_tyre(other_tyre)
    new_tyre = wheel.tyre
    assert old_tyre != new_tyre
    assert new_tyre == other_tyre


def test_change_tyre_incorrect_argument(wheel):
    """
    Tests the change_tyre method's exceptions handling

    Args:
        wheel (Wheel): Fixture providing an instance of the Wheel class.
    """
    other_tyre = Tyre(800, "250/19R10")
    with pytest.raises(ValueError):
        wheel.change_tyre(other_tyre)
    with pytest.raises(TypeError):
        wheel.change_tyre(Rim(241.3))


def test_change_rim(wheel):
    """
    Tests that the change_rim method can successfully change the Wheel's Rim when necessary_rim_size
    is equal to the new rim diameter in inches.

    Args:
        wheel (Wheel): Fixture providing an instance of the Wheel class.
    """
    other_rim = Rim(241.3)
    old_rim = wheel.rim
    # tests if new rim is suitable to the tyre
    assert int(round(other_rim.diameter_inches, 0)) == wheel.tyre.necessary_rim_size
    wheel.change_rim(other_rim)
    new_rim = wheel.rim
    # tests if the rim was changed
    assert old_rim != new_rim
    # tests if the new tyre in the wheel is the same as the tyre provided
    assert new_rim == other_rim


def test_change_rim_incorrect_argument(wheel):
    """
    Tests the change_rim method's exceptions handling

    Args:
        wheel (Wheel): Fixture providing an instance of the Wheel class.
    """
    other_rim = Rim(300)
    with pytest.raises(ValueError):
        wheel.change_rim(other_rim)
    with pytest.raises(TypeError):
        wheel.change_rim(Tyre(800, "250/19R19"))


def test_incorrect_types():
    """
    Tests that invalid types or values for Wheel initialization raise ValueError.
    """
    Pizza(20, ["cheese", "sauce", "peperoni"])
    tyre = Tyre(800, "235/19R19")
    rim = Rim(241.3)
    with pytest.raises(TypeError):
        pizza1 = Pizza(2, [])
        Wheel(tyre, pizza1)
    with pytest.raises(TypeError):
        Wheel(rim, tyre)
