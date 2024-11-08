"""
Module for representing and manipulating rim objects as circular shapes.

This module defines a `Pizza` class, which represents a pizza as a subclass of `Circle`.
It allows for the creation of a pizza with specified ingredients and categorizes it
based on its size, calculated from its radius.
"""

from __future__ import annotations
from typing import Union

from circles.circle import Circle


class Pizza(Circle):
    """
    Representation of a pizza as a subclass of Circle.

    Attributes:
        ingredients (list): A list of pizza ingredients.
        size (str): The size of the pizza, categorized as "small", "medium", or "large".
    """

    def __init__(self, radius: Union[int, float], ingredients: list) -> None:
        """
        Initializes a Pizza object and categorizes it into three different sizes

        Parameters:
            radius (Union[int, float]): The radius of the pizza in centimeters.
            ingredients (list): List of ingredients used in the pizza.

        Inherits all argument verification exceptions from Circle.
        Raises:
            TypeError: If the ingredients variable is not a list
        """
        super().__init__(radius)
        if isinstance(ingredients, list):
            self.ingredients = ingredients
            if 0 < self.get_radius() <= 20:
                self.size = "small"
            elif 20 < self.get_radius() <= 40:
                self.size = "medium"
            elif self.get_radius() > 40:
                self.size = "large"
        else:
            print("Ingredients value must be a list")
            raise TypeError

    @classmethod
    def create_from_diameter(
        cls, diameter: Union[int, float], ingredients: list = None
    ) -> Pizza:
        """
        Creates a Pizza instance using a diameter.

        Parameters:
            diameter (Union[int, float]): The diameter of the pizza in centimeters.
            ingredients (list): List of ingredients used in pizza.

        Returns:
            Pizza: An instance of the Pizza class.
        """
        if ingredients is None:
            ingredients = []
        return cls(diameter / 2, ingredients)

    def print_ingredients(self) -> None:
        """
        Prints a list of the pizza's ingredients to the terminal.
        """
        print("The pizza contains the following ingredients:")
        for ingredient in self.ingredients:
            print(ingredient)
