from dataclasses import dataclass, field, fields

@dataclass
class Particle:
    x: float = 0
    y: float = 0
    fitness: float = 0 
    velocity: float = 0
    best_x: float = x


p1 = Particle()
print(p1.best_x)