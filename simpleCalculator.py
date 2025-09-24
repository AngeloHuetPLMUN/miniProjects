# simpleCalculator

def main():
    print("--------------------------------------------------------")
    print("Just type \"+, -, x/X, /\" between the numbers!")
    print("Its like a typical calculator that will show the total!")
    print("If you click \"Enter\"!")
    print("--------------------------------------------------------")

    num = (input("> "))
    num = num.replace("x", "*").lower()

    try:
        result = eval(num)
        print(result)
    except ZeroDivisionError:
        print("Error! Cannot Division by zero.")
    except Exception:
        print("Invalid Input!")


main()
