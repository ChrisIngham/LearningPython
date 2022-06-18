# Problem 1
try:
    for i in ['a','b','c']:
        print(i**2)
except(TypeError):
    print("There was a type Error")

# Problem 2
x = 5
y = 0
try:
    z = x/y
except(ZeroDivisionError):
    print("Cannot Divide by 0")
finally:
    print("ALL DONE")

# Problem 3
while(True):
    try:
        val = int(input("Enter Value: "))
    except:
        print("Wrong Data Type ")
        continue
    else:
        break
print(val**2)