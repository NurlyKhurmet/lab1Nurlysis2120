# lab2Nurlysis2120
num = int(input("n:")) 
thousands, hundreds, tens, ones = num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10 
 
if thousands + ones == tens - hundreds: 
    print("YES") 
else: 
    print("NO")
