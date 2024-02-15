import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from objects.cube_2x2x2 import RubikCube2

class RubikSolver2():
    def __init__(self):
        self.solution = []

    def is_solved(shuffled_rubik: RubikCube2) -> bool:
        

    def solve(shuffled_rubik: RubikCube2) -> list:
        return
    
    