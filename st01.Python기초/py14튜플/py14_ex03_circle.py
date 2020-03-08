import math
def circle( radius):
    면적 = math.pi*radius*radius
    둘레 = 2*math.pi*radius

    return (면적, 둘레)

def main():
    str = input("원의 반지름을 입력하시오")
    radius = float(str) #문자열을 실수로 변환한다.
    #원의 넓이와 둘레를 계산한다.
    (x,y)= circle(radius)  # x==면적, y==둘레

    tmp = "원의 넓이는 %10.4f, 둘레는 %10.4f 이다." %(x,y)
    print(tmp)

# main 함수 호출
if __name__=='__main__':
    main()