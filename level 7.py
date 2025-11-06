'''
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

ip_dict ={
    "PC-1": "10.10.10.10",
    "PC-2": "192.182.1.8",
    "PC-3": "209.150.45.7"
}

ip_dict["PC-4"] = "192.168.1.1"

#removing or deleting values in a dictionary
del ip_dict["PC-4"]

ip_dict.pop("PC-3")

ip_dict.popitem()


for key,value in my_dict.items():
    print(f"{key} --> {value}")
'''
random_num = [1,1,1,2,2,2,1,2,1,2,1,3,3,4,5,5,6,4,5,8,9,8,7,6,5,4,5,1,2]

frequency = {}

for num in random_num:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] += 1

#print(my_dict["brand"])
#print(ip_dict)
print(frequency)
