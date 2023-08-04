import sys
sys.path.append('.')

from objects.rubik_cube import RubikCube

class M2OPSolver:
    def __init__(self, rubik: RubikCube = None) -> None:
        self.rubik = rubik.rubik

        self.edges = {
            'A': []
        }

        # R U' R' U' R U R' F' R U R' U' R' F R
        self.formula_vertex = [('R', 'clockwise'), ('U', 'counterclockwise'), ('R', 'counterclockwise'), ('U', 'counterclockwise'), ('R', 'clockwise'), ('U', 'clockwise'), ('R', 'counterclockwise'), ('F', 'counterclockwise'), ('R', 'clockwise'), ('U', 'clockwise'), ('R', 'counterclockwise'), ('U', 'counterclockwise'), ('R', 'counterclockwise'), ('F', 'clockwise'), ('R', 'clockwise')]

        self.vertexes = {
            'B': [('U', 'clockwise'), ('F', 'clockwise')],
            'C': [('F', 'clockwise')],
            'D': [('U', 'counterclockwise'), ('F', 'clockwise')],
            'F': [('F', 'clockwise'), ('F', 'clockwise')],
            'G': [('L', 'counterclockwise'), ('F', 'clockwise'), ('F', 'clockwise')],
            'H': [('L', 'counterclockwise'), ('L', 'counterclockwise'), ('F', 'clockwise'), ('F', 'clockwise')],
            'I': [('F', 'counterclockwise'), ('D', 'clockwise')],
            'J': [('F', 'clockwise'), ('F', 'clockwise'), ('D', 'clockwise')],
            'K': [('F', 'clockwise'), ('D', 'clockwise')],
            'L': [('D', 'clockwise')],
            'M': [('R', 'counterclockwise')],
            'N': [('R', 'clockwise'), ('R', 'clockwise')],
            'O': [('R', 'clockwise')],
            'P': [],
            'Q': [('B', 'counterclockwise'), ('D', 'counterclockwise')],
            'R': [('B', 'clockwise'), ('B', 'clockwise'), ('D', 'counterclockwise')],
            'S': [('B', 'clockwise'), ('D', 'counterclockwise')],
            'T': [('D', 'counterclockwise')],
            'U': [('F', 'counterclockwise')],
            'V': [('D', 'counterclockwise'), ('F', 'counterclockwise')],
            'W': [('D', 'clockwise'), ('D', 'clockwise'), ('F', 'counterclockwise')],
            'X': [('D', 'clokcwise'), ('F', 'counterclockwise')]
        }

    def solve(self) -> list:
        solution = []

        solution += self.solve_edge()
        solution += self.solve_vertex()

        return solution
    
    def solve_edge(self) -> list:
        solution_edge = []

        return solution_edge

    def solve_vertex(self) -> list:
        solution_vertex = []

        return solution_vertex