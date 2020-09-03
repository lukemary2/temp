t = float(input("Enter temperature: "))
u = str(input("Enter unit in F/f or C/c: "))
temp = t
unit = u
t = float(temp)
u = str(unit)
if u == "C" or u == "c":
    f = '{0:.1f}'.format(9 / 5 * t + 32)
    print(f"{t} in celsius is equivalent to {f} fahrenheit.")
elif u == 'F' or u == 'f':
    c = '{0:.1f}'.format((t - 32) / 1.8)
    print(f"{t} in fahrenheit is equivalent to {c} celsius.")
else:
    print("Invalid unit(bad)")
