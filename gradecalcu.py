print("STUDENT GRADE CALCULATOR")
print('\n')
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
name=input("Enter student's name:")
n=int(input("Enter the number of subjects:"))
tscore=0
for i in range(n):
    score=float(input(f"Enter the score of each subject {i}: "))
    tscore=tscore+score
avg=(tscore/n)*100
grade1=grade(avg)
print("Student Name:",name)
print("Average Score:",avg)
print("Grade:",grade1)