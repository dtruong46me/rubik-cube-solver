from copy import deepcopy
from random import randint

class RubikCube:
    def __init__(self) -> None:
        self.rubik = {
            'U' : [['W' for i in range(3)] for j in range(3)],
            'D' : [['Y' for i in range(3)] for j in range(3)],
            'L' : [['G' for i in range(3)] for j in range(3)],
            'R' : [['B' for i in range(3)] for j in range(3)],
            'F' : [['R' for i in range(3)] for j in range(3)],
            'B' : [['O' for i in range(3)] for j in range(3)]
        }
    
    # BEGIN: Suffle the Rubik Cube #
    def suffle(self, n_suffles) -> None:
        suffle_way = []
        for suffle in range(n_suffles):
            (face_rand, direction_rand) = (randint(1,6), randint(1,2))
            encode = ''
            # Encoding for the random direction
            if direction_rand == 1:
                direction = 'clockwise'
                endoce = ''
            elif direction_rand == 2:
                direction = 'counterclockwise'
                encode = '\''

            # Encoding for the random face
            if face_rand == 1:
                face = 'U'
            elif face_rand == 2:
                face = 'D'
            elif face_rand == 3:
                face = 'L'
            elif face_rand == 4:
                face = 'R'
            elif face_rand == 5:
                face = 'F'
            elif face_rand == 6:
                face = 'B'
            
            # print(face_rand, face, direction)
            suffle_way.append(face + encode)
            self.rotate_cube(face, direction)
            self.display()

        print("\nSuffle Way: ")
        for i in range(n_suffles):
            print(suffle_way[i], end = ' ')
        print('\n')  
    # END: Suffle the Rubik Cube #


    # BEGIN: Rotate the Rubik Cube #
    def rotate_cube(self, face, direction):
        if face == 'U':
            self.rotate_U(direction)
        elif face == 'D':
            self.rotate_D(direction)
        elif face == 'L':
            self.rotate_L(direction)
        elif face == 'R':
            self.rotate_R(direction)
        elif face == 'F':
            self.rotate_F(direction)
        elif face == 'B':
            self.rotate_B(direction)
        else:
            print('Invalid of the Rubik\'s Face')
    # END: Rotate the Rubik Cube #


    def rotate_U(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['U'][i][0] for i in range(3)]
        column_2 = [self.rubik['U'][i][1] for i in range(3)]
        column_3 = [self.rubik['U'][i][2] for i in range(3)]

        rotate_face_F = [self.rubik['F'][0][i] for i in range(3)]
        rotate_face_L = [self.rubik['L'][0][i] for i in range(3)]
        rotate_face_B = [self.rubik['B'][0][i] for i in range(3)]
        rotate_face_R = [self.rubik['R'][0][i] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['U'][0] = column_1
            self.rubik['U'][1] = column_2
            self.rubik['U'][2] = column_3

            self.rubik['F'][0] = rotate_face_R
            self.rubik['L'][0] = rotate_face_F
            self.rubik['B'][0] = rotate_face_L
            self.rubik['R'][0] = rotate_face_B

        elif direction == 'counterclockwise':
            self.rubik['U'][0] = column_3
            self.rubik['U'][1] = column_2
            self.rubik['U'][2] = column_1

            self.rubik['F'][0] = rotate_face_L
            self.rubik['L'][0] = rotate_face_B
            self.rubik['B'][0] = rotate_face_R
            self.rubik['R'][0] = rotate_face_F
        else:
            print('Invalid of the direction!')
    
    def rotate_D(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['D'][i][0] for i in range(3)]
        column_2 = [self.rubik['D'][i][1] for i in range(3)]
        column_3 = [self.rubik['D'][i][2] for i in range(3)]

        rotate_face_F = [self.rubik['F'][2][i] for i in range(3)]
        rotate_face_L = [self.rubik['L'][2][i] for i in range(3)]
        rotate_face_B = [self.rubik['B'][2][i] for i in range(3)]
        rotate_face_R = [self.rubik['R'][2][i] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['D'][0] = column_1
            self.rubik['D'][1] = column_2
            self.rubik['D'][2] = column_3

            self.rubik['F'][2] = rotate_face_L
            self.rubik['L'][2] = rotate_face_B
            self.rubik['B'][2] = rotate_face_R
            self.rubik['R'][2] = rotate_face_F

        elif direction == 'counterclockwise':
            self.rubik['D'][0] = column_3
            self.rubik['D'][1] = column_2
            self.rubik['D'][2] = column_1

            self.rubik['F'][2] = rotate_face_R
            self.rubik['L'][2] = rotate_face_F
            self.rubik['B'][2] = rotate_face_L
            self.rubik['R'][2] = rotate_face_B
        else:
            print('Invalid of the direction!')
    
    def rotate_L(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['L'][i][0] for i in range(3)]
        column_2 = [self.rubik['L'][i][1] for i in range(3)]
        column_3 = [self.rubik['L'][i][2] for i in range(3)]

        rotate_face_F = [self.rubik['F'][i][0] for i in range(3)]
        rotate_face_D = [self.rubik['D'][i][0] for i in range(3)]
        rotate_face_B = [self.rubik['B'][i][2] for i in range(3)]
        rotate_face_U = [self.rubik['U'][i][0] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2] = column_1
            self.rubik['L'][1][0], self.rubik['L'][1][1], self.rubik['L'][1][2] = column_2
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2] = column_3

            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0] = rotate_face_U[0], rotate_face_U[1], rotate_face_U[2]
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0] = rotate_face_F[0], rotate_face_F[1], rotate_face_F[2]
            self.rubik['B'][0][2], self.rubik['B'][1][2], self.rubik['B'][2][2] = rotate_face_D[2], rotate_face_D[1], rotate_face_D[0]
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0] = rotate_face_B[2], rotate_face_B[1], rotate_face_B[0]

        elif direction == 'counterclockwise':
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2] = column_3
            self.rubik['L'][1][0], self.rubik['L'][1][1], self.rubik['L'][1][2] = column_2
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2] = column_1

            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0] = rotate_face_D[0], rotate_face_D[1], rotate_face_D[2]
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0] = rotate_face_B[2], rotate_face_B[1], rotate_face_B[0]
            self.rubik['B'][0][2], self.rubik['B'][1][2], self.rubik['B'][2][2] = rotate_face_U[2], rotate_face_U[1], rotate_face_U[0]
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0] = rotate_face_F[0], rotate_face_F[1], rotate_face_F[2]
        else:
            print('Invalid of the direction!')

    def rotate_R(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['R'][i][0] for i in range(3)]
        column_2 = [self.rubik['R'][i][1] for i in range(3)]
        column_3 = [self.rubik['R'][i][2] for i in range(3)]

        rotate_face_F = [self.rubik['F'][i][2] for i in range(3)]
        rotate_face_D = [self.rubik['D'][i][2] for i in range(3)]
        rotate_face_B = [self.rubik['B'][i][0] for i in range(3)]
        rotate_face_U = [self.rubik['U'][i][2] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2] = column_1
            self.rubik['R'][1][0], self.rubik['R'][1][1], self.rubik['R'][1][2] = column_2
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] = column_3

            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2] = rotate_face_D[0], rotate_face_D[1], rotate_face_D[2]
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2] = rotate_face_B[2], rotate_face_B[1], rotate_face_B[0]
            self.rubik['B'][0][0], self.rubik['B'][1][0], self.rubik['B'][2][0] = rotate_face_U[2], rotate_face_U[1], rotate_face_U[0]
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2] = rotate_face_F[0], rotate_face_F[1], rotate_face_F[2]

        elif direction == 'counterclockwise':
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2] = column_3
            self.rubik['R'][1][0], self.rubik['R'][1][1], self.rubik['R'][1][2] = column_2
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] = column_1

            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2] = rotate_face_U[0], rotate_face_U[1], rotate_face_U[2]
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2] = rotate_face_F[0], rotate_face_F[1], rotate_face_F[2]
            self.rubik['B'][0][0], self.rubik['B'][1][0], self.rubik['B'][2][0] = rotate_face_D[2], rotate_face_D[1], rotate_face_D[0]
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2] = rotate_face_B[2], rotate_face_B[1], rotate_face_B[0]
        else:
            print('Invalid of the direction!')
    
    def rotate_F(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['F'][i][0] for i in range(3)]
        column_2 = [self.rubik['F'][i][1] for i in range(3)]
        column_3 = [self.rubik['F'][i][2] for i in range(3)]

        rotate_face_U = [self.rubik['U'][2][i] for i in range(3)]
        rotate_face_L = [self.rubik['L'][i][2] for i in range(3)]
        rotate_face_D = [self.rubik['D'][0][i] for i in range(3)]
        rotate_face_R = [self.rubik['R'][i][0] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2] = column_1
            self.rubik['F'][1][0], self.rubik['F'][1][1], self.rubik['F'][1][2] = column_2
            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2] = column_3

            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = rotate_face_U[0], rotate_face_U[1], rotate_face_U[2]
            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2] = rotate_face_L[2], rotate_face_L[1], rotate_face_L[0]
            self.rubik['L'][0][2], self.rubik['L'][1][2], self.rubik['L'][2][2] = rotate_face_D[0], rotate_face_D[1], rotate_face_D[2]
            self.rubik['D'][0][0], self.rubik['D'][0][1], self.rubik['D'][0][2] = rotate_face_R[2], rotate_face_R[1], rotate_face_R[0]

        elif direction == 'counterclockwise':
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2] = column_3
            self.rubik['F'][1][0], self.rubik['F'][1][1], self.rubik['F'][1][2] = column_2
            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2] = column_1

            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2] = rotate_face_R[0], rotate_face_R[1], rotate_face_R[2]
            self.rubik['L'][0][2], self.rubik['L'][1][2], self.rubik['L'][2][2] = rotate_face_U[2], rotate_face_U[1], rotate_face_U[0]
            self.rubik['D'][0][0], self.rubik['D'][0][1], self.rubik['D'][0][2] = rotate_face_L[0], rotate_face_L[1], rotate_face_L[2]
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = rotate_face_D[2], rotate_face_D[1], rotate_face_D[0]
        else:
            print('Invalid of the direction!')
    
    def rotate_B(self, direction) -> None:
        temp_rubik = deepcopy(self.rubik)
        column_1 = [self.rubik['B'][i][0] for i in range(3)]
        column_2 = [self.rubik['B'][i][1] for i in range(3)]
        column_3 = [self.rubik['B'][i][2] for i in range(3)]

        rotate_face_U = [self.rubik['U'][0][i] for i in range(3)]
        rotate_face_L = [self.rubik['L'][i][0] for i in range(3)]
        rotate_face_D = [self.rubik['D'][2][i] for i in range(3)]
        rotate_face_R = [self.rubik['R'][i][2] for i in range(3)]

        if direction == 'clockwise':
            self.rubik['B'][0] = column_1
            self.rubik['B'][1] = column_2
            self.rubik['B'][2] = column_3

            self.rubik['U'][0][0], self.rubik['U'][0][1], self.rubik['U'][0][2] = rotate_face_R[0], rotate_face_R[1], rotate_face_R[2]
            self.rubik['R'][0][2], self.rubik['R'][1][2], self.rubik['R'][2][2] = rotate_face_D[2], rotate_face_D[1], rotate_face_D[0]
            self.rubik['D'][2][0], self.rubik['D'][2][1], self.rubik['D'][2][2] = rotate_face_L[0], rotate_face_L[1], rotate_face_L[2]
            self.rubik['L'][0][0], self.rubik['L'][1][0], self.rubik['L'][2][0] = rotate_face_U[2], rotate_face_U[1], rotate_face_U[0]

        elif direction == 'counterclockwise':
            self.rubik['B'][0] = column_3
            self.rubik['B'][1] = column_2
            self.rubik['B'][2] = column_1

            self.rubik['U'][0][0], self.rubik['U'][0][1], self.rubik['U'][0][2] = rotate_face_L[2], rotate_face_L[1], rotate_face_L[0]
            self.rubik['R'][0][2], self.rubik['R'][1][2], self.rubik['R'][2][2] = rotate_face_U[0], rotate_face_U[1], rotate_face_U[2]
            self.rubik['D'][2][0], self.rubik['D'][2][1], self.rubik['D'][2][2] = rotate_face_R[2], rotate_face_R[1], rotate_face_R[0]
            self.rubik['L'][0][0], self.rubik['L'][1][0], self.rubik['L'][2][0] = rotate_face_D[0], rotate_face_D[1], rotate_face_D[2]

        else:
            print('Invalid of the direction!')

    # BEGIN: Display the Rubik Cube #
    def colored_text(self, text, color):
        colors = {
            'W': '\033[97m',   # White
            'Y': '\033[93m',   # Yellow
            'G': '\033[92m',   # Green
            'B': '\033[94m',   # Blue
            'R': '\033[91m',   # Red
            'O': '\033[33m'    # Orange
        }
        return colors[color] + text + '\033[0m'  # Reset to default color

    def display(self) -> None:
        ''' print each face of the rubik, the template like this:
        +---- U -----+----- D -----+----- L -----+----- R -----+----- F -----+----- B -----+
            W W W         Y Y Y         O O O         R R R         G G G         B B B
            W W W         Y Y Y         G G G         B B B         R R R         O O O
            W W W         Y Y Y         G G G         B B B         R R R         O O O
        +------------+-------------+-------------+-------------+-------------+-------------+
        '''

        print('\033[35m+---- U -----+----- D -----+----- L -----+----- R -----+----- F -----+----- B -----+\033[35m')
    
        for i in range(3):
            u_row = ' '.join(self.colored_text(cell, self.rubik['U'][i][j]) for j, cell in enumerate(self.rubik['U'][i]))
            d_row = ' '.join(self.colored_text(cell, self.rubik['D'][i][j]) for j, cell in enumerate(self.rubik['D'][i]))
            l_row = ' '.join(self.colored_text(cell, self.rubik['L'][i][j]) for j, cell in enumerate(self.rubik['L'][i]))
            r_row = ' '.join(self.colored_text(cell, self.rubik['R'][i][j]) for j, cell in enumerate(self.rubik['R'][i]))
            f_row = ' '.join(self.colored_text(cell, self.rubik['F'][i][j]) for j, cell in enumerate(self.rubik['F'][i]))
            b_row = ' '.join(self.colored_text(cell, self.rubik['B'][i][j]) for j, cell in enumerate(self.rubik['B'][i]))
            print('    ' + u_row + '         ' + d_row + '         ' + l_row + '         ' + r_row + '         ' +
                  f_row + '         ' + b_row)

        print('\033[35m+------------+-------------+-------------+-------------+-------------+-------------+\033[97m\n')
    # END: Display the Rubik Cube #

rubik = RubikCube()

rubik.display()