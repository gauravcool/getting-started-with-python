hours = input("Enter hours: ")
h = float(hours)
rate = input("Enter rate: ")
r = float(rate)
if h <= 40 :
    pay = h * r
else :
    pay = (1.5 * r * (h-40)) + (40 * r)
print(pay)
