import os.path

outfile = open("phones.txt", "w")

if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 이미 존재합니다.")

else:
    outfile.write("홍길동 010-1234-5678")
    outfile.write("김철수 010-1234-5679")
    outfile.write("김영희 010-1234-5680")

outfile.close()

# 소스에서 파일의 상대 경로를 사용하고자 한다면 Open in Terminal 에서 직접 실행해야한다.
# 터미널에서  python .\py31_03_filewrite.py 입력