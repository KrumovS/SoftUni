bad_grades = int(input())
question = input()


score = 0
bad_grades_counter = 0
counter = 0
last_problem = ''
condition = False

while question != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter >= bad_grades:
            condition = True
            break

    counter += 1
    score += grade
    last_problem = question
    question = input()

if condition:
    print(f'You need a break, {bad_grades_counter} poor grades.')
else:
    average_score = score / counter
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {counter}')
    print(f'Last problem: {last_problem}')
