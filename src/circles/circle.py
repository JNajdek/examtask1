"""
Module for defining the abstract base class Circle, which represents a circular shape
with basic geometric methods.

This module contains the `Circle` class, an abstract base class (ABC) providing foundational
properties and methods that can be used or overridden in subclasses to represent circular
objects such as: pizza, wheel, rim, tyre.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import math
from typing import Union


class Circle(ABC):
    """
    An abstract base class representing a circle, defining methods to be used or overridden
    in subclasses.

    Attributes:
        __radius (Union[int, float]): The radius of the circle.

    """

    @abstractmethod
    def __init__(self, radius: Union[int, float]) -> None:
        """
        Initializes a Circle object and verifies if it's radius value is correct

        Parameters:
            radius (Union[int, float]): The radius of the circle.
        """
        self.validate_data(radius)
        self.__radius = radius

    def get_diameter(self) -> Union[int, float]:
        """
        Returns the diameter of the circle.

        Returns:
            Union[int, float]: The diameter of the circle.
        """
        return 2 * self.__radius

    def get_area(self) -> float:
        """
        Returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius**2

    @classmethod
    @abstractmethod
    def create_from_diameter(cls, diameter: Union[int, float]) -> Circle:
        """
        Creates a Tyre instance using a diameter

        Parameters:
            diameter (Union[int, float]): The diameter of the circle
        """
        pass

    def change_diameter(self, new_diameter: Union[int, float]) -> None:
        """
        Changes circle's diameter to a new one

        Parameters:
            new_diameter (Union[int, float]): The new diameter for the circle.
        """
        self.validate_data(new_diameter)
        self.__radius = new_diameter / 2

    @staticmethod
    def validate_data(data):
        """
        Validates the data is an integer/float greater than zero.
        Raises:
            ValueError: If the data is not an integer or a float.
            TypeError: If the data is not greater than zero.
        """
        if not isinstance(data, (float, int)):
            raise TypeError("The data must be a float or an int")

        if data <= 0:
            raise ValueError("The data must be greater than zero")

    def get_radius(self) -> Union[int, float]:
        """
        Returns the radius of the circle.

        Returns:
            Union[int, float]: The radius of the circle.
        """
        return self.__radius
