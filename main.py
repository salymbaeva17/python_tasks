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


a = int(input(": "))
b = int(input(": "))
c = int(input(": "))

if a < b and a < c:
    print(a)
elif a > b and b < c:
    print(b)
elif c < a and b > c:
    print(c)

num = input("Enter 3 numbers: ").split()
print(num)
print(min([int(num[0]), int(num[1]), int(num[2])]))
a, b, c = int(input(": ")), int(input(": ")), int(input(": "))
print(min([a, b, c]))
