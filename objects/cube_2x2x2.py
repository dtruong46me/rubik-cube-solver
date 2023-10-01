
from random import randint

class RubikCube2:
    def __init__(self) -> None:
        self.faces = {
            "U": [["W" for i in range(2)] for j in range(2)],
            "D": [["Y" for i in range(2)] for j in range(2)],
            "L": [["G" for i in range(2)] for j in range(2)],
            "R": [["B" for i in range(2)] for j in range(2)],
            "F": [["R" for i in range(2)] for j in range(2)],
            "B": [["O" for i in range(2)] for j in range(2)]
        }

    """
         _____           __          _______   
        /  _  \____ __ _/ /_____ __ /  ____/_____ __ ___ _ __  ___ _____ ____ 
       /  / / // __` /_  __// __` /_\____  / ___// /  _ \ /  |/  // ___/  __ \ 
      /  /_/ // /_/ / / /_ / /_/ /_ ___  \/ /__ / //  __//      // /__ /  ___/
     /______/ \___ /  \__/ \___ /________/\___//_/ \___//__/ |_/ \___/ \____/

    """

    # BEGIN: Display the Rubik Cube #
    def colored_text(self, text, color):
        colors = {
            'W': '\033[97m',   # White
            'Y': '\033[93m',   # Yellow
            'G': '\033[92m',   # Green
            'B': '\033[94m',   # Blue
            'R': '\033[31m',   # Red
            'O': '\033[91m'    # Orange
        }
        return colors[color] + text + '\033[0m'  # Reset to default color

    def display(self) -> None:
        ''' print each face of the rubik, the template like this:
        +--- U ----+---- D ----+---- L ----+---- R ----+---- F ----+---- B ----+
            W W         Y Y         O O         R R         G G         B B
            W W         Y Y         G G         B B         R R         O O
        +----------+-----------+-----------+-----------+-----------+-----------+
        '''

        print('\033[35m+--- U ----+---- D ----+---- L ----+---- R ----+---- F ----+---- B ----+\033[35m')
    
        for i in range(2):
            u_row = ' '.join(self.colored_text(cell, self.faces['U'][i][j]) for j, cell in enumerate(self.faces['U'][i]))
            d_row = ' '.join(self.colored_text(cell, self.faces['D'][i][j]) for j, cell in enumerate(self.faces['D'][i]))
            l_row = ' '.join(self.colored_text(cell, self.faces['L'][i][j]) for j, cell in enumerate(self.faces['L'][i]))
            r_row = ' '.join(self.colored_text(cell, self.faces['R'][i][j]) for j, cell in enumerate(self.faces['R'][i]))
            f_row = ' '.join(self.colored_text(cell, self.faces['F'][i][j]) for j, cell in enumerate(self.faces['F'][i]))
            b_row = ' '.join(self.colored_text(cell, self.faces['B'][i][j]) for j, cell in enumerate(self.faces['B'][i]))
            print('    ' + u_row + '         ' + d_row + '         ' + l_row + '         ' + r_row + '         ' +
                  f_row + '         ' + b_row)

        print('\033[35m+----------+-----------+-----------+-----------+-----------+-----------+\033[97m\n')
    # END: Display the Rubik Cube #

    # BEGIN: Rotate Rubik Faces #
    def rotate_face(self, face: str, clockwise=True):
        
        if face == 'U':
            self.move_U(clockwise)

        if face == 'D':
            self.move_D(clockwise)

        if face == 'L':
            self.move_L(clockwise)
        
        if face == 'R':
            self.move_R(clockwise)
        
        if face == 'F':
            self.move_F(clockwise)
        
        if face == 'B':
            self.move_B(clockwise)
        
        else:
            print("Invalid Rubik\'s face")

    # DETAILS: Rotate U D L R F B
    def move_U(self, clockwise=True):
        if clockwise==True:
            self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][1][0], self.faces['U'][1][1] = \
            self.faces['U'][1][0], self.faces['U'][0][0], self.faces['U'][1][1], self.faces['U'][0][1]

            self.faces['F'][0][0], self.faces['F'][0][1], self.faces['L'][0][0], self.faces['L'][0][1], \
            self.faces['B'][0][0], self.faces['B'][0][1], self.faces['R'][0][0], self.faces['R'][0][1] = \
            self.faces['R'][0][0], self.faces['R'][0][1], self.faces['F'][0][0], self.faces['F'][0][1], \
            self.faces['L'][0][0], self.faces['L'][0][1], self.faces['B'][0][0], self.faces['B'][0][1]

        if clockwise==False:
            self.faces['U'][0][0], self.faces['U'][0][1], self.faces['U'][1][0], self.faces['U'][1][1] = \
            self.faces['U'][1][0], self.faces['U'][0][0], self.faces['U'][1][1], self.faces['U'][0][1]

            self.faces['F'][0][0], self.faces['F'][0][1], self.faces['L'][0][0], self.faces['L'][0][1], \
            self.faces['B'][0][0], self.faces['B'][0][1], self.faces['R'][0][0], self.faces['R'][0][1] = \
            self.faces['L'][0][0], self.faces['L'][0][1], self.faces['B'][0][0], self.faces['B'][0][1], \
            self.faces['R'][0][0], self.faces['R'][0][1], self.faces['F'][0][0], self.faces['F'][0][1]
    
    def move_D(self, clockwise=True):
        if clockwise==True:
            self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][1][0], self.faces['D'][1][1] = \
            self.faces['D'][1][0], self.faces['D'][0][0], self.faces['D'][1][1], self.faces['D'][0][1]

            self.faces['F'][1][0], self.faces['F'][1][1], self.faces['L'][1][0], self.faces['L'][1][1], \
            self.faces['B'][1][0], self.faces['B'][1][1], self.faces['R'][1][0], self.faces['R'][1][1] = \
            self.faces['L'][1][0], self.faces['L'][1][1], self.faces['B'][1][0], self.faces['B'][1][1], \
            self.faces['R'][1][0], self.faces['R'][1][1], self.faces['F'][1][0], self.faces['F'][1][1]

        if clockwise==False:
            self.faces['D'][0][0], self.faces['D'][0][1], self.faces['D'][1][0], self.faces['D'][1][1] = \
            self.faces['D'][1][0], self.faces['D'][0][0], self.faces['D'][1][1], self.faces['D'][0][1]

            self.faces['F'][1][0], self.faces['F'][1][1], self.faces['L'][1][0], self.faces['L'][1][1], \
            self.faces['B'][1][0], self.faces['B'][1][1], self.faces['R'][1][0], self.faces['R'][1][1] = \
            self.faces['R'][1][0], self.faces['R'][1][1], self.faces['F'][1][0], self.faces['F'][1][1], \
            self.faces['L'][1][0], self.faces['L'][1][1], self.faces['B'][1][0], self.faces['B'][1][1]

    def move_L(self, clockwise=True):
        if clockwise==True:
            self.faces['L'][0][0], self.faces['L'][0][1], self.faces['L'][1][0], self.faces['L'][1][1] = \
            self.faces['L'][1][0], self.faces['L'][0][0], self.faces['L'][1][1], self.faces['L'][0][1]

            self.faces['F'][0][0], self.faces['F'][1][0], self.faces['D'][0][0], self.faces['D'][1][0], \
            self.faces['B'][1][1], self.faces['B'][0][1], self.faces['U'][0][0], self.faces['U'][1][0] = \
            self.faces['U'][0][0], self.faces['U'][1][0], self.faces['F'][0][0], self.faces['F'][1][0], \
            self.faces['D'][0][0], self.faces['D'][0][1], self.faces['B'][1][1], self.faces['B'][0][1]

        if clockwise==False:
            self.faces['L'][0][0], self.faces['L'][0][1], self.faces['L'][1][0], self.faces['L'][1][1] = \
            self.faces['L'][1][0], self.faces['L'][0][0], self.faces['L'][1][1], self.faces['L'][0][1]

            self.faces['F'][0][0], self.faces['F'][1][0], self.faces['D'][0][0], self.faces['D'][1][0], \
            self.faces['B'][1][1], self.faces['B'][0][1], self.faces['U'][0][0], self.faces['U'][1][0] = \
            self.faces['D'][0][0], self.faces['D'][1][0], self.faces['B'][1][1], self.faces['B'][0][1], \
            self.faces['U'][0][0], self.faces['U'][1][0], self.faces['F'][0][0], self.faces['F'][1][0]
    
    def move_R(self, clockwise=True):
        if clockwise==True:
            self.faces['R'][0][0], self.faces['R'][0][1], self.faces['R'][1][0], self.faces['R'][1][1] = \
            self.faces['R'][1][0], self.faces['R'][0][0], self.faces['R'][1][1], self.faces['R'][0][1]

            self.faces['F'][0][1], self.faces['F'][1][1], self.faces['D'][0][1], self.faces['D'][1][1], \
            self.faces['B'][1][0], self.faces['B'][0][0], self.faces['U'][0][1], self.faces['U'][1][1] = \
            self.faces['D'][0][1], self.faces['D'][1][1], self.faces['B'][1][0], self.faces['B'][0][0], \
            self.faces['U'][0][1], self.faces['U'][1][1], self.faces['F'][0][1], self.faces['F'][1][1]

        if clockwise==False:
            self.faces['R'][0][0], self.faces['R'][0][1], self.faces['R'][1][0], self.faces['R'][1][1] = \
            self.faces['R'][1][0], self.faces['R'][0][0], self.faces['R'][1][1], self.faces['R'][0][1]

            self.faces['F'][0][1], self.faces['F'][1][1], self.faces['D'][0][1], self.faces['D'][1][1], \
            self.faces['B'][1][0], self.faces['B'][0][0], self.faces['U'][0][1], self.faces['U'][1][1] = \
            self.faces['U'][0][1], self.faces['U'][1][1], self.faces['F'][0][1], self.faces['F'][1][1], \
            self.faces['D'][0][1], self.faces['D'][1][1], self.faces['B'][1][0], self.faces['B'][0][0]

    def move_F(self, clockwise=True):
        if clockwise==True:
            self.faces['F'][0][0], self.faces['F'][0][1], self.faces['F'][1][0], self.faces['F'][1][1] = \
            self.faces['F'][1][0], self.faces['F'][0][0], self.faces['F'][1][1], self.faces['F'][0][1]

            self.faces['U'][1][0], self.faces['U'][1][1], self.faces['R'][0][0], self.faces['R'][1][0], \
            self.faces['D'][0][1], self.faces['D'][0][0], self.faces['L'][1][1], self.faces['L'][0][1] = \
            self.faces['L'][1][1], self.faces['L'][0][1], self.faces['U'][1][0], self.faces['U'][1][1], \
            self.faces['R'][0][0], self.faces['R'][1][0], self.faces['D'][0][1], self.faces['D'][0][0]

        if clockwise==False:
            self.faces['F'][0][0], self.faces['F'][0][1], self.faces['F'][1][0], self.faces['F'][1][1] = \
            self.faces['F'][1][0], self.faces['F'][0][0], self.faces['F'][1][1], self.faces['F'][0][1]

            self.faces['U'][1][0], self.faces['U'][1][1], self.faces['R'][0][0], self.faces['R'][1][0], \
            self.faces['D'][0][1], self.faces['D'][0][0], self.faces['L'][1][1], self.faces['L'][0][1] = \
            self.faces['R'][0][0], self.faces['R'][1][0], self.faces['D'][0][1], self.faces['D'][0][0], \
            self.faces['L'][1][1], self.faces['L'][0][1], self.faces['U'][1][0], self.faces['U'][1][1]

    
    def move_B(self, clockwise=True):
        if clockwise==True:
            self.faces['B'][0][0], self.faces['B'][0][1], self.faces['B'][1][0], self.faces['B'][1][1] = \
            self.faces['B'][1][0], self.faces['B'][0][0], self.faces['B'][1][1], self.faces['B'][0][1]

            self.faces['U'][0][0], self.faces['U'][0][1], self.faces['R'][0][1], self.faces['R'][1][1], \
            self.faces['D'][1][1], self.faces['D'][1][0], self.faces['L'][1][0], self.faces['L'][0][0] = \
            self.faces['R'][0][1], self.faces['R'][1][1], self.faces['D'][1][1], self.faces['D'][1][0], \
            self.faces['L'][1][0], self.faces['L'][0][0], self.faces['U'][0][0], self.faces['U'][0][1]

        if clockwise==False:
            self.faces['B'][0][0], self.faces['B'][0][1], self.faces['B'][1][0], self.faces['B'][1][1] = \
            self.faces['B'][1][0], self.faces['B'][0][0], self.faces['B'][1][1], self.faces['B'][0][1]

            self.faces['U'][0][0], self.faces['U'][0][1], self.faces['R'][0][1], self.faces['R'][1][1], \
            self.faces['D'][1][1], self.faces['D'][1][0], self.faces['L'][1][0], self.faces['L'][0][0] = \
            self.faces['L'][1][0], self.faces['L'][0][0], self.faces['U'][0][0], self.faces['U'][0][1], \
            self.faces['R'][0][1], self.faces['R'][1][1], self.faces['D'][1][1], self.faces['D'][1][0]

    # END: Display the Rubik Cube #


    # BEGIN: Check if Rubik is solved
    def is_solved(self) -> bool:

        solved_rubik = {
            'U': [['W' for i in range(2)] for j in range(2)],
            'D': [['Y' for i in range(2)] for j in range(2)],
            'L': [['G' for i in range(2)] for j in range(2)],
            'R': [['B' for i in range(2)] for j in range(2)],
            'F': [['R' for i in range(2)] for j in range(2)],
            'B': [['O' for i in range(2)] for j in range(2)],
        }

        faces = ['U', 'D', 'L', 'R', 'F', 'B']

        for face in faces:
            for i in range(2):
                for j in range(2):
                    if self.faces[face][i][j] != solved_rubik[face][i][j]:
                        return False
                    
        return True
    # END: Check solved
