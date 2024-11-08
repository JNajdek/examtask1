"""
Module for testing the initialization, functionality of methods, and properties
of the 'Rim' class

Author: Jakub Najdek
Date: 2023-11-06
Version: 1.0
"""

import pytest
from circles.rim import Rim


def test_initiation():
    """
    Tests if rim initialises correctly with standard radius parameter
    """
    rim = Rim(12)
    assert rim.get_radius() == 12


def test_mm_to_inches():
    """
    Tests the conversion of millimeters to inches with correct argument
    """
    mm = 2345
    inches = Rim.mm_to_inches(mm)
    assert inches == 92.32


def test_mm_to_inches_incorrect_args():
    """
    Tests conversion of millimeters to inches with invalid  mm_value argument
    and exception handling.
    """
    mm = "2345"
    with pytest.raises(TypeError):
        Rim.mm_to_inches(mm)
