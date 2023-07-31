import sys
sys.path.append('..')

from objects.rubik_cube import RubikCube

test_rubik = RubikCube()
test_rubik.rotate_U('clockwise')
test_rubik.rotate_L('clockwise')
test_rubik.display()