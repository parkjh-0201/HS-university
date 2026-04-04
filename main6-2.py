from gpiozero import DigitalInputDevice                    # 'gpiozero' 라이브러리에서 'DifitalInputDevice'를 가져옴
from gpiozero import OutputDevice                          # 'gliozero' 라이브러리에서 'OutputDevice'를 가져옴
import time                                                # 'time' 라이브러리를 가져옴
 
bz = OutputDevice(18)                                      # GPIO 18번 핀을 부저 설정
gas = DigitalInputDevice(17)                               # GPIO 17번 핀을 가스 센서 감지 설정
 
try:                                                       # 무한반복
  while True: 
    if gas.value == 0:                                     # 가스 센서 감지 값이 0이면 가스가 감지 O 
      print(＂가스 감지됨＂)                                # "가스 감지됨" 출력
      bz.on()                                              # 부저 ON
      else:                                                # 가스 셋ㄴ서 감지 값이 1이면 정상
      print(＂정상＂)                                       # "정상" 출력
      bz.off()                                             # 부저 OFF
      
      time.sleep(0.2)                                      # 0.2초마다 반복

except KeyboardInterrupt:                                  # 'Ctrl + C'로 프로그램 종료
  pass

bz.off()                                                   # 프로그램 종료 시 부저 OFF
