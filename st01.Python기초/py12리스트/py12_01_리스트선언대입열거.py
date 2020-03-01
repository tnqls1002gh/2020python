# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle


############################
# 리스트 선언
# 리스트에는 모두 담을 수 있다.(함수도 담을 수 있다.)
# array = []
# array = list()
# array = [1, 1.1 "문자", True, [0, 1], {"a":1, "1": "ba"}, None ]
# 공백 리스트 생성
# 문자 H, e, l, l, o를 요소로 가지는 리스트
# 문자열 Hello를 요소로 가지는 리스트
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
# 공백 리스트 생성
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
list1 = ["H", "e", "l", "l", "o"]
print (type(list1), list1)

list2 = ["Hello"]
print (type(list2), list2)

list4 = list("Hello")
print (type(list4), list4)

list3 = [0, 1, 2, 3, 4]
print (type(list3), list3)

list5 = list(range(0, 5, 1) )
print (type(list5), list5)
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
############################
# 리스트 요소 출력
# 리스트의 시작은 0번 부터
############################

array = [1, 1.1, "문자", True, [0, 1] , {"a":1, "1": "ba"}, None]
print ("array[0]", type(array[0]), array[0])
print ("array[4]", type(array[4]), array[4])
print ("array[5]", type(array[5]), array[5])
print ("array[6]", type(array[6]), array[6])

############################
# 리스트 출력
############################
print ("array", array)
############################
# 리스트 슬라이싱
# 1. 선택 연산자 사용하는 방법
# 2. 리스트 메서드 getitem() 사용하는 방법
############################
print("", array[0])
print ("", array[1:3])
print ("", array[-1])
print ("", array[-3])
############################
# 리스트 요소 대입 #값을 바꾼다
# 리스트의 0번방 값을 문자열 "변경"값으로 바꾸시오
############################
print ("array[0]", array[0])
array[0]= "변경"
print ("array[0]", array[0])


############################
# 리스트 요소 추가 \
# C.create ==> append & insert
# 추가: 리스트의 마지막에 넣는다. --> .append() 메서드 사용
# 삽입: 리스트의 중간에 넣는다.    --> .insert() 메서드 사용
############################
array.append("추가")
print ("array", array)
array.insert(0, "삽입")
print ("array", array)
############################
# 리스트 요소 삭제
print ("array", array)
array.pop(0)
print ("array", array)

del array[0]
print ("array", array)

# D.deltef
# 연산자 방식
# 메서드 방식
############################
# 리스트 열거
############################
print ("array", array)
for i in array:
    print (i)
############################
# 복잡한 리스트
# 1차원 리스트
# 2차원 리스트
# 3차원 리스트
############################


############################
# 리스트에 담을 수 있는 것은? =>다
# 리스트 선언 => [], list()
# 리스트 대입 => =
# 리스트 추가 (C) => append(), inser()
# 리스트 읽기 (R) => [방번호]
# 리스트 수정 (U) => [방번호] = 값
# 리스트 삭제 (D) => pop()
# 리스트 정렬 (S) => sorted()
# 리스트 정렬 (S) => .find() + 반복문, rfinde() + 반복문
# 리스트 길이      => len()
# 리스트 출력 
# 리스트 열거  
# 리스트에 저장된 함수 실행하기
############################

############################
# 문자열 vs 리스트
############################

