num1 = int(input("batas bawah: "))
num2 = int(input("batas atas: "))
count = 0

if num1 < 0 or num2 < 0:
    print("Batas bawah dan atas tidak boleh di bawah Nol")
elif num1 % 2 == 1:
    for i in range(num1, num2, 2):
        print(i)
        count += i
else:
    num1 += 1
    for i in range(num1, num2, 2):
        print(i)
        count += i
        
print("total :", count)
