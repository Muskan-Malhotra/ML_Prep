import math
'''
'welcome scientific calculator'
1.percentage....ask number..5% of 100
2.sqrt...ask number 16
3.lcm....ask number...
4.exit...stop working

if selected 5....invalid option and repeate loop
if instead of number enter string...invalid value...all to enter again the number
'''

print("*********** Welcome to Scientific Calculator ************")
print("******* Select your choice **********")
print("1. Percentage")
print("2. Square Root")
print("3. LCM")
print("4. Exit")



while True:
  
  n = int(input("Your Choice: "))
  if(n==1):
    per = input("Enter the number: ")
    num = input("Enter the amount: ")
    if(per.isalpha() or num.isalpha()):
      print("Invalid input")
      break
    ans = (int(per)/100)*(int(num))
    print("Your ans is: %s " %ans)

  elif(n==2):
    a = int(input("Enter the number to get square root"))
    print("The sqaure root is: ",math.sqrt(a))

  elif(n==3):
    num1 = int(input("Enter the first number: "))
    num2 = int(input())
    if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
      max= num1
    else:
      max= num2
    while(True):
      if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break
    max= max+ 1
  elif(n==4):
    print("EXIT")
    break
  else:
    print("Invalid choice!!")

######################### pass 
for i in 'web':
  pass
print(i)

################### continue

for cch in 'python':
  if cch == 'o':
    continue
  print(cch)