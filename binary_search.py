import random

numbers = random.choices(range(100), k=10)
numbers = sorted(numbers)

print(numbers)
target = random.choice(numbers)

start = 0
end = len(numbers)-1
while start <= end:
    mid = (start+end)//2
    mid_value = numbers[mid]
    if mid_value < target:
        start = mid+1
    elif mid_value > target:
        end = mid-1
    else:
        print("Find target at", mid)
        break
