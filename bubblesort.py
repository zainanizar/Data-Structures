def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True

random = [5, 2, 1, 8, 4]
bubble_sort(random)
print(random)
