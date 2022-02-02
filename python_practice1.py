# print("hello world")
# x = 0
# y = 0
# if x == 0:
#     if y == 10:
#         print("Yes")

# str = 'black eagles'

# try:
#     astr = int(str)
# except:
#     astr = -1

# print(astr)

# for i in [2, 1, 5]:
#     print(i)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)


# c = 5

# while c > 0:
#     print(c)
#     c -= 1


# nums = [1, 2, 3, 4, 5]
# sum = 0
# i = 0

# while i < len(nums):
#     sum = sum + nums[i]
#     i += 1

# print(sum)

# numbers = [7, 14, 21, 8, 32, 49]

# i = 0
# while True:
#     response = numbers[i]
#     if response % 7 == 0:
#         break
#     i += 1

# print(response)

while True:
    response = input()
    if int(response) % 7 == 0:
        break
