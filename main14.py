from gpiozero import MotionSensor                  # 'gpiozero' 라이브러리에서 'MotionSensor'을 가져옴
import time                                        # 'time' 라이브러리를 가져옴

pirPin = MotionSensor(16)                          # GPIO 16번 핀을 PIR 모션 센서 설정 

try:

  while True:                                      # 무한반복
  sensorValue = pirPin.value                       # 센서값을 읽고 변수에 저장 (감지: 1, 미감지: 0)
  print(sensorValue)                               # 센서값 출력
  time.sleep(0.1)                                  # 0.1초 대기

except KeyboardInterrupt:                          # 'Ctrl + C'로 프로그램 종
  pass
