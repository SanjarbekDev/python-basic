while True:
    try:
        x = input("Please enter a number: ")
        x+=12
        break
    except TypeError:
        x=int(x)+1
        print(f"Oops!  That was no valid number.  Try again...{x}")