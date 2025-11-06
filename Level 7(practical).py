student = {
    "name" : "Ama",
    "age" : 19,
    "grade" : "A"
}
print(f'Question 1: {student["name"]}\n')

student["school"] = "Legon"
print(f'Question 2: {student}\n')

student["grade"] = "B+"
print(f'Question3: {student["grade"]}\n')

print("===Question 4===")
for key,value in student.items():
    print(f'{key}: {value}')

scores = {"Math": 85, "English": 90, "Science": 88}

student["results"] = scores
print(f'\nQuestion 5: {student}')
