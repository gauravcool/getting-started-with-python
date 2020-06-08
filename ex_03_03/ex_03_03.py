score = input("Enter score: ")
fs = float(score)
if fs > 0.0 and fs <= 1.0 :
    if fs >= 0.9 :
        grade = 'A'
    elif fs >= 0.8 :
        grade = 'B'
    elif fs >= 0.7 :
        grade = 'C'
    elif fs >= 0.6 :
        grade = 'D'
    else :
        grade = 'F'
else :
    print("Score out of range")
    exit()
print(grade)
