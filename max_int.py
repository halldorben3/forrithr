
#Ask the user to put in a value for max_int and repeat it and if the new value is higher
#then the original value it will be put as the new max_int. If the value is negative the algorithm will stop
max_int=0
num_int=int(input('Input a value: '))
while num_int >= 0:
    num_int=int(input('Input a value: '))
    if num_int > max_int:
        max_int=num_int

print("The maximum is", max_int)



