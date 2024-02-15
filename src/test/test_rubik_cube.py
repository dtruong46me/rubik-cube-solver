import sys
sys.path.append('.')

from objects.cube_3x3x3 import RubikCube

test_rubik = RubikCube()

test_rubik.suffle(10)

test_rubik.display()