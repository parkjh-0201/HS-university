from gpiozero import MotionSensor                                              # 'gpiozero' 라이브러리에서 'MotionSensor'를 가져옴
import time                                                                    # 'time' 라이브러리를 가져옴 
from picamera2 import Picamera2                                                # 'picamera2'에서 'Picamera2'를 가져옴
import datetime                                                                # 날짜/시간 설정을 위해 'datetime' 라이브러리를 가져옴 

pirPin = MotionSensor(16)                                                      # GPIO 16번 핀을 PIR 모션 센서 설정

picam2 = Picamera2()                                                           # Picamer2 객체 생성
camera_config = picam2.create_preview_configuration()                          # 카메라 미리보기 설정
picam2.configure(camera_config)                                                # 카메라 설정 적용
picam2.start()                                                                 # 카메라 시작

try:

while True:                                                                    # 무한반복
try:
sensorValue = pirPin.value                                                     # 센서 값을 읽고 변수에 저장
if sensorValue ==1:                                                            # 센서 값이 1이면 움직임이 감지 O
now = datetime.datetime.now()                                                  # 현재 시간과 날짜를 가져옴
print(now)                                                                     # 현재 시간과 날짜 출력
fileName = now.strftime('%y-%m-%d %H:%M:%S')                                   # 날짜와 시간을 기반으로 파일 이름 생성
picam2.capture_file(fileName = '.jpg')                                         # jpg 사진 촬영 후 저장
time.sleep(0.5)                                                                # 0.5초 대기 (연속 촬영 방지)

except:                                                                        # 오류 발생 시 무시하고 계속 실행
pass

except KeyboardInterrupt:                                                      # 'Ctrl + C'로 프로그램 종료 
pass
