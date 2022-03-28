def solution():
    number = int(input('Enter a two-digit number.This number should be between 10 and 99. That is, 9>n<100:'))
    b = []
    if 9 < number < 100:
        a = str(number)
        for i in range(0, len(a)):
            b.append(int(a[i:i + 1]))
        return sum(b)
    else:

        return 'Enter a two-digit number. Please!'


print(solution())
