counter = 0
arr = []
max = -1
while True :
    val = input("Enter a number: ")
    if val == 'done' :
        break
    try :
        fval = int(val)
    except :
        print('Invalid input')
        continue
    counter = counter + 1
    arr.append(fval)
    min = arr[0]
#print('ALL DONE')
for el in arr :
    if(el > max) :
        max = el
print('Maximum is',max)
for el2 in arr :
    if(min > el2) :
        min = el2
print('Minimum is',min)
