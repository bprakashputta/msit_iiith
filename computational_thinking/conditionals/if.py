def foo(x):
    if x%3==0:
        print("3")
    elif x%5==0:
        print("5")
    elif x%3==0 and x%5==0:
        print("3 and 5")

foo(15)