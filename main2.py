from gpiozero import LED                        # 'gpiozero' 라이브러리에서 'LED'를 가져옴
from time import sleep                          # 'time' 라이브러리에서 'sleep'을 가져옴

# GPIO 핀 번호를 각각 설정
carLedRed = 2
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

# 각 핀을 LED 객체로 생성
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1:                                    # 무한루프: 프로그램이 종료될때 까지 신호등패턴을 반복     
        carLedRed.value = 0                     # 차량 빨간불 X
        carLedYellow.value = 0                  # 차량 노란불 X
        carLedGreen.value = 1                   # 차량 초록불 O
        humanLedRed.value = 1                   # 사람 빨간불 O
        humanLedGreen.value = 0                 # 사람 초록불 X
        sleep(3.0)                              # 3초간 대기
        carLedRed.value = 0                     # 차량 빨간불 X
        carLedYellow.value = 1                  # 차량 노란불 O
        carLedGreen.value = 0                   # 차량 초록불 X
        humanLedRed.value = 1                   # 사람 빨간불 O
        humanLedGreen.value = 0                 # 사람 초록불 X
        sleep(1.0)                              # 1초간 대기
        carLedRed.value = 1                     # 차량 빨간불 O
        carLedYellow.value = 0                  # 차량 노란불 X
        carLedGreen.value = 0                   # 차량 노란불 X
        humanLedRed.value = 0                   # 사람 빨간불 X
        humanLedGreen.value = 1                 # 사람 초록불 O
        sleep(3.0)                              # 3초간 대기
    
except KeyboardInterrupt:
    # 'Ctrl + C'로 모든 프로그램 종료 시 예외 처리 
    pass

# 프로그램 종료시 모든 신호등 X
carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
