
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. Parent 부모 클래스를 선언합니다.
# 3. Child 자식 클래스를 선언합니다. 부모 자식 관계 설정 하는 것이 중요. 
# 4. main() 메서드 만들기 
#     자식 클래스의 인스턴스를 생성하고 부모의 메서드를 호출합니다.
# 5. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

# Parent Class 만들기

class Parent():
    def __init__(self):
        self.__value = "부모 변수"
    def test(self):
        print("parent 클래스의 test()메서드입니다.")   

    def getValue(self):
        return self.__value 

# Child Class 만들기

class Child(Parent):
    def __init(self):
         pass

child = Child()
child.test()
val = child.getValue()
print (val)

# 자식 클래스의 매개변수는 부모 클래스를 사용하면된다다다다ㅏ다다다다다다
# 부모의 변수를 자식 변수가 자신의것처럼 사용할수있다다다다다ㅏㄷ
