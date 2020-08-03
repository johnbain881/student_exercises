from instructor import Instructor
from exercise import Exercise
from cohort import Cohort
from student import Student
from student_exercise_reports import StudentExerciseReports


reports = StudentExerciseReports()
# reports.all_students()
# print("")
# reports.all_cohorts()
# print("")
# reports.all_exercises()
# print("")
# reports.javascript_exercises()
# print("")
# reports.python_exercises()
# print("")
# reports.css_exercises()
# print("")
# reports.all_instructors()
# print("")
# reports.student_exercises()
# print("")
# reports.exercise_students()
# print("")
# reports.instructor_exersises()
# print("")
# reports.student_instructor_exercises()
print("")
reports.cohorts()

# exercise1 = Exercise("cashToCoins", "Python")
# exercise2 = Exercise("coinsToCash", "Python")
# exercise3 = Exercise("chickenMonkey", "Python")
# exercise4 = Exercise("monkeyChicken", "Python")


# cohort1 = Cohort("1")
# cohort2 = Cohort("2")
# cohort3 = Cohort("3")


# student1 = Student("john", "bain", "johnbain")
# student2 = Student("daniel", "meza", "danielmeza")
# student3 = Student("kirk", "sudduth", "kirksudduth")
# student4 = Student("felipe", "moura", "felipemoura")


# instructor1 = Instructor("Joe", "Shephard", "JoeShephard", "Dad Jokes")
# instructor2 = Instructor("Bryan", "Nilsen", "BryanNilsen", "Rock")
# instructor3 = Instructor("Madi", "Peper", "MadiPeper", "Help")


# cohort1.students.append(student1)
# cohort1.students.append(student2)
# cohort2.students.append(student3)
# cohort3.students.append(student4)


# cohort1.instructors.append(instructor1)
# cohort2.instructors.append(instructor2)
# cohort3.instructors.append(instructor3)


# instructor1.assign(student1, exercise1)
# instructor1.assign(student1, exercise2)
# instructor1.assign(student2, exercise3)
# instructor1.assign(student2, exercise4)

# instructor2.assign(student3, exercise1)
# instructor2.assign(student3, exercise2)

# instructor3.assign(student4, exercise3)
# instructor3.assign(student4, exercise4)


# students = [student1, student2, student3, student4]
# exercises = [exercise1, exercise2, exercise3, exercise4]
# instructors = [instructor1, instructor2, instructor3]

# for student in students:
#     print_string = ""
#     for exercise in student.exercises:
#         print_string += f"{exercise.exercise} "
#     print(f"{student.first} is working on {print_string}")


# for instructor in instructors:
#     print(f"{instructor.first} {instructor.last} {instructor.specialty}")

