
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

import Circle

def main():
    c1 = Circle.Circle(10)
    print("원 반지름=", c1.radius())
    print("원 넓이=", c1.calcArea())
    print("원 둘레", c1.calcCircum())
    

for Circle in c1:
    print("원 반지름""원 넓이""원 둘레")