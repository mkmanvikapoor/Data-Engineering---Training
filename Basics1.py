import random
import numpy as np

# print("Hello World")
# print(type('default string '))
# print(type(u'string with b '))
# print(type('default string '))
# print(type(b'string with b '))

# class myclass():
#   def __len__(self):
#     return 0
#
# myobject = myclass()
# print(bool(myobject))

# x = 200
# print(isinstance(x, int))

# for x in range(1, 5):
#     print(x),
#
# # for x in xrange(1, 5):
# #     print(x),
#
# try:
#
#     trying_to_check_error
#
# except NameError as err:
#
#     print
#     err, 'Error Caused'

# print(random.randrange(1, 10))
#
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
#
# for x in "banana":
#   print(x)
#
# txt = "The best things in life are free!"
# print("free" in txt)
# if "free" in txt:
#   print("Yes, 'free' is present.")
#
# b = "Hello, World!"
# print(b[2:5])
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
#
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# thisList = list(("apple", "banana", "cherry", "orange", "kiwi", "mango"))
# thisList[1:3] = ["blackcurrant", "watermelon"]
# print(thisList)

# thisList = list(("apple", "banana", "cherry"))
# thisList = ["apple", "banana", "cherry", "mango", "kiwi"]
# newList = []
# thisList.insert(2, "watermelon")
# thisList[1:2] = ["blackcurrant", "watermelon"]
# thisList.append("orange")
# tropical = ["mango", "pineapple", "papaya"]
# thistuple = ("kiwi", "strawberry")
# thisList.extend(tropical)
# thisList.extend(thistuple)
# thisList.remove("watermelon")
# thisList.pop(5)
# del thisList[2]
# thisList.clear()

# for i in range(len(thisList)):
#     print(thisList[i])

# i = 0
# while i <len(thisList):
#     print(thisList[i])
#     i = i+1
# for x in thisList:
#     if "a" in x:
#         newList.append(x)

# newList = [x for x in thisList if "a" in x]
# newList = [x for x in range(10) if x < 5]
# newList = ["hello" for x in thisList]
# newList = [x if x != "banana" else "orange" for x in thisList]
# print(newList)
# thisList.sort(reverse = True)
# thisList.sort(key = str.lower)
# myList = thisList.copy()
# myList = list(thisList)
# print(thisList)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# list1.extend(list2)
# print(list1)

# Tuples
# thisTuple = ("apple", "banana", "cherry")
# thisTuple = ("apple",)
# thisTuple = tuple(("apple", "banana", "cherry"))
# print(thisTuple)
# print(type(thisTuple))

# fruits = ("apple", "banana", "cherry", "strawberry", "rasperry")
# y = list(x)
# y[1] = "kiwi"
# y.append("orange")
# x = tuple(y)
# y = ("orange",)
# x += y
# del x

# (green, *yellow, red) = fruits
# print(yellow)

# for i in range(len(fruits)):
#   print(fruits[i])

# i = 0
# while i < len(fruits):
#   print(fruits[i])
#   i = i + 1

# mytuple = fruits * 2
#
# print(mytuple)

#Sets
# thisSet = {"apple", "banana", "cherry"}
# print(len(thisSet))
# print(type(thisSet))
# thisset = set(("litchi", "strawberry", "apple"))
# print(thisset)
#
# for x in thisset:
#     print(x)
# thisset.add("orange")
# print(thisset)

# thisset.update(thisSet)
# mylist = ["kiwi", "pineapple"]
# thisset.update(mylist)
# thisset.remove("kiwi")
# thisset.discard("kiwi")
# x = thisset.pop()
# print(x)
# for x in thisset:
#     print(x)
# # setunion = thisset.union(thisSet)
# # setunion = thisset.intersection_update(thisSet)
# # setunion = thisset.intersection(thisSet)
# setunion = thisset.symmetric_difference_update(thisSet)
# print(setunion)

#Dictonaries
# thisdict = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": 1964,
#     "colors": ["red", "blue", "white"]
# }
# print(thisdict["model"])
# print(len(thisdict))
# print(thisdict)
# print(type(thisdict))
#
# thatdict = dict(name = "John", age = 36, country = "Norway")
# y = thatdict.keys()
# print(y)
# x = thatdict.get("age")
# print(x)
# print(thatdict)
# z = thatdict.values()
# print(z)
# z = thatdict.items()
# print(z)
# thatdict["city"] = "Norway"
# print(thatdict)
# thatdict.update({"age": 46})
# thatdict.pop("name")
# print(thatdict)
# thatdict.popitem()
# print(thatdict)
# # del thisdict["country"]
# # print(thisdict)
# mydict = dict(thisdict)
# print(mydict)
# if "age" in thatdict:
#     print("Age is there in list")

# myfamily = {
#   "child1" : {
#     "name" : "EmilyS",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
#
# print(myfamily)

#If..Else
# a = 2
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
#
# a = 330
# b = 330
# print("A") if a > b else print("B")
# print("A") if a > b else print("=") if a == b else print("B")
#
# a = 33
# b = 200
#
# if b > a:
#   pass

#Matrices using nested Lists
# A = [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]
# print(A)
# print(A[1])
# print(A[1][1])
# print(A[0][-1])

# a = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
# print(a)
# print(type(a))
#
# ones_array = np.ones( (1, 5), dtype=np.int32 )
# print(ones_array)
#
# b = np.zeros( (2, 3) )
# print(b)
#
# a = np.arange(4)
# print(a)
#
# B = np.arange(12).reshape(2, 6)
# print(B)

#Matrices Operations
A = np.array([[2, 4, 5, 6], [5, -6, 3, 2], [2, 3, 4, 5]])
B = np.array([[9, 3], [3, -6]])
# C = A + B
# D = A.dot(B)
# E = A.transpose()
# print(C)
# print(D)
# print(E)

print(B[:, 1])
print(A[:2, :3])
print(A[:, 1:4])
