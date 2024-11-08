"""
Module for representing and manipulating wheel objects as circular shapes.

This module defines a `Wheel` class, representing a wheel as a subclass of `Circle`.
A `Wheel` is composed of two primary components: a `Tyre` and a `Rim`. This class
ensures compatibility in sizes between these components and provides methods to replace
individual components while maintaining compatibility.
"""

from __future__ import annotations
from typing import Union


from circles.circle import Circle
from circles.rim import Rim
from circles.tyre import Tyre


class Wheel(Circle):
    """
    Representation of a wheel as a subclass of a Circle.
    The wheel is composed of a tyre, and a rim objects.

    Attributes:
        tyre (Tyre): The tyre component.
        rim (Rim): The rim component.

    """

    def __init__(self, tyre: Tyre, rim: Rim) -> None:
        """
        Initializes a Wheel object and ensures the compatibility between the tyre
        diameter and the wheel's diameter.

        Parameters:
            tyre (Tyre): The tyre component.
            rim (Rim): The rim component.

        Raises:
            ValueError: If tyre and rim sizes do not match
            TypeError: If invalid type of data is provided.
        """
        super().__init__(tyre.get_radius())
        if isinstance(tyre, Tyre) and isinstance(rim, Rim):
            self.tyre = tyre
            self.rim = rim
            if not self.verify_rim_size():
                print("Rim and Tyre size doesn't match")
                raise ValueError

        else:
            print("Incorrect wheel arguments data")
            raise TypeError

    def change_tyre(self, new_tyre: Tyre) -> None:
        """
        Replaces the tyre with the new one.

        Parameters:
            new_tyre (Tyre): The new tyre to replace the existing one.

        Raises:
            ValueError: If the new tyre's rim requirements don't match with the current rim.
            TypeError: If the provided new_tyre argument is not an instance
             of the 'Tyre' class
        """
        if isinstance(new_tyre, Tyre):
            if new_tyre.necessary_rim_size == int(round(self.rim.diameter_inches, 0)):
                self.tyre = new_tyre
            else:
                print("The new tyre doesn't match the rim")
                raise ValueError
        else:
            print("Provided object must be a tyre")
            raise TypeError

    def change_rim(self, new_rim: Rim) -> None:
        """
        Replaces the rim with the new one.

        Parameters:
            new_rim (Rim): The new rim to replace the existing one.

        Raises:
            ValueError: If the new rim doesn't match with the current tyre's rim requirement.
            TypeError: If the provided new_rim argument is not an instance
             of the 'Rim' class
        """
        if isinstance(new_rim, Rim):
            if new_rim.diameter_inches == self.tyre.necessary_rim_size:
                self.rim = new_rim
            else:
                print("The new rim doesn't match the tire")
                raise ValueError
        else:
            print("Provided object must be a rim")
            raise TypeError

    def verify_rim_size(self) -> bool:
        """
        Checks if the tyre fits properly on the rim.

        Returns:
            bool: True if the rim and tyre sizes match otherwise, False.
        """
        return self.tyre.necessary_rim_size == int(round(self.rim.diameter_inches, 0))

    @classmethod
    def create_from_diameter(
        cls, diameter: Union[int, float], tyre: Tyre, rim: Rim
    ) -> Wheel:
        """
        Creates a Wheel instance using diameter, Tyre and Rim objects.

        Parameters:
            diameter (Union[int, float]): The diameter of the wheel.
            tyre (Tyre): The tyre component.
            rim (Rim): The rim component.

        Returns:
            Wheel: A new Wheel instance.
        """
        return cls(tyre, rim)
