def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Function called", count, "time(s)")
        func()

    return wrapper

@call_counter
def greet():
    print("Hello!")

n = int(input("Enter number of times to call the function: "))

for i in range(n):
    greet()
