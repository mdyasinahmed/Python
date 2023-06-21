marks = [95, 98, 97]

marks.insert(0, 99)

print(99 in marks)

print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i+=1

marks.clear()
print(marks)