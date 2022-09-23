def find_length(word):
  return len(word)
x = map(find_length, ('apple', 'banana', 'cherry'))
print('length of words:', list(x))

###### two variables
def add(a,b):
  return a+b

x=map(add,(1,2,3),(5,6,7))
print("result: ",list(x))

#################### lambda function

x=map(lambda x:x**2,(5,8,9))
print("Result: ",list(x))

######### Reduce function #####
