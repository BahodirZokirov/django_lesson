# a = ['a', 'b', 'c', 'd']
# b = [1, 2, 3, 4]
# c = enumerate(a, b)
# print(c)


# def even_numbers(arr,n):
#     new = []
# #     while len(new) < n:
#     for i in range(1, len (arr) + 1):
#         if arr[-i] % 2 == 0 and len(new) < 3:
#             new.append (arr[-i])
#     return new[::-1]
# print (even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# a = 123456789
# a = str(a)
# print (a[::-1])

def number_joy(n):
    nat = 0
    while n > 0:
        q = n % 10
        n = n // 10
        nat += q
    na = str(nat)
    reverse_nat = na[::-1]
    k = int(reverse_nat)
    result = k * nat
    print (na)
    print (reverse_nat)
    print (result)
    print (n)
    if result == n:
        return True
    else:
        return False

print(number_joy(1729))