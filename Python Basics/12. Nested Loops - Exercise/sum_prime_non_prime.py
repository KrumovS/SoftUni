num = input()

sum_prime = 0
sum_non_prime = 0

while num != "stop":
    num = int(num)
    if num < 0:
        print(f'Number is negative.')
    elif num == 0:
        sum_non_prime += num
    elif num == 1:
        sum_prime += num
    else:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                sum_non_prime += num
                break
        else:
            sum_prime += num

    num = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
