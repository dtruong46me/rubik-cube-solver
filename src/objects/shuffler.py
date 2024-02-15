import os

from random import randint

class RubikShuffler:
    def __init__(self) -> None:
        pass

    from objects.cube_2x2x2 import RubikCube2
    def shuffle(self, rubik: RubikCube2, from_input=False, from_file=False, from_random=False):
        if from_input==True:
            self.shuffle_from_input(rubik)

        if from_file==True:
            self.shuffle_from_file(rubik)
        
        if from_random==True:
            self.shuffle_from_random(rubik)
            # Shuffle rubik code here

    def shuffle_from_input(self, rubik: RubikCube2):

        print('Input to shuffle Rubik Cube (Seperated by space)')
        moves = input('Shuffle Sequence: ').split(' ')

        for move in moves:
            face = move[0]
            # clockwise = True
            
            if len(move) == 1:
                rubik.rotate_face(face=face, clockwise=True)
            
            if len(move) == 2:
                # clockwise = False
                rubik.rotate_face(face=face, clockwise=False)

    def shuffle_from_file(self, rubik: RubikCube2):
        shuffle_file_txt = 'shuffle.txt'
        parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        filepath = os.path.join(parent_path, 'data', shuffle_file_txt)
        
        with open(file=filepath) as f:
            moves = f.readline().split(' ')
            
            for move in moves:
                face = move[0]

                if len(move) == 1:
                    rubik.rotate_face(face=face, clockwise=True)
                
                if len(move) == 2:
                    rubik.rotate_face(face=face, clockwise=False)

    def shuffle_from_random(self, rubik: RubikCube2, random_steps=20):
        faces = {
            0: 'U',
            1: 'D',
            2: 'L', 
            3: 'R',
            4: 'F',
            5: 'B'
        }

        clockwise = {
            0: False,
            1: True
        }

        for _ in range(random_steps):
            # Random face and clockwise
            (f_rand, c_rand) = (randint(0, 5), randint(0, 1))

            face = faces[f_rand]
            cw = clockwise[c_rand]

            rubik.rotate_face(face=face, clockwise=cw)