students = ["hablu", "bablu", "mablu", "kablu", "chablu"]

for student in students:
    if student == "mablu":
        break;
    print(student)


for student in students:
    if student == "bablu":
        continue;
    print(student)