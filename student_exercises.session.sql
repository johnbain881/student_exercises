DROP TABLE IF EXISTS Cohort;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS Student_Exercises;

CREATE TABLE Cohort (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE Student (
    id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES Cohort(id)
);
CREATE TABLE Instructor (
    id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slack_handle TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    specialty TEXT NOT NULL, 
    FOREIGN KEY(cohort_id) REFERENCES Cohort(id)
);
CREATE TABLE Exercise (
    id INTEGER NOT NULL PRIMARY KEY,
    exercise TEXT NOT NULL,
    language TEXT NOT NULL
);

CREATE TABLE Student_Exercises (
    id INTEGER NOT NULL PRIMARY KEY,
    instructor_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY(instructor_id) REFERENCES Instructor(id),
    FOREIGN KEY(student_id) REFERENCES Student(id),
    FOREIGN KEY(exercise_id) REFERENCES Exercise(id)
);

INSERT INTO Cohort (name)
Values ("Day Cohort 40");
INSERT INTO Cohort (name)
Values ("Day Cohort 39");
INSERT INTO Cohort (name)
Values ("Day Cohort 38");


INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("John", "Bain", "johnbain", 1);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Daniel", "Meza", "danielmeza", 2);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Kaleb", "Moran", "kalebmoran", 3);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Zach", "Nicholson", "zachnicholson", 1);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Elijah", "Lavoie", "elijahlavoie", 2);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Tanner", "Brainard", "tannerbrainard", 3);
INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
Values ("Zane", "Bliss", "zanebliss", 3);

INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id, specialty)
Values ("Joe", "Shepherd", "joes", 1, "dad jokes");
INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id, specialty)
Values ("Bryan", "Nilsen", "bry", 2, "helpful");
INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id, specialty)
Values ("Madi", "Peper", "mad", 3, "kind");

INSERT INTO Exercise (exercise, language)
Values ("Classes", "Python");
INSERT INTO Exercise (exercise, language)
Values ("React", "JavaScript");
INSERT INTO Exercise (exercise, language)
Values ("CashToCoins", "Python");
INSERT INTO Exercise (exercise, language)
Values ("Styling", "CSS");
INSERT INTO Exercise (exercise, language)
Values ("ChickenMonkey", "JavaScript");

INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (1, 1, 1);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (2, 1, 2);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (3, 2, 3);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (1, 2, 4);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (2, 3, 5);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (3, 3, 1);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (1, 4, 2);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (2, 4, 3);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (3, 5, 4);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (1, 5, 5);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (2, 6, 1);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (3, 6, 2);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (1, 7, 3);
INSERT INTO Student_Exercises (instructor_id, student_id, exercise_id)
Values (2, 7, 4);



select
                    e.Id ExerciseId,
                    e.exercise,
                    s.Id,
                    s.first_name,
                    s.last_name,
                    i.Id instructorId,
                    i.first_name instructor_first,
                    i.last_name instructor_last
                from Exercise e
                join Student_Exercises se on se.Exercise_Id = e.Id
                join Student s on s.Id = se.Student_Id
                join Instructor i on s.Id = se.Instructor_Id;