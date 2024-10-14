import random

while True:     # 게임 재시작을 위한 While문
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")
    rand = random.randrange(1,10)       # 랜덤 숫자

    while True:         # 입력값 유효성 검사
        try :
            num = int(input("예상 숫자 : "))    # 숫자 입력
            if (num > 10 or num < 1):           # 숫자 범위 체크
                print("잘못된 입력입니다. 1과 10사이의 숫자를 입력해주세요.")
            elif rand == num :
                print("정답입니다!")
                break
            else :                              # 숫자 범위 밖
                print("너무 작습니다. 다시 입력하세요" if rand > num else "너무 큽니다. 다시 입력하세요")
        except ValueError:                      # 문자열 체크
            print("잘못된 입력입니다. 1과 10사이의 숫자를 입력해주세요.")   
    
    while True:         # 게임 재시작 체크
        retry = input("게임을 다시 하시겠습니까? (y/n): ")
        if retry == "n" or retry == "N":
            print("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
            exit()
        elif retry == "y" or retry == "Y":
            break
        else :
            print("잘못된 입력입니다. y또는 n을 입력해주세요.")