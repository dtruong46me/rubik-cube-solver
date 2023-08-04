import sys
sys.path.append('.')

from objects.rubik_cube import RubikCube

class CFOPSolver:
    def __init__(self, rubik: RubikCube = None) -> None:
        self.rubik = rubik.rubik
    
    def solve(self) -> list:
        solution = []

        solution += self.solve_cross()
        solution += self.solve_f2l()
        solution += self.solve_oll()
        solution += self.solve_pll()
    
    def solve_cross(self) -> list:
        solution_cross = []

        return solution_cross
    
    def solve_f2l(self) -> list:
        solution_f2l = []

        return solution_f2l
    
    def solve_oll(self) -> list:
        solution_oll = []

        return solution_oll

    def solve_pll(self) -> list:
        solution_pll = []

        return solution_pll