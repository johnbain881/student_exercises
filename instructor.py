from NSSperson import NSSperson


class Instructor(NSSperson):
    def __init__(self, first, last, slack, specialty):
        super().__init__(first, last, slack)
        self.specialty = specialty


    def assign(self, student, exercise):
        student.addExercises(exercise)
