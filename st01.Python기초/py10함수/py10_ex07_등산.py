# 사용자 함수 만들기
# 정수를 입력받아서 제곱한 값을 반환하는 square()함수를 만들어 보기

# 함수 정의
# n : 매개변수
def square(n):

        return n**2 # 결과 반환


# 함수 호출
val = square(10) #100
print("10의 제곱은", val)


# 사용자 함수 만들기
# 두개의 정수가 주어지면 두수 중에서 더 큰수를 찾는

# 함수정의
# x: 매개변수
# y: 매개변수

def getmax (x, y)
    result = None # None: 값이 없다.
    if x>y:
        result x
    else
        result y
    return result

def myinput(mesg):
    try:
        n1 = input(mesg)
        n1 = int(n1)
    except ValueError as ex:
        print (ex)
    
    return n1

# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다.
 
def main():

# 입력 처리
n1 = myinput("첫번째 정수 입력")
n2 = myinput("두번째 정수 입력")

# 최대 값 출력
val = getmax (n1, n2)
print (val)

main()