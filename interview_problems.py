
# find sum of any two numbers are equal to 13

# way1:
# -----
nums = [11, 2, 13, 2]

target = 13

seen = {}

for i, num in enumerate(nums):
    needed = target - num
    if needed in seen:
        print(seen[needed], i)

    seen[num] = i



# way2:
# -----
data = [2, 2, 11, 13]

target = 13

for i in range(len(data)): # i=0,1,2,3
    for j in range(i + 1, len(data)): # j=1,2,3
        if data[i] + data[j] == target:
            print(i, j)




