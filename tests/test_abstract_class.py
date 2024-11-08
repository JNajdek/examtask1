"""
Module for testing the functionality of the methods and properties of the abstract class 'Circle'.
As it is not possible to test an abstract class directly, it is done using its subclasses

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
def child_classes():
    """
    This fixture sets up instances of the Pizza, Rim, Tyre, and Wheel subclasses for testing.
    It includes instances with both integer and float radius values to ensure compatibility
    across types. Different object types provide comprehensive coverage of different circle
    implementations in subclasses.

    Returns:
        list: A list of subclass instances of Circle, including various radius types.
    """
    objects = []
    # pizza doesn't contain the ingredients because we are testing circle class and its properties
    pizza_int = Pizza(2, [])
    objects.append(pizza_int)
    pizza_float = Pizza(2.0, [])
    objects.append(pizza_float)
    rim_int = Rim(12)
    objects.append(rim_int)
    rim_float = Rim(12.4)
    objects.append(rim_float)
    tyre_int = Tyre(130, "123/21R21")
    objects.append(tyre_int)
    tyre_float = Tyre(130.2, "123/21R21")
    objects.append(tyre_float)

    tyre_wheel = Tyre(800, "235/19R19")
    rim_wheel = Rim(241.3)
    wheel = Wheel(tyre_wheel, rim_wheel)
    objects.append(wheel)
    return objects


def test_arguments_correct_values(child_classes):
    """
    Tests that each subclass of Circle initializes correctly when provided with a valid
    radius (radius must be greater than zero) and verifies that the returned radius is accurate

    Args:
        child_classes (list): Fixture providing subclass instances.
    """
    # testing obj with correct arguments
    radiuses = [2, 2.0, 12, 12.4, 130, 130.2, 800]
    for obj, radius in zip(child_classes, radiuses):
        assert obj.get_radius() == radius


def test_arguments_incorrect_values():
    """
    Tests that invalid radius values (less or equal to zero) raise a ValueError
    when initializing Circle subclasses.
    """
    # testing abstract class with incorrect arguments using pizza example

    with pytest.raises(ValueError):
        Pizza(-2, [])

    with pytest.raises(ValueError):
        Pizza(0, [])


def test_arguments_correct_types(child_classes):
    """
    Tests that each subclass instance initializes correctly when given correct argument
    types (int, float) and maintains the same type of radius as initialized.

    Args:
        child_classes (list): Fixture providing subclass instances.
    """
    # testing if class returns the data in the same type as created
    types = [int, float, int, float, int, float, int]
    for obj, int_or_float in zip(child_classes, types):
        assert isinstance(obj.get_radius(), int_or_float)


def test_arguments_incorrect_types():
    """
    Tests that invalid radius types (for example str) raise a ValueError
    when initializing Circle subclasses.
    """

    with pytest.raises(TypeError):
        Pizza("2", [])

    with pytest.raises(TypeError):
        Pizza([1, 2], [])


def test_diameter(child_classes):
    """
    Tests that each subclass correctly calculates and returns its diameter.

    Args:
        child_classes (list): Fixture providing subclass instances.
    """
    diameters = [4, 4.0, 24, 24.8, 260, 260.4, 1600]
    for obj, diameter in zip(child_classes, diameters):
        assert obj.get_diameter() == diameter


def test_area(child_classes):
    """
    Tests that each subclass correctly calculates and returns its area.

    Args:
        child_classes (list): Fixture providing subclass instances.
    """
    areas = [12.57, 12.57, 452.39, 483.05, 53092.92, 53256.40, 2010619.73]
    for obj, area in zip(child_classes, areas):
        assert obj.get_area() == pytest.approx(area, rel=1e-3)


def test_create_from_diameter():
    """
    Tests the create_from_diameter method for each subclass, ensuring that it correctly
    calculates and sets the radius based on the provided diameter.
    """
    # due to the different number of arguments objects are created manually

    tyre1 = Tyre.create_from_diameter(2, "235/19R19")
    assert tyre1.get_diameter() == 2
    pizza1 = Pizza.create_from_diameter(22.0, [])
    assert pizza1.get_diameter() == 22.0
    rim1 = Rim.create_from_diameter(232)
    assert rim1.get_diameter() == 232
    tyre_wheel = Tyre(800, "235/19R19")
    rim_wheel = Rim(241.3)
    Wheel.create_from_diameter(int(tyre_wheel.get_diameter()), tyre_wheel, rim_wheel)
    assert tyre_wheel.get_diameter() == 1600


def test_change_diameter(child_classes):
    """
    Tests that each subclass instance correctly updates its diameter when changed.

    Args:
        child_classes (list): Fixture providing subclass instances.
    """
    for obj in child_classes:
        obj.change_diameter(8)
        assert obj.get_diameter() == 8


def test_name_mangling():
    """
    Tests the exercise's name-mangling requirement by attempting to access a private
    attribute (__radius) in each subclass.

    Asserts:
        AttributeError is raised when accessing a private attribute directly.
    """
    with pytest.raises(AttributeError):
        pizza_no_ingredients_int = Pizza(2, [])
        print(pizza_no_ingredients_int.__radius)
