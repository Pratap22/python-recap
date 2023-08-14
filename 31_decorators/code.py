# Decorator in Python

def make_pretty(func):
    def inner():
        print("I got decorated")
        print("Learn With Pratap")
        func()
    return inner

def ordinary():
    print("I am ordinary")

def ordinary1():
    print("I am ordinary1")

# decorated_func = make_pretty(ordinary1)

# decorated_func()

@make_pretty
def ordinary2():
    print("I am ordinary2")

ordinary2()

def smart_divide(func):
    def inner(a,b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            print("Uh Oh!! Cannot divide")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

divide(7,0)