print("\t\tSimple Calculator\n")

while (True):
    try:
        num1 = float(input("Enter the number 1:"))
        num2 = float(input("Enter the number 2:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    opr = int(input("Enter the Choice : "))
    
    match opr:
        case 1:
            print(num1,"+",num2,"=",num1+num2)
        case 2:
            print(num1,"-",num2,"=",num1-num2)
        case 3:
            print(num1,"*",num2,"=",num1*num2)
        case 4:
            print(num1,"/",num2,"=",num1/num2)
            
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
else:
    print("Invalid Input")
    
        
    