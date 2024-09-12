"""File to define Fish class."""

__author__ = "730411307"


class Fish:
    """Class to represetn the fish living in the river."""
    # attributes
    age: int
    
    def __init__(self, age=0) -> None:
        """The age of fish in river."""
        self.age = age
        return None
    
    def one_day(self):
        """One day of fish being in river."""
        self.age += 1
        return None