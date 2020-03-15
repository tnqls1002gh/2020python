
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

# 입력 파일 이름과 출력 파일 이름을 받는다.
infilename =  askopenfilename() #절대 경로 표시되는 파일명
outfilename = asksaveasfilename()

# 입력과 출력을 위한 파일을 연다.
infilename = open("infilename", "r", encoding="UTF-8")
outfilename = open("outfilename", "w", encoding="UTF-8")
# 합계와 횟수를 위한 변수를 정의한다.
sum=0
count=0
# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.
for line in infilename:
    dailySale=int(line)
    sum = sum+dailySale
    count = count+1
# 총매출과 일평균 매출을 출력 파일에 기록한다.
outfilename.wirte("총매출=" "str(sum)")
outfilename.wirte("평균 일매출=" +"str(sum/count)")

infilename.close()
outfilename.close()

