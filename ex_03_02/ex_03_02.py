hours = input("Enter hours: ")
rate = input("Enter rate: ")

try :
    h = float(hours)
    r = float(rate)
except :
    print("Please enter numeric entry: ")
    quit()
if h <= 40 :
    pay = h * r
else :
    pay = (1.5 * r * (h-40)) + (40 * r)
print("f", pay)
