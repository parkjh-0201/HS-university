import cv2
# 모델이 구분할 수 있는 사물 목록 (숫자 ID : 사물 이름)
classNames = {0: 'background',
1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

# 숫자 ID를 넣으면 사물 이름을 돌려주는 함수
# 예: 17 넣으면 'cat' 반환
def id_class_name(class_id, classes):
for key, value in classes.items():                       # 목록을 하나씩 확인하면서
if class_id == key:                                      # ID가 일치하면
return value                                             # 사물 이름 반환

# 카메라 연결 (-1: 연결된 카메라 자동 선택)
camera = cv2.VideoCapture(-1)
camera.set(3, 640) # 카메라 가로 해상도 640으로 설정
camera.set(4, 480) # 카메라 세로 해상도 480으로 설정

def main():
try:
# 학습이 완료된 AI 모델 불러오기
# .pb 파일 : 학습된 가중치(파라미터)가 저장된 파일
# .pbtxt 파일 : 모델의 구조가 저장된 파일
model = cv2.dnn.readNetFromTensorflow('/home/pi/myProjects/project_37/OpencvDnn/models/frozen_inference_graph.pb',
'/home/pi/myProjects/project_37/OpencvDnn/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
# q 키를 누를 때까지 카메라 영상을 계속 분석
while True:
keyValue = cv2.waitKey(1)

# q 키를 누르면 종료
if keyValue == ord('q'):
break

# 카메라에서 현재 프레임(사진 한 장) 가져오기
# _ 는 성공 여부인데 여기서는 사용하지 않으므로 무시
_, image = camera.read()

# 현재 프레임의 가로, 세로 크기 저장 (박스 위치 계산에 사용)
image_height, image_width, _ = image.shape

# 프레임을 모델이 받아들일 수 있는 형태로 변환 후 모델에 입력
# size=(300, 300) : 모델이 요구하는 이미지 크기로 조정
# swapRB=True : 색상 순서를 BGR → RGB로 변환
model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))

# 모델이 현재 프레임을 분석하여 결과 출력
output = model.forward()

# 감지된 사물을 하나씩 확인
for detection in output[0, 0, :, :]:
# 이 감지 결과가 얼마나 확실한지 (0~1 사이, 1에 가까울수록 확실)
confidence = detection[2]
# 확실도가 50% 미만이면 불확실한 결과이므로 건너뜀
if confidence > .5:
# 감지된 사물의 ID 번호
class_id = detection[1]
# ID 번호로 사물 이름 찾기
class_name = id_class_name(class_id, classNames)
# 콘솔에 결과 출력 (ID / 확실도 / 사물이름)
print(str(str(class_id) + " " + str(detection[2]) + " " + class_name))
# 감지된 사물의 박스 위치 계산
# detection[3~6]은 비율값(0~1)이므로 실제 이미지 크기를 곱해 픽셀 좌표로 변환
box_x = detection[3] * image_width           # 박스 왼쪽 위 x 좌표
box_y = detection[4] * image_height          # 박스 왼쪽 위 y 좌표
box_width = detection[5] * image_width       # 박스 오른쪽 아래 x 좌표
box_height = detection[6] * image_height     # 박스 오른쪽 아래 y 좌표
# 프레임 위에 사물 위치를 나타내는 박스 그리기 (색상: 청록색, 두께: 1)
cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
# 박스 위에 사물 이름 텍스트 표시 (색상: 빨간색)
cv2.putText(image, class_name, (int(box_x), int(box_y + .05 * image_height)), cv2.FONT_HERSHEY_SIMPLEX, (.005 * image_width), (0, 0, 255))
# 분석이 완료된 현재 프레임을 화면에 표시
cv2.imshow('image', image)

# Ctrl+C 로 강제 종료 시 에러 없이 조용히 종료
except KeyboardInterrupt:
pass
# 이 파일을 직접 실행했을 때만 main() 호출
# (다른 파일에서 import 했을 때는 자동 실행 안 됨)
if __name__ == '__main__':
main()
cv2.destroyAllWindows() # 열려 있는 모든 창 닫기
