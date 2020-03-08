# 딕셔너리의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle

# 딕셔너리 선언하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "소금", "치자"],
    "origin": "필리핀"  
}
# 요소 추가 전에 내용을 출력해봅니다.
print(dictionary["name"])
print(dictionary["type"])
print(dictionary["ingredient"])
print(dictionary["origin"])
# 딕셔너리 추가
dictionary["head"]="머리"
dictionary["body"]="몸"

# 선택 연사자[]로 딕셔너리 읽기
# dictionary의 head 값을 출력하시오
print("head 값", dictionary["head"]


# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
try:
    dictionary["존재하지 않는 키"]
except KeyError as ex:
    print (ex)

# 딕셔너리 수정


# 딕셔너리 삭제.
# 1 연산자방식 =>del
# 2 메서드 방식 =>.pop("key")
# name 키를 삭제
# type 키를 삭제
print("삭제 전", dictionary)
dictionary.pop("name")
dictionary.pop("type")
print("삭제 후", dictionary)


# 딕셔너리 키 존재 여부 확인 => .get() 메서드 사용.
# value = dictionary["존재하지 않는 키"]  # KeyError
# value 값이 None 이며 키가 없다는 의미다.
if value == None
    print("키가 존재하지 않는다.")
else:
    print("키값이 존재한다.")
    print(value)

if "존재하지 않는 키" in dictionary:
    print("키값이 존재한다")
else:
    print("키값이 존재하지 않는다")

# S: 정렬. 딕셔너리는 정렬하는 방법이 없다.
# 단, ket 값 정렬 가능, value 값만 정렬은 가능
# 키가 존재하지 않는 경우의 확인 방법 :  None 사용

# 출력합니다.

############
# 딕셔너리 열거
############

# key 만 열거 keys() 메서드 사용
for key in dictionary.keys():
    print("keys>>>", key)
# value 만 열거
for value in dictionary.values():
    print("values>>>", value)
# key, value를 쌍으로 열거 items():
for item in dictionary.items():
    print("items>>>", item)