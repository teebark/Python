hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    pay = 40 * r + 1.5 * r * (h - 40)
else:
    pay = h * r
print (pay)