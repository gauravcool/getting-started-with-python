def computepay(h,r):
    if h <= 40.0:
        pay = h * r
    else:
        pay = (40 * r) + (1.5 * (h-40) * r)
    return pay
hours = input("Enter hours: ")
h = float(hours)
rate = input("Enter rate: ")
r = float(rate)
p = computepay(h, r)
print("Pay",p)
