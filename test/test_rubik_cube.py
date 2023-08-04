import sys
sys.path.append('.')

from objects.rubik_cube import RubikCube

test_rubik = RubikCube()
list_seq = test_rubik.input_user()

test_rubik.suffle_from_input(list_seq)
# test_rubik.suffle(10)

test_rubik.display()