
# 모듈을 읽어 들입니다.
import os

#파일 존재 유무 체크 
#os.path.isfile()을 사용하여 파일의 존재 여부를 확인 할 수 있다.
# 기본 정보를 몇 개 출력해봅시다.

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].

# 파일을 생성하고 + 파일 이름을 변경합니다.

# 파일을 제거합니다.



# 파일 존재 유무 체크 
if os.path.isfile("./phones.txt"):
    print("파일 존재")
else:
    print("파일 없음")
# 현재 폴더의 파일/폴더를 출력합니다.

# 현재 폴더의 파일/폴더를 구분합니다.

# 폴더를 읽어 들이는 함수
