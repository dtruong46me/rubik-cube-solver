from cube_2x2x2 import RubikCube2

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

    def shuffle_from_random(self):

        pass