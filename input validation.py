def validate(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int) or i <= 0:
                print("Error! All arguments must be positive integers.")
                return
        func(*args)
    return wrapper

@validate
def add(a, b):
    print("Sum =", a + b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

add(x, y)
