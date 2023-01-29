number_of_tabs = int(input())
salary = int(input())

facebook = 0
instagram = 0
reddit = 0

for i in range(number_of_tabs):
    website = input()
    if website == "Facebook":
        facebook += 1
    elif website == "Instagram":
        instagram += 1
    elif website == "Reddit":
        reddit += 1
    fine = facebook * 150 + instagram * 100 + reddit * 50
    if fine - salary >= 0:
        break
if fine - salary >= 0:
    print(f'You have lost your salary.')
else:
    diff = abs(fine - salary)
    print(diff)
