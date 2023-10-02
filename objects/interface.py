from cube_2x2x2 import RubikCube2
from random import randint

class Interface:
    def __init__(self, rubik: RubikCube2) -> None:
        self.rubik = rubik
    
    def shuffle(self, from_input=False, from_file=False, from_random=False):
        if from_input==True:
            self.shuffle_from_input()

        if from_file==True:
            self.shuffle_from_file()
        
        if from_random==True:
            self.shuffle_from_random()
            # Shuffle rubik code here

    def shuffle_from_input(self):

        print('Input to shuffle Rubik Cube (Seperated by space)')
        moves = input('Shuffle Sequence: ').split(' ')

        for move in moves:
            face = move[0]
            # clockwise = True
            
            if len(move) == 1:
                self.rubik.rotate_face(face=face, clockwise=True)
            
            if len(move) == 2:
                # clockwise = False
                self.rubik.rotate_face(face=face, clockwise=False)

    def shuffle_from_file(self):
        filepath = '../data/shuffle.txt'
        
        with open(file=filepath) as f:
            moves = f.readline().split(' ')
            
            for move in moves:
                face = move[0]

                if len(move) == 1:
                    self.rubik.rotate_face(face=face, clockwise=True)
                
                if len(move) == 2:
                    self.rubik.rotate_face(face=face, clockwise=False)

    def shuffle_from_random(self, customize=False):
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

        # The default random steps is 20
        random_steps=20

        # When user change random steps
        if customize==True:
            random_steps = int(input('Enter your random steps: '))
        
        for _ in range(random_steps):
            # Random face and clockwise
            (f_rand, c_rand) = (randint(0, 5), randint(0, 1))

            face = faces[f_rand]
            cw = clockwise[c_rand]

            self.rubik.rotate_face(face=face, clockwise=cw)

    
    def solve(self) -> None:

        if self.rubik.is_solved() == False:
            
            ### START CODE HERE ###



            ### END CODE HERE ###
            pass

        if self.rubik.is_solved() == True:
            print("Solved")

        return
    
    