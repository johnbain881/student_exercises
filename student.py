from NSSperson import NSSperson

class Student(NSSperson):
    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.exercises = []

    
    def addExercises(self, exercise):
        self.exercises.append(exercise)

    def __str__(self):
        return (f"{self.first} {self.last} is in {self.cohort}")