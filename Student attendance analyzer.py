
attendance = ["Present", "Absent", "Present", "Present", "Absent", "Present"]

present_count = 0
absent_count = 0

for status in attendance:
    if status == "Present":
        present_count = present_count + 1
    else:
        absent_count = absent_count + 1

print("Attendance Summary")
print("------------------")
print("Total Present Days:", present_count)
print("Total Absent Days:", absent_count)

    