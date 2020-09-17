import math

def ps01():
    while True:
        try:
            x = int(input("Enter number x:"))

        except ValueError:
            print("Error! This si not a number. Try again.")

        else:
            break

    while True:
        try:
            y = int(input("Enter number y:"))

        except ValueError:
            print("Error! This si not a number. Try again.")

        else:
            print("The x is " + str(x)+ "\n"
                  " The y is " +str(y)+ "\n"
                  "x raised the power y is " + str(x**y) + "\n" 
                  "Log(base2) of x is " + str(math.log(x,2)))
            break


ps01()



