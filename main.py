# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# # append добавляет 3 элементом в массив [5000, 6000] число 7000  #[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# list1[2][2].insert(3, 8000)  # insert указывает индекс куда нужно добавить новое число
# print(list1)  # [10, 20, [300, 400, [5000, 6000, 7000, 8000], 500], 30, 40]

# list2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# print(list2[2][1][2])  # ['f', 'g']
# list2[2][1][2].append(["h", "i", "j"])  # ['a', 'b', ['c', ['d', 'e', ['f', 'g', ['h', 'i', 'j']], 'k'], 'l'], 'm', 'n']
# print(list2)

# s = [1, 2, 3, 'a', ['b', 'c', 'python'], 4, 5, []]
# print(s[4][2])  # python

# a = input("boy or girl: ").lower()
# b = int(input("kg: "))
# if a == "boy" and b >= 10 or a == "girl" and b >= 5:
#     print("Great job, you got 5")
# else:
#     print("Try again")


# a = int(input(": "))
# b = int(input(": "))
# c = int(input(": "))
#
# if a < b and a < c:
#     print(a)
# elif a > b and b < c:
#     print(b)
# elif c < a and b > c:
#     print(c)
#
# num = input("Enter 3 numbers: ").split()
# print(num)
# print(min([int(num[0]), int(num[1]), int(num[2])]))
# a, b, c = int(input(": ")), int(input(": ")), int(input(": "))
# print(min([a, b, c]))


# s = input(": ")
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") >= 2:
#     print(s.find("f"), s.rfind("f"))
# else:
#     print("F not defined")


# g = int(input(": "))
# if g < 25:
#     print("f")
# elif 25 <= g < 45:
#     print("e")
# elif 45 <= g < 50:
#     print("d")
# elif 50 <= g < 60:
#     print("c")
# elif 60 <= g < 80:
#     print("b")
# elif g > 80:
#     print("a")
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a==b==c:
#     print("Equilateral")
# elif a==b or b==c or a==c:
#     print("Isosceles")
# else:
#     print("triangle")

# a = "password"
# b = input("enter password: ")
# if a == b:
#     print("Welcome")
# else:
#     print("Try again")

# a = input("Enter word: ")
# if len(a) > 3 and a.endswith("ing"):
#     print(a.replace("ing", "ly"))
# elif len(a) > 3 and a[-3:] != "ing":
#     print(a + "ing")
# elif len(a) <= 3:
#     print(a)


x1, y1 = int(input("x1:")), int(input("y1:"))
x2, y2 = int(input("x2:")), int(input("y2:"))
x3, y3 = int(input("x3:")), int(input("y3:"))

a2 = (x1 - x2) ** 2 + (y1 - y2) **2
b2 = (x2 - x3)**2 + (y2 - y3)**2
c2 = (x3 - x3)**2 +(y3 - y1) **2
if a2+b2 ==c2 or a2+c2 == b2 or c2+b2 == a2:
    print("Right triangle")
else:
    print("not right")


a = int(input(":"))
b = int(input(":"))
s = input("Enter + - / *: ")
if s == "+":
    print(a, "+", b, "=", a + b)
elif s == "-":
    print(a, "-", b, "=", a - b)
elif s == "*":
    print(a, "*", b, "=", a * b)
elif s == "/":
    if b != 0:
        print(a, "/", b, "=", a / b)
    else:
        print("Error")

v = int(input("Скорость водителя: "))
if v <= 70:
    print("OK")
else:
    p = (v - 70)//5
    if p < 12:
        print("Points: ", p)
    else:
        print("License cancelled")
