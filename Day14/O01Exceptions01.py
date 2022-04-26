
# import sys

num = 0
inv = 1
try:
    # error pron code
    inv = 1 / num
except Exception as e:
    print(e)

# except ZeroDivisionError as z:
#     print("Exception Occured......")
#     print(sys.exc_info()[0])
#     print(z)
# except TypeError as t:
#     print(sys.exc_info()[0])
#     print(t)
else:
    print(f"inv :{inv}")
finally:
    print("completed the process of division.....")
