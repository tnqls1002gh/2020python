# phones.txt 파일에 아래의 2줄 쓰고 저장하시오. 
# 최무선  010-1111-2222")
# 정중부  010-2222-3333

# 파일 저장 할 때 utf-8 인코딩을 성정하시오.
# 실행하면 줄 바꿈이 안 된다. 어떻게 처리할 것인가?
# 파일이 없으면 쓰기 모드로 파일을 여는 코드를 추가하시오.

outfile = open("./file/phones.txt", "a", encoding="UTF-8")

outfile.write("최무선 010-1111-2222\n")
outfile.write("정중부 010-2222-3333\n")

outfile.close()
