"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730563759"


class Simpy:
    """This is defining the class Simpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize arguments of a list[float]."""
        self.values = values

    def __repr__(self) -> str:
        """Return a string with its Class name and value."""
        return f"Simpy({self.values})"

    def fill(self, constant: float, occurence: int) -> None:
        """Mutate the object to give a list of constants with the occurance."""
        i: int = 0
        self.values = []
        while i < occurence:
            self.values.append(constant)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arange values with a start and increment it by step until stop."""
        assert step != 0.0
        i: int = 0
        self.values.append(start)
        if step > 0:
            while self.values[i] < (stop - step):
                self.values.append(self.values[i] + step)
                i += 1
        if step < 0:
            while self.values[i] > (stop - step):
                self.values.append(self.values[i] + step)
                i += 1

    def sum(self) -> float:
        """The sum items in self.values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding self and the right hand side."""
        if type(rhs) == float:
            result: list[float] = []
            for x in range(len(self.values)):
                value = self.values[x] + rhs
                result.append(value)
            return Simpy(result)
        
        else:
            result: list[float] = []
            for x in range(len(self.values)):
                value = self.values[x] + rhs.values[x]
                result.append(value)
            return Simpy(result)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Self to the power of the right hand side."""
        if type(rhs) == float:
            result: list[float] = []
            for x in range(len(self.values)):
                value = self.values[x] ** float(rhs)
                result.append(value)
            return Simpy(result)
        else:
            result: list[float] = []
            for x in range(len(self.values)):
                value = self.values[x] ** rhs.values[x]
                result.append(value)
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compare self to the right hand side to check for equality."""
        if type(rhs) == float:
            result: list[bool] = []
            for x in range(len(self.values)):
                result.append(self.values[x] == rhs)
            return result
        else:
            result: list[bool] = []
            for x in range(len(self.values)):
                result.append(self.values[x] == rhs.values[x])
            return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check to see if self is greater than the right hand side."""
        if type(rhs) == float:
            result: list[bool] = []
            for x in range(len(self.values)):
                result.append(self.values[x] > float(rhs))
            return result
        else:
            result: list[bool] = []
            for x in range(len(self.values)):
                result.append(self.values[x] > rhs.values[x])
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Grab the self from the index or if true."""
        if type(rhs) == int:
            result: float
            result = self.values[rhs]
            return result
        else:
            result: list[bool] = []
            for x in range(len(self.values)):
                if rhs[x]:
                    result.append(self.values[x])
            return Simpy(result)
    