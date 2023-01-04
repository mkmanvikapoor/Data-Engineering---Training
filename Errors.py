# print(10 * (1/0))
import sys
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#
#     x, y = inst.args
#     print('x =',x)
#     print('y =', y)
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# def this_fails():
#     x = 1/0
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print("Handling error:", err)

# try:
#     raise NameError('Hi Manvi')
# except NameError:
#     print("Name exception is raised")
#     raise

# try:
#     open("database.sqlite")
# except OSError as exc:
#     raise RuntimeError from exc

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye')

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
#
# print(bool_return())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError:
        print("Type Error")
    else:
        print("result is", result)
    finally:
        print("finally statement executed")

divide(2,1)
divide(2,0)
divide("2", "1")
