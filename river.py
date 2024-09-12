"""File to define River class."""

__author__ = "730411307"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Class for the river."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish(2))
        for x in range(0, num_bears):
            self.bears.append(Bear(5, 0))

    def check_ages(self):
        """Managing age of animals."""
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        self.fish = new_fish

        new_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        
        self.bears = new_bears

        return None

    def bears_eating(self):
        """Bears eat fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None
    
    def check_hunger(self):
        """Checking the hunger of the bears."""
        satisfed_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                satisfed_bears.append(bear)

        self.bears = satisfed_bears
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Remove fish from river."""
        if amount > len(self.fish):
            self.fish = []
        else:
            self.fish = self.fish[amount:]

        return None
    
    def repopulate_fish(self):
        """Repopulating fish in the river."""
        for x in range(0, len(self.fish) // 2):
            for y in range(4):
                self.fish.append(Fish(2)) 
        return None
    
    def repopulate_bears(self):
        """Repopulating bears at the river."""
        for x in range(0, len(self.bears) // 2):
            self.bears.append(Bear(5, 0))

        return None
    
    def view_river(self):
        """Print the current status of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """One week in the river."""
        days_in_week = 7
        for day in range(days_in_week): 
            self.one_river_day()