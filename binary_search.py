import random
max = int(input("Enter the max value for the number to guess:"))
numArr = []
for i in range (max + 1):
    numArr.append(i + 1)
high = numArr[-1]
low = numArr[0]
num = random.randint(1, max + 1)
static = num
print("this is your lucky number:", num)
while low <= high:
    check = low + (high - low) // 2
    if numArr[check] == static:
        print("Seikai desu! Kotae wa:", numArr[check])
        break
    else:
        if numArr[check] > static:
            print("A little lower than", numArr[check])
            high = check - 1
        elif numArr[check] < static:
            print("A little higher than", numArr[check])
            low = check + 1
