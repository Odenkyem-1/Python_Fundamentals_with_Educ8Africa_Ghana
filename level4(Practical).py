userName = input("Enter Username: ")
age = input("Enter age: ")

newName = userName[0:3]

newAge = int(age)
futureAge = newAge + 5

f_age=float(futureAge)

print(f"Hello {userName}, in 5 year you will be {f_age} years old!")

if newAge >= 18:
    print("You are an Adult")
else:
    print("You are not an adult")