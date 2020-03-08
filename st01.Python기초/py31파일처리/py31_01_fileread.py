

#########################
# readline() 파일에서 한 줄씩 읽기
print("readlin()" 파일에서 한 줄씩 읽기)
pfr = open("./file/phones.txt", "r")

s=pfr.readline()
print(s)
s=pfr.readline()
print(s)
s=pfr.readline()
print(s)
s=pfr.readline()
print(s)


# 파일 닫기
pfr.close()
#########################
##

#########################
##반복문 처리
print("반복문으로 파일에서 읽어서 모니터에 출력하기")
pfr = open("./file/phones.txt", "r")

line=prf.readlin()
while line != "":
    # 모니터에 출력
    print(s)

    #다시 파일에서 읽기
    line = pfr.readlin()