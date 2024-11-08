"""
Module for representing and manipulating tyre objects as circular shapes.

This module defines a `Tyre` class, representing a tyre as a subclass of `Circle`.
The `Tyre` class includes methods and properties, such as size
specifications and necessary rim dimensions based on a standard tyre label format.
In addition, it verifies the validity of tyre label data

"""

from __future__ import annotations
from typing import Union

from circles.circle import Circle


class Tyre(Circle):
    """
    Representation of a rim as a subclass of a Circle, based on a standard tyre label format.

    Attributes:
        tyre_size (int): The width of the tyre in millimeters
        necessary_rim_size (int): The required rim diameter in inches

    """

    def __init__(self, radius: Union[int, float], tyre_label: str) -> None:
        """
        Initializes a Tyre object.

        Parameters:
            radius (Union[int, float]): The radius of the tyre in millimeters.
            tyre_label (str): A string following the standard tyre size designation format.
            The tyre label must follow
                the format "XXX/YYRZZ" where:
                    - "XXX": The tyre width in millimeters,
                    - "YY": height-to-width ratio
                    - "ZZ": The rim diameter in inches.

        Raises:
            ValueError: If tyre_label is not a string, or if it doesn't follow the standard
             format explained above.
        """
        super().__init__(radius)
        if isinstance(tyre_label, str):
            if (
                tyre_label[:3].isnumeric()
                and tyre_label[4:6].isnumeric()
                and tyre_label[7:].isnumeric()
            ):
                if (
                    len(tyre_label) == 9
                    and "/" == tyre_label[3]
                    and "R" == tyre_label[6]
                ):
                    self.tyre_size = int(tyre_label[:3])
                    self.necessary_rim_size = int(tyre_label[7:])
                else:
                    print(
                        "Label data must be compatible with standard tire size designation"
                    )
                    raise ValueError
            else:
                print(
                    "Label data must be compatible with standard tire size designation"
                )
                raise ValueError
        else:
            print("Tyre label must be a string")
            raise ValueError

    def get_necessary_ring_diameter(self) -> Union[int]:
        """
        Returns the necessary rim diameter for the tyre.

        Returns:
            int: The rim diameter in inches required for the tyre.
        """
        return self.necessary_rim_size

    @classmethod
    def create_from_diameter(cls, diameter: Union[int, float], tyre_label: str) -> Tyre:
        """
        Creates a Tyre instance using a diameter and a tyre label

        Parameters:
            diameter (Union[int, float]): The diameter of the tyre in millimeters.
            tyre_label (str): A string following the standard tyre size designation format.

        Returns:
            Tyre: An instance of the Tyre class.
        """
        return cls(diameter / 2, tyre_label)
