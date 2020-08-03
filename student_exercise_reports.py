import sqlite3
from student import Student
from exercise import Exercise
from instructor import Instructor
from cohort import Cohort

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/useradd/workspace/python/student_exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.Id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def all_cohorts(self):

        """Retrieve all of the exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            SELECT *
            FROM Cohort
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def all_exercises(self):

        """Retrieve all of the exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            SELECT *
            FROM Exercise
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def javascript_exercises(self):

        """Retrieve all of the exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            SELECT *
            FROM Exercise
            WHERE Exercise.language = "JavaScript"
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def python_exercises(self):

        """Retrieve all of the exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            SELECT *
            FROM Exercise
            WHERE Exercise.language = "Python"
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def css_exercises(self):

        """Retrieve all of the exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            SELECT *
            FROM Exercise
            WHERE Exercise.language = "CSS"
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def all_instructors(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[6], row[5])
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select i.Id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.cohort_id,
                i.specialty,
                c.name
            from Instructor i
            join Cohort c on i.cohort_id = c.Id
            order by i.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def student_exercises(self):
        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.exercise,
                    s.Id,
                    s.first_name,
                    s.last_name
                from Exercise e
                join Student_Exercises se on se.Exercise_Id = e.Id
                join Student s on s.Id = se.Student_Id
            """)

            dataset = db_cursor.fetchall()
            for row in dataset:
                the_exercise_name = row[1]
                student_name = f"{row[3]} {row[4]}"


                if the_exercise_name not in exercises:
                    exercises[the_exercise_name] = [student_name]
                else:
                    exercises[the_exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

    def exercise_students(self):
        students = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.exercise,
                    s.Id,
                    s.first_name,
                    s.last_name
                from Exercise e
                join Student_Exercises se on se.Exercise_Id = e.Id
                join Student s on s.Id = se.Student_Id
            """)

            dataset = db_cursor.fetchall()
            for row in dataset:
                the_exercise_name = row[1]
                student_name = f"{row[3]} {row[4]}"


                if student_name not in students:
                    students[student_name] = [the_exercise_name]
                else:
                    students[student_name].append(the_exercise_name)

            for the_student_name, exercises in students.items():
                print(the_student_name)
                for exercise in exercises:
                    print(f'\t* {exercise}')


    def instructor_exersises(self):
        instructor_exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.exercise,
                    i.Id,
                    i.first_name,
                    i.last_name
                from Exercise e
                join Student_Exercises se on se.Exercise_Id = e.Id
                join Instructor i on i.Id = se.Instructor_Id
            """)

            dataset = db_cursor.fetchall()
            for row in dataset:
                exercise = row[1]
                instructor = f"{row[3]} {row[4]}"

                if instructor not in instructor_exercises:
                    instructor_exercises[instructor] = [exercise]
                else:
                    instructor_exercises[instructor].append(exercise)

            for key, values in instructor_exercises.items():
                print(f"{key} has assigned:")
                for value in values:
                    print(f"\t* {value}")

    
    def student_instructor_exercises(self):
        exercises = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.exercise,
                    s.Id,
                    s.first_name,
                    s.last_name,
                    i.Id as instructor_id,
                    i.first_name as instructor_first,
                    i.last_name as instructor_last
                from Exercise e
                join Student_Exercises se on se.Exercise_Id = e.Id
                join Instructor i on i.Id = se.Instructor_Id
                join Student s on s.Id = se.Student_Id
            """)

            dataset = db_cursor.fetchall()
            for row in dataset:
                the_exercise_name = row[1]
                student_name = f"{row[6]} {row[7]} assigned this to {row[3]} {row[4]}"


                if the_exercise_name not in exercises:
                    exercises[the_exercise_name] = [student_name]
                else:
                    exercises[the_exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')


    def cohorts(self):
        cohorts = dict()
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select c.name,
                    s.first_name,
                    s.last_name,
                    i.first_name as instructor_first,
                    i.last_name as instructor_last
                from Cohort c
                join Student s on s.cohort_id = c.id
                join Instructor i on i.cohort_id = c.id
                order by c.id;
            """)

            dataset = db_cursor.fetchall()
            for row in dataset:
                cohort_name = row[0]
                instructor_name = f"{row[3]} {row[4]}"
                student_name = f"{row[1]} {row[2]}"

                if cohort_name not in cohorts:
                    cohorts[cohort_name] = {instructor_name : [student_name]}
                else:
                    cohorts[cohort_name][instructor_name].append(student_name)

            for cohort, instructors_students in cohorts.items():
                print(cohort)
                for instructor, students in instructors_students.items():
                    print("\tStudents:")
                    for student in students:
                        print(f"\t\t* {student} is in {cohort}")
                    print("\tInstructors:")
                    print(f"\t\t* {instructor} is in {cohort}")