"""
Question 2 :
write a function to determine the maximum and the minimum ones of n given numbers.
Input : [1,2,3,4,9,5,6]
Output : max = 9 and min = 1

"""
def max_min(n):
    n.sort()
    print("min : ", n[0])
    print("max : ", n[-1])

# def max(num):
#     max = 0
#     min = num[0]
#     for i in num:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     print(max, min)
#
#
# print("max",max([1,2,3,4,9,5,6]))
max_min([1,2,3,4,9,5,6])
