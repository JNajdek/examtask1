"""
Module for representing and manipulating rim objects as circular shapes.

This module defines the `Rim` class, a subclass of `Circle`, which models a rim with methods
for handling and converting its dimensions between millimeters and inches. 'Rim' class can be
used as a standalone object and as a part of the 'Wheel' class
"""

from __future__ import annotations
from typing import Union

from circles.circle import Circle


class Rim(Circle):
    """
    Representation of a rim as a subclass of a Circle.

    Attributes:
        diameter_inches (Union[int, float]): The diameter of the rim measured in inches.

    """

    def __init__(self, radius: Union[int, float]) -> None:
        """
        Initializes a Rim object.

        Parameters:
            radius (Union[int, float]): The radius of the rim in millimeters.

        Inherits all argument verification exceptions from Circle.
        """
        super().__init__(radius)
        self.diameter_inches = self.mm_to_inches(2 * radius)

    @classmethod
    def create_from_diameter(cls, diameter: Union[int, float]) -> Rim:
        """
        Creates a Rim instance using a diameter.

        Parameters:
            diameter (Union[int, float]): The diameter of the rim in millimeters.

        Returns:
            Rim: An instance of the Rim class.

        """
        return cls(diameter / 2)

    @staticmethod
    def mm_to_inches(mm_value: Union[int, float]) -> float:
        """
        Converts millimeters to inches.

        Parameters:
            mm_value (Union[int, float]): The value in millimeters to convert.

        Returns:
            float: The equivalent value in inches.
        """
        Rim.validate_data(mm_value)
        return round(mm_value / 25.4, 2)
