from datetime import date
# class Dog:
#     species = "Canis familiaris"  #Class Atrributes
#     def __init__(self, name, age):  #instance attributes
#         self.name = name
#         self.age = age
#         # self.breed = breed
#
#     # def description(self):
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# buddy = Dog("harry", 6)
# jim = Dog("Jim", 6, "Bulldog")
# print(buddy.name)
# print(buddy.species)
# print(buddy.description())
# print(buddy)
# print(jim)

# class Bulldog(Dog):
#     def speak(self, sound = "Arf"):
#         # return f"{self.name} barks {sound}"
#         return super().speak(sound)

# jim = Bulldog("Jim", 5)
# print(jim)
# print(type(jim))
# print(isinstance(jim, Dog))
# print(jim.speak())
# print(jim.speak("Grrr"))

#Inheritance
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("Idnumber is {}".format(self.idnumber))

# class Company:
#     def __init__(self):
#         self._project = "NLP"
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         # self.__salary = salary
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee Name", self.name)
#         print("Project:", self._project)
#
# c = Employee("Manvi")
# c.show()
#
# print("Project:", c._project)
        # Person.__init__(self, name, idnumber)

    # def details(self):
    #     print("My name is {}".format(self.name))
    #     print("Idnumber is {}".format(self.idnumber))
    #     print("Post is {}".format(self.post))
# emp = Employee("Manvi", 20000)
# print("Name:", emp.name)
# print("Salary:", emp._Employee__salary)
# a = Employee("Manvi", 110262, 20000, "Trainee")
# a.display()
# a.details()

# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#     def flight(self):
#         print("Most of the birds can fly")
#
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly")

# class ostrich(Bird):
#     def flight(self):
#         print("Ostrichs cannot fly")
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ostr = ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_spr.intro()
# obj_spr.flight()
#
# obj_ostr.intro()
# obj_ostr.flight()


# class A(object):
#     def __init__(self, something):
#         print("A init called")
#
#
# class B(A):
#     def __init__(self, something):
#         print("B init called")
#         A.__init__(self, something)
#
# obj = B("something")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year -year)
#
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
# person1 = Person("Manvi", 26)
# person2 = Person.fromBirthYear('Mayank', 1994)
#
# print(person1.age)
# print(person2.age)
#
# print(Person.isAdult(26))

# def insertToFile():
#
# def getFromFile():








