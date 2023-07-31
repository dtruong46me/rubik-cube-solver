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
        # Map random int to face name
        faces = {
            1 : 'U',
            2 : 'D',
            3 : 'L',
            4 : 'R',
            5 : 'F',
            6 : 'B'
        }

        # Map random int to direction
        directions = {
            1 : ('clockwise', ''),
            2 : ('counterclockwise','\'')
        }

        # Random according to n_suffles
        suffle_seq = []
        for _ in range(n_suffles):
            (face_rand, direction_rand) = (randint(1,6), randint(1,2))

            face = faces[face_rand]
            direction = directions[direction_rand][0]

            encode = directions[direction_rand][1]
            
            # print(face_rand, face, direction)
            suffle_seq.append(face + encode)
            self.rotate_cube(face, direction)

        print("\nSuffle Sequence: ")
        for i in range(n_suffles):
            print(suffle_seq[i], end = ' ')
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


    # Rotate 'U' face clockwise
    def rotate_U(self, direction):
        if direction == 'clockwise':
            self.rubik['U'][0][0], self.rubik['U'][0][1], self.rubik['U'][0][2], self.rubik['U'][1][0],\
            self.rubik['U'][1][2], self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2] =\
            self.rubik['U'][2][0], self.rubik['U'][1][0], self.rubik['U'][0][0], self.rubik['U'][2][1],\
            self.rubik['U'][0][1], self.rubik['U'][2][2], self.rubik['U'][1][2], self.rubik['U'][0][2]

            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2],\
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2],\
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2],\
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2] = \
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2],\
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2],\
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2],\
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2]

        elif direction == 'counterclockwise':
            self.rubik['U'][0][0], self.rubik['U'][0][1], self.rubik['U'][0][2], self.rubik['U'][1][0],\
            self.rubik['U'][1][2], self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2] =\
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2], self.rubik['U'][1][1],\
            self.rubik['U'][2][1], self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0]

            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2],\
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2],\
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2],\
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2] = \
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2],\
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2],\
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2],\
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2]
        
        else:
            print('Invalid direction!')
    
    # Rotate 'D' face clockwise  
    def rotate_D(self, direction):
        if direction == 'clockwise':
            self.rubik['D'][0][0], self.rubik['D'][0][1], self.rubik['D'][0][2], self.rubik['D'][1][0],\
            self.rubik['D'][1][2], self.rubik['D'][2][0], self.rubik['D'][2][1], self.rubik['D'][2][2] =\
            self.rubik['D'][2][0], self.rubik['D'][1][0], self.rubik['D'][0][0], self.rubik['D'][2][1],\
            self.rubik['D'][0][1], self.rubik['D'][2][2], self.rubik['D'][1][2], self.rubik['D'][0][2]

            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2],\
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2],\
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] = \
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2],\
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2],\
            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2]

        elif direction == 'counterclockwise':
            self.rubik['D'][0][0], self.rubik['D'][0][1], self.rubik['D'][0][2], self.rubik['D'][1][0],\
            self.rubik['D'][1][2], self.rubik['D'][2][0], self.rubik['D'][2][1], self.rubik['D'][2][2] =\
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2], self.rubik['D'][1][1],\
            self.rubik['D'][2][1], self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0]

            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2],\
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2],\
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] = \
            self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2],\
            self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2],\
            self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2]
        
        else:
            print('Invalid direction!')

    # Rotate 'L' face clockwise
    def rotate_L(self, direction):
        if direction == 'clockwise':
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2], self.rubik['L'][1][0],\
            self.rubik['L'][1][2], self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2] =\
            self.rubik['L'][2][0], self.rubik['L'][1][0], self.rubik['L'][0][0], self.rubik['L'][2][1],\
            self.rubik['L'][0][1], self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2]

            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0],\
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0],\
            self.rubik['B'][2][2], self.rubik['B'][1][2], self.rubik['B'][0][2],\
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0] = \
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0],\
            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0],\
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0],\
            self.rubik['B'][2][2], self.rubik['B'][1][2], self.rubik['B'][0][2]
        
        elif direction == 'counterclockwise':
            self.rubik['L'][0][0], self.rubik['L'][0][1], self.rubik['L'][0][2], self.rubik['L'][1][0],\
            self.rubik['L'][1][2], self.rubik['L'][2][0], self.rubik['L'][2][1], self.rubik['L'][2][2] =\
            self.rubik['L'][0][2], self.rubik['L'][1][2], self.rubik['L'][2][2], self.rubik['L'][1][1],\
            self.rubik['L'][2][1], self.rubik['L'][0][0], self.rubik['L'][1][0], self.rubik['L'][2][0]

            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0],\
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0],\
            self.rubik['B'][2][2], self.rubik['B'][1][2], self.rubik['B'][0][2],\
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0] = \
            self.rubik['D'][0][0], self.rubik['D'][1][0], self.rubik['D'][2][0],\
            self.rubik['B'][2][2], self.rubik['B'][1][2], self.rubik['B'][0][2],\
            self.rubik['U'][0][0], self.rubik['U'][1][0], self.rubik['U'][2][0],\
            self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0]

        else:
            print('Invalid direction!')

    # Rotate 'R' face clockwise  
    def rotate_R(self, direction):
        if direction == 'clockwise':
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2], self.rubik['R'][1][0],\
            self.rubik['R'][1][2], self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] =\
            self.rubik['R'][2][0], self.rubik['R'][1][0], self.rubik['R'][0][0], self.rubik['R'][2][1],\
            self.rubik['R'][0][1], self.rubik['R'][2][2], self.rubik['R'][1][2], self.rubik['R'][0][2]

            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2],\
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][1][0], self.rubik['B'][0][0],\
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2] = \
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][1][0], self.rubik['B'][0][0],\
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2],\
            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2]
        
        elif direction == 'counterclockwise':
            self.rubik['R'][0][0], self.rubik['R'][0][1], self.rubik['R'][0][2], self.rubik['R'][1][0],\
            self.rubik['R'][1][2], self.rubik['R'][2][0], self.rubik['R'][2][1], self.rubik['R'][2][2] =\
            self.rubik['R'][0][2], self.rubik['R'][1][2], self.rubik['R'][2][2], self.rubik['R'][1][1],\
            self.rubik['R'][2][1], self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0]

            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2],\
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][1][0], self.rubik['B'][0][0],\
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2] = \
            self.rubik['U'][0][2], self.rubik['U'][1][2], self.rubik['U'][2][2],\
            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2],\
            self.rubik['D'][0][2], self.rubik['D'][1][2], self.rubik['D'][2][2],\
            self.rubik['B'][2][0], self.rubik['B'][1][0], self.rubik['B'][0][0]

        else:
            print('Invalid direction!')

    # Rotate 'F' face clockwise
    def rotate_F(self, direction):
        if direction == 'clockwise':
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2], self.rubik['F'][1][0],\
            self.rubik['F'][1][2], self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2] =\
            self.rubik['F'][2][0], self.rubik['F'][1][0], self.rubik['F'][0][0], self.rubik['F'][2][1],\
            self.rubik['F'][0][1], self.rubik['F'][2][2], self.rubik['F'][1][2], self.rubik['F'][0][2]

            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = \
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0],
            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2]
        
        elif direction == 'counterclockwise':
            self.rubik['F'][0][0], self.rubik['F'][0][1], self.rubik['F'][0][2], self.rubik['F'][1][0],\
            self.rubik['F'][1][2], self.rubik['F'][2][0], self.rubik['F'][2][1], self.rubik['F'][2][2] =\
            self.rubik['F'][0][2], self.rubik['F'][1][2], self.rubik['F'][2][2], self.rubik['F'][1][1],\
            self.rubik['F'][2][1], self.rubik['F'][0][0], self.rubik['F'][1][0], self.rubik['F'][2][0]

            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = \
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0],\
            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0]

        else:
            print('Invalid direction!')

    # Rotate 'B' face clockwise
    def rotate_B(self, direction):
        if direction == 'clockwise':
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2], self.rubik['B'][1][0],\
            self.rubik['B'][1][2], self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2] =\
            self.rubik['B'][2][0], self.rubik['B'][1][0], self.rubik['B'][0][0], self.rubik['B'][2][1],\
            self.rubik['B'][0][1], self.rubik['B'][2][2], self.rubik['B'][1][2], self.rubik['B'][0][2]

            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = \
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0],
            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2]
        
        elif direction == 'counterclockwise':
            self.rubik['B'][0][0], self.rubik['B'][0][1], self.rubik['B'][0][2], self.rubik['B'][1][0],\
            self.rubik['B'][1][2], self.rubik['B'][2][0], self.rubik['B'][2][1], self.rubik['B'][2][2] =\
            self.rubik['B'][0][2], self.rubik['B'][1][2], self.rubik['B'][2][2], self.rubik['B'][1][1],\
            self.rubik['B'][2][1], self.rubik['B'][0][0], self.rubik['B'][1][0], self.rubik['B'][2][0]

            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],\
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0],\
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0] = \
            self.rubik['R'][0][0], self.rubik['R'][1][0], self.rubik['R'][2][0],\
            self.rubik['U'][2][0], self.rubik['U'][2][1], self.rubik['U'][2][2],\
            self.rubik['L'][2][2], self.rubik['L'][1][2], self.rubik['L'][0][2],
            self.rubik['D'][0][2], self.rubik['D'][0][1], self.rubik['D'][0][0]

        else:
            print('Invalid direction!')

test_rubik = RubikCube()
test_rubik.rotate_U('clockwise')
test_rubik.rotate_L('clockwise')
test_rubik.rotate_U('clockwise')
test_rubik.rotate_L('clockwise')
test_rubik.display()