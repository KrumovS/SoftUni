steps_goal = 10000
total_steps = 0

going_home = False

while not going_home:
    steps = input()
    if steps == "Going home":
        steps = input()
        total_steps += int(steps)
        going_home = True

    else:
        total_steps += int(steps)
        if total_steps >= int(steps_goal):
            break

differance = abs(steps_goal - total_steps)

if total_steps < steps_goal:
    print(f'{differance} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{differance} steps over the goal!')
