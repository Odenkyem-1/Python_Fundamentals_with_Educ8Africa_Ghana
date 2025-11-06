no_i = float(input("How many numbers are you analysing?\n"))

li_num=[]

i = 0
while i < no_i:
    num = float(input("Enter number: "))
    li_num.append(num)
    i+=1

positive_num = 0
negative_num = 0
no_of_zeros = 0

for i in li_num:
    if i < 0:
        negative_num += 1
    elif i > 0:
        positive_num += 1
    elif i == 0:
        no_of_zeros += 1
    else:
        pass

print(f'Number of positive: {positive_num}')
print(f'Number of negative: {negative_num}')
print(f'Number of zeros: {no_of_zeros}')