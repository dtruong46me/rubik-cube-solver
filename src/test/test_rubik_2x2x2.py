import sys
sys.path.append('.')

from objects.cube_2x2x2 import RubikCube2
from objects.shuffler import RubikShuffler

test_rubik = RubikCube2()

shuffler = RubikShuffler()

shuffler.shuffle(test_rubik)