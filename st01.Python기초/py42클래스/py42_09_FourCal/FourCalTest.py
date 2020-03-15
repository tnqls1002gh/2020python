
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
         result = self.first + self.second
         return result

    def minus(self):
        result = self.first - self.second
        return result

    def mul(self):
         result = self.first * self.second
         return result

    def div(self):
         result = self.first / self.second
         return result

fourcal = Fourcal()
fourcal.setdata(2, 4)

cal1 = fourcal.add()
print ("add:", cal1)

cal2 = fourcal.minus()
print ("min:", cal2)

cal3 = fourcal.mul()
print ("mul:", cal3)

cal4 = fourcal.div()
print ("div:", cal4)


#생성자 만들고 메서드 제정하고 접근자, 설정자 메서드 설정