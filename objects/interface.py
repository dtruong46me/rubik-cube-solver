from cube_2x2x2 import RubikCube2

class Interface:
    def __init__(self, rubik: RubikCube2) -> None:
        self.rubik = rubik
    
    def shuffle(self, rubik, from_input=False, from_file=False):
        if from_input==True:
            self.shuffle_from_input()

        if from_file==True:
            self.shuffle_from_file()
        
        else:
            print()
            # Shuffle rubik code here
        pass

    def shuffle_from_input(self, rubik):

        pass

    def shuffle_from_file(self, rubik):

        pass