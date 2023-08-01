from ..objects.rubik_cube import RubikCube

class LayerSolver:
    def __init__(self, rubik: RubikCube) -> None:
        self.rubik = rubik
    
    def sovle(self) -> list:
        solution = []
        solution += self.solve_U_layer
        solution += self.solve_M_layer
        solution += self.solve_D_layer
        
        return solution

    def solve_U_layer(self) -> list:
        solution_U = []

        '''
        solution here
        '''

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