num1 = 0
num2 = 0
nums = [1,num1,num2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0
]
startNums = nums.copy()
index = 0
answer = 19690720
print('starting')
for i in range(0,100):
    num1 = i
    for x in range(0,100):
        num2 = x
        nums = startNums.copy()
        nums[1] = num1
        nums[2] = num2
        while True:
            val = nums[index]
            try:
                a = nums[nums[index+1]]
                b = nums[nums[index+2]]
            except:
                pass
            if val == 99:
                break
            elif val == 1:
                nums[nums[index+3]] = a+b
            elif val == 2:
                nums[nums[index+3]] = a*b
            else:
                print('aersdfasdf')
            index += 4
        print(nums[0])
        if nums[0] == answer:
            print('ANSWER:', num1, num2)

print(num1, num2)