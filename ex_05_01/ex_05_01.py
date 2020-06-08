counter = 0
total = 0
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
    total = total + fval
#print('ALL DONE')
if counter != 0 :
    print(total, counter, total/counter)
