from NSSperson import NSSperson


class Instructor(NSSperson):
    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first, last, slack, cohort)
        self.specialty = specialty


    def assign(self, student, exercise):
        student.addExercises(exercise)


    def __str__(self):
        return (f"{self.first} {self.last} leads {self.cohort} using their {self.specialty}")