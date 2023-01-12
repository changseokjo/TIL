# 2_Week

# 별찍기 - 1
# a = int(input(""))
# add = ""

# for i in range(0, a):
#     add = add + '*'
#     print(add)

# A + B - 4
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# x보다 작은 수
# a, b = map(int, input().split())
# x = map(int, input().split())

# for i in x:
#     if b > i:
#         print(i, end = " ")

# 개수 새기
a = int(input())
array = [int(i) for i in input().split()]
b = int(input())

print(array.count(b))
