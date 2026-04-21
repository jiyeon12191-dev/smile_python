# age = int(input("8세미만 :"))
# if  age <= 8:
#     print("무료입니다")
# elif age >= 8 and age <= 19:
#     print("1000원입니다")
# else:
#    print("2000원입니다")

id = input("아이디:")
password = input("비밀번호:")

if id == 'admin' and password == '1234':
    print("로그인 성공")
else:
    print("로그인 실패")    
