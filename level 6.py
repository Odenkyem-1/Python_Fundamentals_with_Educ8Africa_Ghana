'''
DATA STRUCTURES
-LISTS
-DICTIONARY
-TUPLE
-Sets

#declearing a list
ip_list = ["10.10.10.26","192.168.1.5","192.167.15.3","192.205.0.224"]

#printing the values in a list with a `for-loop`
for i in ip_list:
    print(i)

#Accessing the items/elements in a list (Indexing)
print(ip_list[0])
print(ip_list[1])

#Adding an element to the last position of a list
ip_list.append("128.244.21.5")
print(ip_list[-1]) #Accesing the last element

#Removing the last element using the pop function of a list
ip_list.pop()
print(ip_list)
'''

ip_list = ["10.10.10.26","192.168.1.5","192.167.15.3","192.205.0.224"]

list_remove = ["192.205.0.224","10.10.10.26"]

for i in ip_list:
    if i in list_remove:
        ip_list.remove(i)

print(ip_list)