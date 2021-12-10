def func(text):
    print(text)
    print("i am inside func")
func(5)
print("i an inside original code, means outside func")

def addition(a, b):
    print(a+b)

addition(4, 2)
print("---------------------------------")

def substract(a, b):
    return a-b

result = substract(4, 1)
print(result)

x = lambda a, b : a -b

print(x(6,5))

