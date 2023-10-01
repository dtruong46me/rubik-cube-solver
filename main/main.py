from ..objects.cube_3x3x3 import RubikCube
from ..solver.layer_solver import LayerSolver
from ..solver.cfop_solver import CFOPSolver
from ..solver.m2op_solver import M2OPSolver

def main():
    while True:
        print('WELCOME TO RUBIK CUBE SOLVER!')
        print('Enter 1: Input Rubik Cube')
        print('Enter 2: Suffle Rubik Cube')
        print('Enter 3: Solve Rubik Cube')
        print('Enter 0: Exit')

        choice = int(input('Your choice: '))

        rubik = RubikCube()
        
        if choice == 0:
            choice_quit = input('Do you want to quit the program? (Y/N): ')
            if choice_quit == 'Y' or choice_quit == 'y':
                print('Exit the program!')
                break
            elif choice_quit == 'N' or choice_quit == 'n':
                pass
            else:
                print('Invalid Input! Please try again!')

        if choice == 1:
            rubik.input_user()
        
        if choice == 2:
            num_suffle = int(input('Enter number of sequences you want to suffle: '))
            rubik.suffle(num_suffle)
        
        if choice == 3:
            while True:
                print('\nCHOOSE SOLVER TO SOLVE:')
                print(' - Enter a: Layer by Layer')
                print(' - Enter b: CFOP Solver')
                print(' - Enter c: M2OP Solver')

                choice_solver = input('Your choice: ')

                if choice_solver == 'a' or choice_solver == 'A':
                    layer_solver = LayerSolver()
                    layer_solver.sovle(rubik)
                
                elif choice_solver == 'b' or choice_solver == 'B':
                    cfop_solver = CFOPSolver()
                    cfop_solver.sovle(rubik)

                elif choice_solver == 'c' or choice_solver == 'C':
                    m2op_solver = M2OPSolver()
                    m2op_solver.sovle(rubik)

if __name__ == '__main__':
    main()