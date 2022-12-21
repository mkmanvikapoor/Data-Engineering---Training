# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print("Negative changed to zero")
# elif x == 0:
#     x == 0
#     print("zero")
# else:
#     print("more")
#
# words = ['cat', 'window', 'defenstrate']
# for w in words:
#     print(w, len(w))
#
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)
#
# a = list(range(0, 10, 3))
# print(a)
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print("Not a prime number")
#             break
#         else:
#             print("Prime Number")

# a = bool(set())
# print(a)
#
#
# def even_odd(number):
#     if number % 2:
#         return 'odd number'
#     else:
#         return 'even number'
#
# result1 = even_odd(7)
# print(result1)
# result2 = even_odd(4)
# print(result2)

# a = 5
# b = 7
# print(a, "is greater") if (a>b) else print(b, "is greater")

#Short circuiting
# def check(i):
#     print("geeks")
#     return i
#
# print(10 > 11 > check(3))
# print("\r")
# print(10 < 11 > check(3))
# print("\r")
# print(10 < 11 > check(12))
#
# a = 10
# b = 20
# c = 30
#
#
# def printreturn(l):
#     print(l)
#     return l
#
#
# if a == 11:
#     print("a == 11")
# elif b == 20 and c == 30:  # This is True
#     print("b==20 and c==30")
# elif true:
#     print("print statement is run")


# a = 10
# b = 10
# print(a==b)
#
# print(id(a))
# print(id(b))
# print(a is b)

# fruits = ["apple", "banana", "litchi"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)
#
# for x in range(1, 12, 2):
#     if x == 3: break
#     print(x)
# else:
#     print("finally finished")
#
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)

#Iterators
# mystr = "banana"
# myit = iter(mystr)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#enumerate
# l1 = ["eat", "sleep", "repeat"]
# for elem in enumerate(l1):
#     print(elem)
# for count, elem in enumerate(l1, 50):
#     print(count, elem)

#while loops
i = 1
while i<6:
    print(i)
    if i == 3:
        # break
        # continue
    i +=1