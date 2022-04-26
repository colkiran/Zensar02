
import logging

logging.basicConfig(level=logging.INFO)

def multiplyMe(x, y):
    return x * y

i = int(input("Enter the first Number :"))
j = int(input("Enter the second Number :"))

logging.info("Product of {0} and {1} is {2}".format(i, j, multiplyMe(i, j)))

