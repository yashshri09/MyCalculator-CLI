def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("select the operation-\n" 
      "1: add \n" 
      "2:substract\n" 
      "3:multiply\n" 
      "4:divide\n")

# input from the user

select = int(input("Select the operation 1,2,3,4: "))

number_1 = int(input("Enter the number: "))
number_2 = int(input("Enter the number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1 ,number_2))

elif select == 2:
    print(number_2, "-", number_1, "=", sub(number_2,number_1))

elif select == 3:
    print(number_1, "*", number_2, "=", mul(number_1,number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", div(number_1,number_2))

else:
    print("Invalid Input")

