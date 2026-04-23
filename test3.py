tot = 0
while True:
    i = input("숫자를 입력하세요:")
    i = int(i)
    tot = tot+i
    if i == 0:
        print(tot)
        break