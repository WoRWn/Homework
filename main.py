a = str(input("Введите строку: ")).lower()
length = len(a) // 2
k = 0
for i in range(length):
    if a[i] == a[len(a)-1-i]:
        k += 1
if k == length:
    print("True")
else:
    print("False")