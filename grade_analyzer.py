grades = [45, 78, 90, 32, 100, 67, 90, 50]
passed = 0
failed = 0
total = 0
average = 0
highest = 0
highest_index = 0
more_90 = 0
min_grades = 0

for i in range(len(grades)):
    total = grades[i] + total


    if grades[i] >= 50:
        passed = passed + 1
    else:
        failed = failed + 1
    if grades[i] >= 90:
        more_90 += 1
        print(f"Grades above or equal to 90: {grades[i]} at index {i}")

average = total / len(grades)
highest = max(grades)
highest_index = grades.index(highest)
min_grades = min(grades)
min_index = grades.index(min_grades)



print(f"Students passed: {passed}")
print(f"Students failed: {failed}")
print(f"Total grades: {total}")
print(f"Average grade: {average}")
print(f"Highest grade: {highest}")
print(f"Highest grade index: {highest_index}")
print(f"More 90: {more_90}")
print(f"Min grades: {min_grades}")
print(f"Lowest grade index: {min_index}")