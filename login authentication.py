logged_in = False

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied! Please log in first.")
    return wrapper

@login_required
def dashboard():
    print("Welcome to the Dashboard!")

choice = input("Are you logged in? (yes/no): ").lower()

if choice == "yes":
    logged_in = True

dashboard()
