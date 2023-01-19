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
# a = int(input())
# array = [int(i) for i in input().split()]
# b = int(input())

# print(array.count(b))

# 과제 안내신 분
# a = [i for i in range(1, 31)]

# for _ in range(28):
#     data = int(input())
#     a.remove(data)
# print(min(a))
# print(max(a))

# 행렬 덧셈
# a, b = [], []

# n, m = map(int, input().split())

# for row in range(n):
#     row = list(map(int, input().split()))
#     a.append(row)

# for row in range(n):
#     row = list(map(int, input().split()))
#     b.append(row)
    
# for row in range(n):
#     for col in range(m):
#         print(a[row][col] + b[row][col], end=' ')
#     print()

# 아스키코드
# print(ord(input()))

# 단어 길이 재기
# print(len(input()))

# 대소문자 바꾸기
print(input().swapcase())