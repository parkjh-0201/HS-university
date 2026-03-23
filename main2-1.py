from gpiozero import LEDBoard                # 'gpiozero' 라이브러리에서 'LEDBoard'를 가져옴
from time import sleep                       # 'time' 라이브러리에서 'sleep'를 가져옴

leds = LEDBoard(2, 3, 4, 20, 21)             # LED 묶음 설정

try:                                         # 무한루프: 프로그램이 종료될 때까지 신호등 패턴을 반복
while 1:
leds.value = (0, 0, 1, 1, 0)                 # 차량: 빨강 X, 파랑 X, 초록 O / 사람: 빨강 O, 초록 X
sleep(3.0)                                   # 3초 대기
leds.value = (0, 1, 0, 1, 0)                 # 차량: 빨강 X, 파랑 O, 초록 X / 사람: 빨강 O, 초록 X
sleep(1.0)                                   # 1초 대기
leds.value = (1, 0, 0, 0, 1)                 # 차량: 빨강 O, 파랑 X, 초록 X / 사람: 빨강 X, 초록 O
sleep(3.0)                                   # 3초 대기

except KeyboardInterrupt:                    # 'Ctrl + C'로 프로그램 종료시 예외 처리
pass 

leds.off()                                   # 프로그램 종료시 모든 LED X
