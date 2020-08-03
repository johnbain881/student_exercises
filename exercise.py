class Exercise:
    def __init__(self, exercise, language):
        self.exercise = exercise
        self.language = language


    def __str__(self):
        return (f"Try to do {self.exercise} in {self.language}")