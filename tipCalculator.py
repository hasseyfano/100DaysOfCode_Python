print("welcome to the tip calculator")
bill=float(input("what was the total bill?  $"))
tipPercent=float(input("what percentage tip would you like to give?  10,20, or 15?"))
splitNumber=int(input("How many people to split the bill?"))
result= round((bill+(bill*tipPercent/100))/splitNumber,2)
print(f"Each person should pay: $ {result}")



