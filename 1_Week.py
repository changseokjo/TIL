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


def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)


print(factorial(5))
    