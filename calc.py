a = float(input("Enter first Number: "))
func = input("Choose * + - / or %: ")
b = float(input("Enter second number: "))

while func not in ['*', '+', '-', '/', '%']:

    func = input("Not an operator. Try + - % * / or : ")

if func == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif func == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif func == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif func == '/':
     result = a / b
     print(f"{a} / {b} = {result}")

