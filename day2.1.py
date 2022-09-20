data={}
data = [{"name":"apple","Price":"500"},{"name":"banana","price":"1500"}]


name=[]
price=[]
for i in data:
#{​​'name':'bitcoin','price':500}​​
  for j in i:
#'name','price'
    if j == 'name':
      name.append(i[j])
    else:
      if i[j].isnumeric():
        price.append(int(i[j]))


print(name)
print(price)

lst = ['51','52','53']
for i in lst:
  if i.isnumeric():  #return true if it is a numeric string
    print(i)


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
