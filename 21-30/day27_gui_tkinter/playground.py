def add(*args):
    total = 0
    for nums in args:
        total += nums
    return total


print(add(2, 5, 7, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # self.make = kw["make"] # this will crash of no arguments are provided. instead use get()
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Subaru", model="Legacy")
print(my_car.make)
