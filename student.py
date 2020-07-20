from NSSperson import NSSperson

class Student(NSSperson):
    def __init__(self, first, last, slack):
        super().__init__(first, last, slack)
        self.exercises = []

    
    def addExercises(self, exercise):
        self.exercises.append(exercise)
