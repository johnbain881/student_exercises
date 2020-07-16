class Student:
    def __init__(self, first, last, slack):
        self.first = first
        self.last = last
        self.slack = slack
        self.cohort = ""
        self.exercises = []

    
    def addExercises(self, exercise):
        self.exercises.append(exercise)
