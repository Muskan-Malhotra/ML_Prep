# data={}
# data = [{"name":"apple","Price":"500"},{"name":"banana","price":"1500"}]


# name=[]
# price=[]
# for i in data:
# #{​​'name':'bitcoin','price':500}​​
#   for j in i:
# #'name','price'
#     if j == 'name':
#       name.append(i[j])
#     else:
#       if i[j].isnumeric():
#         price.append(int(i[j]))


# print(name)
# print(price)

# lst = ['51','52','53']
# for i in lst:
#   if i.isnumeric():  #return true if it is a numeric string
#     print(i)


'''
[10:29] Saurika  Tiwary(Vatika82-N) (Guest)
    price=[500, 1500, 500, 1500, None]
​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
    name= ['bitcoin', 'bitcoins','bitcoin', 'bitcoins', 'abc']
​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
    for i in range(len(price)):
if price[i]==None:
price.pop(i)
name.pop(i)
​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
    print(name,price)
'''



## persons data that starts with j
names=['john thomas','Sam','Lily','JOHN','Jonas Mark','Peter','John','Lee']

for i in names:
  if i.startswith('j') or i.startswith('J'):
    print(i)

######### Exercise 2 #########
task = 'welcome python and JOY class'

for i in range(len(task)):
  if(task[i].lower()=='o'):
    print(i)


########## armstrong number ##############
num = input("Enter the number: ")
temp = int(num)
lgt = len(list(num))

ans = 0
while(temp>0):
  rem = temp%10
  temp = temp//10  ##--> changes to 
  ans = ans+rem**lgt

if(ans == int(num)):
  print("Is an armstrong number")
else:
  print("Not an armstrong number")

#############part 2 ################
num = input("Enter the number: ")

n = len(num) #3
res=0
for i in num:
  res = int(i)**n+res

if(res == int(num)):
  print("%s Is an armstrong number" %num)
else:
  print("%s Not an armstrong number" %num)



###############Leap year ##############
y = 2025
if( y%4 == 0 and y%100 == 0):
  print("Leap year")
else:
  print("Not leap year")

###############temp check #############
temp=35;rain='no';hum=50
if temp == 15 and rain == 'no' and hum == 20:
  print('cold day')
elif temp == 35 and rain == 'no' and hum == 50:
  print('hot day')
elif rain=='yes':
  print('rainy day')
else:
  print('normal day')


###############################################
UN = input('enter un: ')

if UN == 'admin':
  PW=input('enter pw: ')
  if PW=='admin1234':
    print('success')
  else:
    print('invalid username')
    

################# QUESTION ########################
'''
bank application
deposit -> 1,50,000
if deposit -> more than 5,00,000  
2) deposit ->20,000 to 5,00,000
3)deposit -> 1000-20,000
4) deposit -> 1000, less than 1000 -> i deposit right now
'''
#############################################

deposit = int(input("Enter the amount to be deposited: "))
if(deposit == 150000):
  print("Thank you for depositing")
elif(deposit>500000):
  print("Need to deposite PAN card copy")
elif(deposit >=20000 and deposit<500000):
  print("Please print your receipt")
elif(deposit >=1000 and deposit<20000):
  print("Thank you for choosing us!")
elif(deposit<1000):
  print("Need to maintain minimum balance as per policies")

