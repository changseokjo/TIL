# 1_Week

# # 더하기
# def plus(a, b, c):
#     return a + b + c

# # 곱하기
# def multiply(start, end):
#     return start * end

# to = int(input("첫번째 숫자를 입력하세요 : "))
# to2 = int(input("두번째 숫자를 입력하세요 : "))

# # a = int(input("첫번째 숫자를 입력하세요 : "))
# # b = int(input("두번째 숫자를 입력하세요 : "))
# # c = int(input("세번째 숫자를 입력하세요 : "))

# # # print("전체 합 : ", plus(a,b,c))
# # print(f"합 : {plus(a,b,c)}")

# print(f"합 : {multiply(to,to2)}")

# x = int(input("첫번째 숫자를 입력하세요 : "))
# y = int(input("두번째 숫자를 입력하세요 : "))

# print("몫 : ", x // y , ", 나머지 : ", x % y)

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n - 1)

# print(factorial(5))

# a, b = input("").split()

# print(int(a) + int(b))
# print(int(a) - int(b))
# print(int(a) * int(b))
# print(int(a) // int(b))
# print(int(a) % int(b))

# 시험 성적
# value = int(input(""))

# if 100 >= value and 89 < value:
#     print('A')
# elif 89 >= value and 79 < value:
#     print('B')
# elif 79 >= value and 69 < value:
#     print('C')
# elif 69 >= value and 59 < value:
#     print('D')
# else:
#     print('F')

# 사분면 고르기

# a = input("")
# b = input("")

# if int(a) > 0:
#     if int(b) > 0:
#         print('1')
#     else:
#         print('4')
# else:
#     if int(b) > 0:
#         print('2')
#     else:
#         print('3')

# 윤년

# year = input("")

# if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#     print('1')
# else:
#     print('0')