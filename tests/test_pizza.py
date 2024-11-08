"""
Module for testing the initialization, functionality of methods, and properties
of the 'Pizza' class

Author: Jakub Najdek
Date: 2023-11-06
Version: 1.0
"""

import pytest
from circles.pizza import Pizza


@pytest.fixture
def pizza_int():
    """
    Fixture for creating a Pizza object with specific attributes.
    Returns:
        Pizza: A Pizza object with radius 20 and the ingredients ["cheese", "sauce", "peperoni"].
    """
    return Pizza(20, ["cheese", "sauce", "peperoni"])


def test_is_iterable(pizza_int):
    """
    Tests that the pizza ingredients can be iterated over (list type can be iterated over).

    Parameters:
        pizza_int (Pizza): A pizza object created from the fixture.
    """
    assert isinstance(pizza_int.ingredients, list)


def test_printing_ingredients(pizza_int, capsys):
    """
    Tests the printing of ingredients to the standard output.

    Parameters:
        pizza_int (Pizza): A pizza object created from the fixture.
        capsys (pytest fixture): A pytest fixture for capturing standard output.

    """
    pizza_int.print_ingredients()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "The pizza contains the following ingredients:\ncheese\nsauce\npeperoni\n"
    )


@pytest.mark.parametrize(
    ("input_n", "expected"),
    [
        (5.0, "small"),
        (20, "small"),
        (21, "medium"),
        (40, "medium"),
        (40.1, "large"),
        (600, "large"),
    ],
)
def test_pizza_sizes_and_compartment_boundaries(input_n, expected):
    """
    Tests the determination of pizza size based on its diameter, using parameterization to
     verify different size categories.

    Parameters:
        input_n (float): The diameters of the pizza.
        expected (str): The expected sizes of the pizza ("small", "medium", or "large").

    """
    pizza = Pizza(input_n, [])
    assert pizza.size == expected


def test_incorrect_ingredients():
    """
    Tests the invalid ingredients type exceptions handling
    """
    with pytest.raises(TypeError):
        Pizza(20, "banana")
