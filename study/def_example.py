import random


def total(a, b):
    result = a + b
    return result


x = total(1, 2)
y = total(3, 4)

print(x)
print(y)


def get_random_number():
    number = random.randint(1, 10)
    return number


print(get_random_number())
