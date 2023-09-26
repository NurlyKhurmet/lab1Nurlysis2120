# 1
print("4,8,15,16,23,42") 

# 2print ("4\n8\n15\n16\n23\n42") 
#2
n = [4, 8, 15, 16, 23, 42]
for num in n:
    print(num) 
# 3
x = int(input())
print(x + 1)
print(x + 2)

# 4
x=int(input()) 
y=int(input()) 
z=int(input()) 
print(x+y+z) 

# 5
x =int(input())
print(x * x * x)
print(x * x * 6)
# 6
x=int( input()) 
y=int( input()) 
print (y//x) 
print (y%x) 
# 7
number = int(input("Enter a four-digit number: "))

thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10

print(f"thousands  {thousands}")
print(f"hundreds {hundreds}")
print(f" tens {tens}")
print(f"units  {units}")
 
 
# 8
x = int(input( ))

if x % 2 == 1:
    y = (x + 1) / 2
else:
    y = x / 2

print("result", y)


# 9
x = int(input("number: "))
result = x << 1
if result == 0:
    print("Внимание: Результат << равен нулю")
else:
    print(f"Результат << равен {result}")

# 10
try:
    num1 = float(input( ))
    num2 = float(input( ))
    operation = input( )

    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
    else:
        print("Error:")

    if result is not None:
        print(f"{num1} {operation} {num2} = {result:.3f}")

except ValueError:
    print("Error:")
except Exception as e:
    print(f"error: {str(e)}")
