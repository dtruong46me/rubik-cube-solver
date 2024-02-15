import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from objects.cube_2x2x2 import *
from objects.shuffler import *

if __name__ == '__main__':
    test_rubik = RubikCube2()
    shuffler = RubikShuffler()

    shuffler.shuffle(test_rubik, from_input=True)

    test_rubik.display()