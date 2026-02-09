number = 12345
sum = 0 
while number > 0:
   remainder = number % 10 
   number = number // 10
   sum = sum+ remainder
   print("Sum of remainder: ", sum)
   