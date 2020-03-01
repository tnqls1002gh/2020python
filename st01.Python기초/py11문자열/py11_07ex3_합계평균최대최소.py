#문자열 "74 874 9883 73 9 73646 774"에서 각 숫자의 합계, 평균, 최대값 그리고 최소값을 구하시오

temp3 = "74 874 9883 73 9 73646 774"
a = temp3.split(" ")
    int(a)
    print a
#문자열로된 리스트가 반환
print(max (a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))