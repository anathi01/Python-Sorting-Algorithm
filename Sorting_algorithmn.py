import random

# Creates a list of numbers from 0-999
list1 = [x for x in range(1000)]

# Jumbles the numbers in the list
random.shuffle(list1)

# Determines the number of times the code needs to run
print("Enter The Numer of Steps(Accuracy):", "A large value may reduce perfomance")
steps = int(input())

for k in range(steps):
    for i in range(len(list1)):
        if (i < len(list1) - 1):
            # Checks whether the current number is greater than the next number
            if (list1[i] > list1[i+1]):
                # If so, they swap places
                list1[i], list1[i+1] = list1[i+1], list1[i]
        else:
            # Restarts the cycle
            i = 0
    
print(list1)
