# def mygcd(x, y):
#     st = set ({})
#     for i in range (x + 1):
#         t1 = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 t1 += 1
#         if t1 == 1:
#             st.add (i)
#
#
#     for i in range (y + 1):
#         t1 = 0
#         for j in range (1, i):
#             if i % j == 0:
#                 t1 += 1
#         if t1 == 1:
#             st.add (i)
#
#     return st
# print (mygcd(16, 32))





def find_smallest(numbers, to_return):
    srt = sorted (numbers)
    return srt [0] if to_return == "value" else numbers.index(srt[0])

print (find_smallest([ 3, 4,465, 6, 6, 6,46,4, 6,46, 4,8, 4,81, 1 ], "valueujkl"))