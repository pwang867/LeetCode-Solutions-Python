"""This is docstring of Learn_docstring."""


class ZeroDivideError(Exception):
    def __init__(self, s=""):
        print("Zero division is not allowed" + s)


"""
this is a testing
"""

"""this is a doc string for Class Calculator above"""


class Calculator:
    """this is a doc string for Class Calculator"""

    def divide(self, x, y):
        """this is doc string of Calculator.divide"""
        if y == 0:
            raise ZeroDivideError()
        else:
            raise ValueError()


if __name__ == "__main__":
    c = Calculator()
    print(__doc__)
    print(Calculator.__doc__)
    print(Calculator.divide.__doc__)
