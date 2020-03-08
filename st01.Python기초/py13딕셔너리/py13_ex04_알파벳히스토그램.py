# 작업 순서
# 1. 파일 읽고 문자열에 텍스트 저장
# 2. 줄바꿈(|n)을 제거한다. str.replace("|n","")
# 2. 딕셔너리 table을 만든다.
# 3. 문자열 split()해서 array 리스트로 만든다
# 4. 반복문을 사용하여 array 리스트를 루프 돌면서
    #1. 리스트 요소에서 첫글자를 추출하다. 선택 연산자[]사용
    #1.1 val = array[i][0] 또는 val =i[0]
    #2. 대문자와 소문자를 구분하지 않도록 소문자로 치환한다.
    # val = val.lower()
    #3. 딕셔너리 table에서 키값중에 val 있는지 찾는다.
    # ==>table에서 찾을 때는 get()메서드나 in 연산자를 사용한다,
    #4. 찾았다면 table[val]= table[val] + "-"
    # 아니면 table[val]= "-"
# 5. 찾기가 끝나면 table 출력한다.
str = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

str = str.replace("\n",  "")
table = {}
array = str.split(" ")

for i in range(0, len(array), 1):
    #print (i)
    # array[0] = This  t 만 추출  ==> array[0][0] == T
    # array[1] = was   w만 추출  ==> array[1][0] == w 
    # array[2] = a        a만 추출 ==> array[2][0] == a
    key = array[i][0] #첫번째 글자 추출
    key = key.upper() #대문자 치환
    tmp = table.get(key)

    if tmp == None:
        #미존재
        # table[key] = "-" # 문자로 저장
        table[key] = 1   
    else:
        table[key] = table[key] + 1 

for item in table.items():
    print(item[0], item[1], item[0]*item[1])


