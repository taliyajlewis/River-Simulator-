"""File to define Bear class."""

__author__ = "730411307"


class Bear:
    """Class to represent the Bears living by the river."""
    # attributes
    age: int
    hunger_score: int

    def __init__(self, age=0, hunger_score=0) -> None:
        """Bears living by the river."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """One day at the river."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Increase hunger by number of fish."""
        self.hunger_score += num_fish