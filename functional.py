from decorators import timer

# @do_twice
# def say_whee():
#     print("whee!")

#print(say_whee())
# say_whee()

# def greet(name):
#     print(f"Hello {name}")
# print(say_whee.__name__)
# help(say_whee)
# greet("Manvi")

# def return_greeting(name):
#         print("Creating greeting")
#         return f"Hi {name}"
#
# return_greeting("Manvi")
#
# print(return_greeting)
@timer
def time_spent(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)])

time_spent(10)

