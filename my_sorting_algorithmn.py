import random

list1 = [x for x in range(1000)]

random.shuffle(list1)

print("Enter The Numer of Steps(Accuracy):", "A large value may reduce perfomance")
steps = int(input())

for k in range(steps):
    for i in range(len(list1)):
        if (i < len(list1) - 1):
            if (list1[i] > list1[i+1]):
                list1[i], list1[i+1] = list1[i+1], list1[i]
        else:
            i = 0
    
print(list1)