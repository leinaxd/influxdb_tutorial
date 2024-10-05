# 04/10/2024
#Brainstorming:
#[Machine]
# - Operation step          (What is the current manufacturing step?)
# - Available manufacturing (which mechanizations are available for that machine)
# - tolerance
# - weight
# - consumption
# [Roadmap/material flow]
# - represent how the material is moving through the factory (sequence of machines)


from dataclasses import dataclass
from typing import Literal

@dataclass
class Machine:
    """Represents a machine"""
    id: str
    manufacturer: Literal['serial', 'focas']

@dataclass
class Operation:
    """Represents an operation step, like moving, transforming material"""
    id:int
    type:str

@dataclass
class Piece:
    """Represents a piece part of a manufacturing process"""
    id: str
    material_id: int
    

