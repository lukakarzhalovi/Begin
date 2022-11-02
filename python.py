'''
import random
random = random.randrange(2)
print(random)

def FunctionF():
    x =input("შეიყვანე სიტყვა 'python': ")
    Word = ""
    for i in x:
        if i == "y":
            continue
        else:
            Word += i
    return Word

def Function0():
    y = input("შეიყვანე სიტყვა 'python': ")
    Word = ""
    for i in y:
        if i == "o":
            continue
        else:
            Word += i
    return Word   

if random == 0:
    print(Function0())
else:
    print(FunctionF())


x =input("შეიყვანე სიტყვა:  ")
count= 0
for i in x:
    if i == "d":
        count+=1
print(count)

def Number():
    x = input("შეიყვანე სიტყვა: ")
    count= 0
    for i in x:
        if i == "d":
            count+=1
    return count


if  count > 5:
    print("ბევრია")
else:
    print(Number())


numbers =input("შეიყვანეთ რიცხვების კომბინაცია: ")
Palindrom = numbers[::-1]
print(Palindrom)
def Number3():
    b = ""
    for i in range(len(numbers)):
        if i % 2 != 0:
            continue
        else:
            b+=numbers[i]
    return b


def Number2():
    b = ""
    for i in range(len(numbers)):
        if i % 2 == 0:
            continue
        else:
            b+=numbers[i]
    return b

if numbers == Palindrom:
    print(Number3())
else:
    print(Number2())
'''
x = input("შეიყვანეთ რიცების მიმდევრობა: ")
i = 0
count = 0
def datvla():
    while i < len(x):
        print(x[i:i+2])
        i+=1
        if x[i:i+2] == "53":
            count+=1
    return count
print(datvla())
