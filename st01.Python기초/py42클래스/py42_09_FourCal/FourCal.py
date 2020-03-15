
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기 
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기 

class Fourcal(): # 클래스 정의부
    def __init__(self, first):
        self.__first = first # 비공개 변수 선언.

        # self.__first 변수의 getter 메서드 만들기
        # getter 메서드 이름을 만들 때 get + 변수명의 첫글자는 대문자로 나머지는 소문자로
        # getter 메서드의 목적: 비공개 변수값 리턴

    def getFirst(self):
        return self.__first

        # self.__first 변수의 setter 메서드 만들기
        # setter 메서드의 목적: 비공개 변수값을 바꾼다.
        # setter 메서드 이름을 만들 때 set + 변수명의 첫글자는 대문자로 나머지는 소문자로
    def setFirst(self, value):
        self.__first = value

def main():
    #인스턴스 만들기
    c1 = Fourcal(4)

    # 비공개 변수 self.__first 값을 출력
    val = c1.getFirst()
    print (val)
    # 비공개 변수 self.__first 값을 8로 바꾸시오
    val = c1.setfirst(8) # 변경된다.

    print(val)

    main()
    

    # 비공개 변수 self.__first 값을 출력
