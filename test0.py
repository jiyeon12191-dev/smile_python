print("와우")
num=10
num2=30
result = num + num2
print(result)
name = "이순신"
print(name)
job = "군인"
print(name + job + "이다")
print("배고파" * 5)
반지름 = 5
pi = 3.14
print(반지름 * 2 * pi)
is_student = True
is_food = False
print(is_student)
print( type(pi) )
num = input("정수입력 : " )
num = int(num)
print( num + 10 )
# 한줄 주석이다 
"""  여러줄 주석 이다"""
#문제 . 너비와 높이를 입력받아 사각형의 넓이를 출력 하세요
#a = 10
#print("정수" + str(a))
#width = input("너비 입력 :") # 문자열로 입력 받음
#width = int(width) # 정수타입으로 형변환 
width = int(input("너비 입력 : " ))
height = int(input("높이 입력 : "))
# print(width*height)
print("넓이 : " + str(width*height) )