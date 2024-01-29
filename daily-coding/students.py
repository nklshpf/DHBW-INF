from faker import Faker
import random

fake = Faker()
print("Name:", fake.name())

students = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18, 25),
        "major": random.choice(["Computer Science", "Mathematics", "Physics", "Biology"]),
        "gpa": round(random.uniform(2.00, 4.00), 2),
        "is_international": random.choice([True, False])
    }
    students.append(student)

for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    print("Age:", student["age"])
    print("Major:", student["major"])
    print("GPA:", student["gpa"])
    print("Is International?:", student["is_international"])
    print()


first_names = []
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    first_names.append(first_name)

print(first_names)

duplicate_count = len(first_names) - len(set(first_names))

duplicate_count = {name: first_names.count(name)
                   for name in set(first_names)
                   if first_names.count(name) > 1}
print(duplicate_count)