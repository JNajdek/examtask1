# Exam Task 1: Circles Package
ExamTask1 is a project containing the Python package circles and unit tests to verify its quality. The package creates circle-like objects that inherit from the main abstract class, Circle.

# Structure
The 'circles' package is located in the .examtask1/src/circles directory and contains the following circle-like objects:

- circle.py: Contains the abstract Circle class.
- pizza.py: Contains the Pizza subclass.
- rim.py: Contains the Rim subclass.
- tyre.py: Contains the Tyre subclass.
- wheel.py: Contains the Wheel subclass.
- 
The unit tests are located in the ./examtask1/tests folder, where each class has a corresponding test suite.

The Pytest coverage report is located at ./examtask1/htmlcov/class_index.html.

# Installation and Configuration
To install the required dependencies, navigate to the project directory in the terminal and run:
'pip install -r requirements.txt'
# Running Tests
For complete test coverage, execute the following command in the terminal at the project level:
'pytest tests'