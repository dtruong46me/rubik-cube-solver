import sys
sys.path.append('.')

from objects.cube_2x2x2 import RubikCube2
from objects.interface import Interface

test_rubik = RubikCube2()

interface = Interface(rubik=test_rubik)

interface.shuffle(from_input=True, from_file=False)