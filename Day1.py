import os

#Input path
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\Inputs\Day1"

#Reading input
data = open(input_path,'r')
Content = data.read()
lines = Content.split("\n")

print(len(lines))

nums = {'0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9'}
calibrations = []
check = []

for i in range(len(lines)):
    line = lines[i]
    l = 0
    r = len(line)-1

    while l <= r:
        if line[l] in nums:
            while line[r] not in nums:
                r -= 1
            num = line[l] + line[r]
            calibrations.append(num)
            l = r + 2
        l += 1

calibrations = list(map(int, calibrations))
print(check)
print(sum(calibrations))
print(len(calibrations))



