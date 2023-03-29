# 1번
def grade(score):
    #your code
    score = int(score)
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 60):
        return "D"
    else:
        return "F"

score = input("Enter your score : ")
print(grade(score))


# 2번
def quadrant(x, y):
    #your code
    x = int(x)
    y = int(y)
    if (x > 0):
        if (y > 0):
            return "제 1사분면"
        else:
            return "제 4사분면"
    else:
        if (y > 0):
            return "제 2사분면"
        else:
            return "제 3사분면"

x = input("Enter the x : ")
y = input("Enter the y : ")

print(quadrant(x, y))


# 3번
def leapYear(year):
    #your code
    year = int(year)
    if (year % 4 != 0):
        print("윤년이 아닙니다.")
    elif ((year % 100 == 0) and (year % 400 != 0)):
        print("윤년이 아닙니다.")
    else:
        print("윤년입니다.")

year = input("Enter the year : ")

print(leapYear(year))


# 4번
def dice(a, b, c):
    # your code
    a = int(a)
    b = int(b)
    c = int(c)
    if ((a == b) and (b == c)):
        return 10000 + 1000 * a
    elif ((a != b) and (b != c)):
        p = max (a, b, c)
        return 100 * p
    else:
        if (a == b):
            return 1000 + 100 * a
        else:
            return 1000 + 100 * c
        
a = input("Enter the first number of dice : ")
b = input("Enter the first number of dice : ")
c = input("Enter the first number of dice : ")

print(dice(a, b, c))


# 5번
def alarm(time):
    # your code
    time = int(time)
    time += 10000
    time = str(time)
    time = time[1:]

    hour = int(time[0:2])
    min = int(time[2:4])

    if (min >= 45):
        return str(hour) + "시" + str(min - 45) + "분"
    else:
        if (hour != 00):
            return str((hour - 1)) + "시" + str((60 + (min - 45))) + "분"
        else:
            return "23시" + str((60 + (min - 45))) + "분"

time = input("Enter the alarm time : ")

print(alarm(time)) 
