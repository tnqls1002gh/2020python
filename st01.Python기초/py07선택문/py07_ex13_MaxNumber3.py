a = int(input("첫번째수를입력하세요"))
b = int(input("두번째수를입력하세요"))
c = int(input("세번째수를입력하세요"))

if a > b:
    print(a)
    # a, c 비교 
    if a > c:
        print(a)
    else : 
        print(c)
else:
    # b, c 비교
    if b > c:
        print(b)
    else :
        print(c)

#중첩 if 방식
if a > b  and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

#연속 if