from datetime import datetime

def logger(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now().strftime("%H:%M:%S"))
        func()
    return wrapper

@logger
def greet():
    print("Hello, Welcome!")

greet()
