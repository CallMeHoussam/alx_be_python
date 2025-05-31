first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
if operator == "*" :
    result = first * second
    print("The result is ",result)
elif operator == "+" :
    result = first + second
    print("The result is ",result)
elif operator == "-" :
    result = first - second
    print("The result is ",result)
elif operator == "/" :
    
    if second == 0 :
        print("Cannot divide by zero.")
    else :
        result = first / second
        print("The result is ",result)