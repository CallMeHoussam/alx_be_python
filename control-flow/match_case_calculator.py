first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match operator :
    case "*" :
        result = first * second
        print("The result is ",result)
match operator :
    case "+" :
        result = first + second
        print("The result is ",result)
match operator :
    case "-" :
        result = first - second
        print("The result is ",result)
match operator :
    case "/" :
        if second == 0 :
            print("Cannot divide by zero.")
        else :
            result = first / second
            print("The result is ",result)