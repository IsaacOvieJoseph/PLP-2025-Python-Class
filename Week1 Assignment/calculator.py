continuityCheck = True     # To continue using calculator
while continuityCheck: 
# Collect user's arithmetic operands
  Operand1 = float(input("Enter first operand: "))
  Operand2 = float(input("Enter second operand: "))

  inValidOperator = True     # Invalid operator checker

# Collect user's interested arithmetic operation
  while inValidOperator:
    Operator = input("\n 1 => Add \n 2 => Substract \n 3 => Multiply \n 4 => Divide \n \nInput ( 1 - 4 ) to select your desired arithmetic operator: ")

    #Check Valid Operator selection
    if int(Operator) in range(1,5):
      inValidOperator = False
    else:
      print("\n*** Error: Invalid arithmetic operator ***")
      
    # Execute arithmetic operation
  if Operator == 1:
    Result = Operand1 + Operand2
    Result = f"{Operand1} + {Operand2} = {Result}"
  elif Operator == 2:
    Result = Operand1 - Operand2
    Result = f"{Operand1} - {Operand2} = {Result}"
  elif Operator == 3:
    Result = Operand1 * Operand2
    Result = f"{Operand1} x {Operand2} = {Result}"
  else:
    Result = Operand1 / Operand2
    Result = f"{Operand1} / {Operand2} = {Result}"
  print()
  print(Result)  

# To determine if to terminate calculator
  anotherRun = str(input("\nEnter 'Y' to perform another calculation: ")).upper()
  if anotherRun != "Y":
    continuityCheck = False
    print("\n ******* Thank you for using my calculator *******")

