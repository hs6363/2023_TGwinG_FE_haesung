# 1번
def sum(a, b):
    # your code
    return a + b

# 2번
def sub(a, b):
    # your code
    return a - b

# 3번
def mul(a, b):
    # your code
    return a * b

# 4번
def div(a, b):
    # your code
    return a / b

# 5번
def distance(x1, y1, x2, y2):
    # your code
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return d

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    # your code
    return lylics[21:31]

# 7번
def reverseStr(string):
    # your code
    return string[::-1]

string = input("reverse할 string을 입력해주세요")
print(reverseStr(string))

# 8번
def introduce():
    # your code
    userName = input("이름을 입력하세요 : ")
    userHobby = input("취미를 입력하세요 : ")
    userUniv = input("재학 중인 학교를 입력하세요 : ")
    userBday = input("생일을 입력하세요 : ")

    return "제 이름은 " + userName + " 입니다. 취미는 " + userHobby + " 입니다. 저는 " + userUniv + "를 다니고 있습니다. 제 생일은 " + userBday[2:4] + "월 " + userBday[4:6] + "일 입니다."

print(introduce())

# 9번
def calc():
    # your code
    a = int(input("첫 번째 수를 입력하세요 : "))
    b = int(input("두 번째 수를 입력하세요 : "))
    print("두 수의 합 :", a + b)
    print("두 수의 차 :", a - b)
    print("두 수의 곱 :", a * b)
    print("두 수의 몫 :", a // b)

calc()