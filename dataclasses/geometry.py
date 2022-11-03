"""Dataclasses"""

from dataclasses import dataclass, field
from math import pi


class Circle:
    def __init__(self, x: float = 0, y: float = 0, radius=1) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def circumference(self):
        return 2 * self.radius * pi


@dataclass
class CircleDataclass:
    x: float = 0
    y: float = 0
    radius: float = 1
    # Internal class field that do not need to be initialized
    _equation = field(init=False, repr=False)
    
    @property
    def circumference(self) -> float:
        return 2 * self.radius * pi
    

def main():
    # circle = Circle(radius=2)
    circle = CircleDataclass(radius=5)
    print(circle)
    print(f"Circumference: {circle.circumference}")


if __name__ == "__main__":
    main()
