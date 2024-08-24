num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("choose one of the following operator + * - / % :")

match operation:
      case"+":
          result = num1 + num2
          print("Result of th operation is:", result)
      case"-":
          result = num1 - num2
          print("Result of the operation is:", result)
      case"*":
          result = num1 * num2
          print("Result of the operation is:", result)
      case"/":
          if num2 == 0:
              print("Invalid  output")
          else:
              result = num1/num2
              print("Result of the operation is:", result)
      case"%":
          if num2 == 0:
              print("Invalid output")
          else:
              print("Result of thr opeartion:",result)
      case"_":
          print("Invalid Operator")
