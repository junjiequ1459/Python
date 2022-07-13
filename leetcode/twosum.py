def twoSum(nums, target):
    count = 1
    count2 = 0
    for i in nums:
        for j in range(1, len(nums)):
            if i + nums[j] == target:
                print(count2,count)
                break
            count = count + 2
        count = count + 1



x = [3,2,4]
y = 6
count = 0
count2 = 0






twoSum(x,y)


def main():
    pass
if __name__ == '__main__':
    main()