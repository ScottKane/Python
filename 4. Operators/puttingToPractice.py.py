

firstInput = input("Input the first number: ")
firstInput = int(firstInput)

secondInput = input("Input the second number: ")
secondInput = int(secondInput)

if firstInput < secondInput:
    secondInput = str(secondInput)
    print ("The second number ({0}) is highest".format(secondInput))
elif firstInput > secondInput:
    firstInput = str(firstInput)
    print ("The first number ({0}) is highest".format(firstInput))
else:
    print ("Both numbers are equal")
