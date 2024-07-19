#Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse= True)
print(grades)   # on notes 3 on list has a sort example

print('='*60)

#Task2
grade_sum = sum(grades)
grade_len = len(grades)

average_grade = grade_sum / grade_len
print("Average grade: ", average_grade)