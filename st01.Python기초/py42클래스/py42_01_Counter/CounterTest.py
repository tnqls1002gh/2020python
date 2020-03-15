
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

import Counter
def main():
    # Counter 인스턴스 생성
    instance1 = Counter.Counter()
    print(instance1.__str__())

    instance1.increment() #1
    instance1.increment() #2

    count = instance1.get.Count()
    print("count" , count)
    print(instance1.__str__())

    #단독 사용시 main ()를 호출
    #if__name__=="__main__":
     #   main()
