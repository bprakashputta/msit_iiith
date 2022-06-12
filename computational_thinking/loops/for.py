# # t=0
# for num in range(10,14):
#     for i in range(2, num):
#         if num % i == 1:
#             print(num)
#             break

# # a = int("Enter any number")
# # for i in range(2,6):
# #     if a == i:
# #         print("A")
# #     else:
# #         print("B")


# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var%2==0:
#             continue
#             var += 1
#     var += 1
# else:
#     var += 1

# print(var)

t=0
for i in range(0, 3):
    for j in range(3, 5):
        t += i - j
    print(t)
