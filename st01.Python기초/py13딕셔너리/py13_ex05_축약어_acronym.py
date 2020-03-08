
table = {
    "B4": "Before",
    "TX": "Thanks",
    "BBL": "Be Back Later",
    "BCNU": "Be Seeing You",
    "HAND": "Have A Nice Day"
}
# 1. 문자열 입력 받기
# 2. 문자열을 split() 해서 array 리스트로 만든다.
# 3-1. 반복문을 이용해서 array 리스트를 루프를 돌면서 딕셔너리 table을 찾는다.
# 3-2. 찾았다면 바꾼다. .replace
# 4. 출력한다. 문자열 메서드 join() 사용하여

# 1. 
str = input("문자열을 입력하세요:")

# 2. 문자열 나누기
array = str.split("")

for i in range(0, len(array), 1):
    print(array[i])
# 3. 반복문을 사용하여 array 리스트 루프를 돌면서
for i in array:
    print(i)
    # 3-1 table에서 찾는다,
    # 찾을때는 get()메서드나 in 연산자를 사용한다.
    # 찾았다면 바꾼다.
    # array[0] = TX일때 table에서 찾으려면 ( get(), in)
    # array[1] = Mr. 일때 table에서 찾으려면 ( get(), in)
    # array[2] = Park. 일때 table에서 찾으려면 ( get(), in)
    value = table.get(i)

    if value == None : 
        result = result + i + ""
    else:
        result = result + value + ""

# 4. 출력한다

print(result)