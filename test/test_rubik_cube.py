import sys
sys.path.append('.')

from objects.rubik_cube import RubikCube

test_rubik = RubikCube()

test_rubik.suffle(10)

test_rubik.display()