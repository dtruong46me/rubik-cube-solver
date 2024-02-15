import sys
sys.path.append('.')

from objects.cube_3x3x3 import RubikCube
from solver.m2op_solver import M2OPSolver

rubik = RubikCube()
m2op_solver = M2OPSolver(rubik)

