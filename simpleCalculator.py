# simpleCalculator

def main():
    is_working = True

    while is_working:
        print("--------------------------------------------------------")
        print("Just type \"+, -, x/X, /\" between the numbers!")
        print("It's like a typical calculator that will show the total!")
        print("If you click \"Enter\"!")
        print("--------------------------------------------------------")
        print("Type 'exit' anytime to quit.")
        print("--------------------------------------------------------")

        mag_sulat_ka = input("> ").strip()

        if mag_sulat_ka.lower() == "exit":
            print("Tanginamo alis! Thank You!")
            break

        mag_sulat_ka = mag_sulat_ka.replace("x", "*")

        try:
            result = eval(mag_sulat_ka)
            print(result)
        except ZeroDivisionError:
            print("Error! cannot divide by zero.")
        except NameError:
            print("Invalid input! TANGA KA \"exit/EXIT nga lang eh\"")
        except Exception as e:
            print("Something went wrong:", e)


main()
