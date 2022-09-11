firstNumber = int(input("Please enter your first number: "))
secondNumber = int(input("Please enter your second number: "))
solution = ""
for i in range(firstNumber, secondNumber):
    if i%7==0 and i%5!=0:
        solution += str(i) +" "
print(solution)
