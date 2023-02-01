jury = int(input())
name_of_presentation = input()

student_counter = 0
student_grade = 0
all_student_grade = 0


while name_of_presentation != "Finish":

    for i in range(jury):
        grade = float(input())
        student_counter += 1
        student_grade += grade
        all_student_grade += grade

    average_grade = student_grade / jury
    print(f'{name_of_presentation} - {average_grade:.2f}.')

    student_grade = 0
    name_of_presentation = input()

average_grade_of_all_students = all_student_grade / student_counter
print(f"Student's final assessment is {average_grade_of_all_students:.2f}.")


