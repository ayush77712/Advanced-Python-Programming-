
import threading
import time

def display_numbers():
    for i in range(1, 4):
        print("Number:", i)
        time.sleep(1)

def calculate_squares():
    for i in range(1, 4):
        print("Square:", i * i)
        time.sleep(1)

def display_messages():
    for i in range(1, 4):
        print("Hello from Thread 3")
        time.sleep(1)

t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=calculate_squares)
t3 = threading.Thread(target=display_messages)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed.")
