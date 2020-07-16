class Instructor:
    def __init__(self, first, last, slack, specialty):
        self.first = first
        self.last = last
        self.slack = slack
        self.cohort = ""
        self.specialty = specialty


    def assign(self, student, exercise):
        student.addExercises(exercise)
