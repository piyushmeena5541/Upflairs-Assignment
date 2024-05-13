def calculator(num1,num2,operation):
    if(operation == 'add'):
      add = num1 + num2
      print("Addition of numbers is " , add)
    elif(operation == 'sub'):
      sub = num1 - num2
      print("Subtraction of numbers is " , sub)
    elif(operation == 'mul'):
      mul = num1 * num2
      print("Multiplication of numbers is " , mul)
    elif(operation == 'div'):
      div = num1 / num2
      print("Division of numbers is " , div)
    else:
      print("Invalid Operation ")  


num1 = float(input("Enter the Value of Num 1 :"))
num2 = float(input("Enter the Value of Num 2 :"))
operation = str(input("Enter the Operation :"))

calculator(num1 , num2 , operation)
