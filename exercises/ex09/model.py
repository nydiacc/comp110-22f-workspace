"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from math import cos, pi, sin, sqrt
from random import random
from exercises.ex09 import constants

__author__ = "730563759"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Gives the distance between two points."""
        point_distance: float = 0.0
        point_distance = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return point_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
    
    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Updates location."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()

    def contract_disease(self) -> None:
        """Assigns INFECTED to the sickness attribute."""
        self.sickness = constants.INFECTED
        
    def is_vulnerable(self) -> bool:
        """Checks to see if sickness attribute is VULNERABLE."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Checks to see if sickness attribute is INFECTED."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Classifies the the vulnerable cells as gray and infected cells as crimson."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "crimson"
        if self.is_immune():
            return "medium sea green"

    def contact_with(self, other: Cell) -> None:
        """When two cells make contact."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        elif self.is_infected() and other.is_vulnerable():
            other.contract_disease()    

    def immunize(self) -> None:
        """Assigns constant IMMUNE to sickness attribute."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Checks to see if sickness attribute is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initial_infected: int = 0, initial_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        
        if initial_infected <= 0 or initial_infected >= cells:
            raise ValueError("Some number of the Cell objects must begin infected.")
        if initial_immune >= cells or initial_immune < 0:
            raise ValueError("Improper immune cell total.")

        for i in range(0, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        
        idx: int = 0

        while idx < initial_infected:
            self.population[idx].contract_disease()
            idx += 1

        while idx < initial_immune + initial_infected:
            self.population[idx].immunize()
            idx += 1
        
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)    
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0 

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for g in self.population:
            f: int = 0
            for h in self.population:
                if h.is_infected() is False:
                    f += 1
            if f == len(self.population):
                return True

    def check_contacts(self) -> None:
        """Tests whether any two cell values come in contact with one another."""
        i: int = 0
        for x in range(len(self.population)):
            cell_one: Cell = self.population[x]
            while i < len(self.population):
                cell_two: Cell = self.population[i]
                if cell_one.location.distance(cell_two.location) < constants.CELL_RADIUS:
                    cell_one.contact_with(cell_two)
                i += 1