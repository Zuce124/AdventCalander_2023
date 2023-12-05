import os

#Input path
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\Inputs\Day1"

#Reading input
data = open(input_path,'r')
Content = data.read()
lines = Content.split("\n")

#indexes
nums = {'0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9'}
nums_w = {'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n',
          'eight': 'e8t', 'nine': 'n9e'}
keys = nums_w.keys()
calibrations = []

for i in range(len(lines)):
    line = lines[i]
    #converting number word to character number
    for key in keys:
        line = line.replace(key, nums_w[key])

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
print(sum(calibrations))



