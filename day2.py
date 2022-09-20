name = input("Enter your name: ")
acc = input("Enter your account: ")
add= input("Enter your address: ")

fname = name.split(" ")
psw = fname[0][::-1]

t1=(name,acc,add,psw)

print(t1)


'''
Enter your name: John Newman
Enter your account: 12345
Enter your address: A-64 Street,LA
('John Newman', '12345', 'A-64 Street,LA', 'namweN nhoJ')
'''


##########################################################################



