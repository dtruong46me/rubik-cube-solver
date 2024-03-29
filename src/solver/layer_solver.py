import sys
sys.path.append('.')
from objects.cube_3x3x3 import RubikCube

class LayerSolver:
    def __init__(self, rubik: RubikCube) -> None:
        self.rubik = rubik.rubik
    
    def sovle(self) -> list:
        solution = []
        solution += self.solve_U_layer
        solution += self.solve_M_layer
        solution += self.solve_D_layer
        
        return solution

    def solve_U_layer(self) -> list:
        solution_U = []

        # For each solution, we have to 
        # Step 1: Solve the 'U' cross
        # Step 2: Solve 4 vertexes
        # Step 3: 

        return solution_U
    
    def solve_M_layer(self) -> list:
        solution_M = []

        '''
        solution here
        '''

        return solution_M
    
    def solve_D_layer(self) -> list:
        solution_D = []

        '''
        solution here
        '''

        return solution_D