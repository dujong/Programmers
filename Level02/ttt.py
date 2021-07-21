import dlib, cv2
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt

#이미지 처리
# 모델 불러오기
detector = dlib.cnn_face_detection_model_v1('/content/drive/MyDrive/DL/dog_face_detector/dogHeadDetector.dat')
predictor = dlib.shape_predictor('/content/drive/MyDrive/DL/dog_face_detector/dogHeadDetector.dat')

# 이미지 불러오기

img_path = '~~/18.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(pigsize=(16, 16))
plt.imshow(img)

# model 사용해서 얼굴 탐지
# upsample_num_times은 정밀 탐지를 위해서 이미지를 확대하는 횟수
dets = detector(img, upsample_num_times=1)

img_result = img.copy()

for i, d in enumerate(dets):
    print('count: {} Letf: {} Top: {} Right: {} Bottom: {} Confidence: {}' .format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

    x1, y1 = d.rect.left, d.rect.top
    x2, y2 = d.rect.right, d.rect.bottom

    cv2.rectangle(img_result, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=(255, 0, 0), lineType=cv2.LINE_AA)

plt.figure(figsize=(16,16))
plt.imshow(img_result)

# 감지한 얼굴 area에서 landmark 추출
for i, d in enumerate(dets):
    shape = predictor(img, d.rect)
    shape = face_utils.shape_to_np(shape)

    for i, p in enumerate(shape):
        cv2.circle(img_result, center=tuple(p), radius=3, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
        cv2.putText(img_result, str(i), tuple(p) ,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

img_out = cv2.cvtColor(img_result , cv2.COLOR_RGB2BGR)
cv2.imwrite('/content/drive/MyDrive/DL/dog_face_detector/img/dog_test_out.jpg', img_out)
plt.figure(figsize=(16, 16))
plt.imshow(img_result)

#비디오 처리
SCALE_FACTOR = 0,2

detector = dlib.cnn_face_detection_model_v1('/content/drive/MyDrive/DL/dog_face_detector/dogHeadDetector.dat')
predictor = dlib.shape_predictor('/content/drive/MyDrive/DL/dog_face_detector/dogHeadDetector.dat')


video_path = '/content/drive/MyDrive/DL/dog_face_detector/img/27.mp4'
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('/content/drive/MyDrive/DL/dog_face_detector/img/%s_dog_test_video.mp4' %(video_path.split('img/')[1].split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened:
    ret, img = cap.read()

    if not ret:
        break

    img_result = img.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, dsize=None, fx=SCALE_FACTOR, fy=SCALE_FACTOR)

    dets = detector(img, upsample_num_times=1)

    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))
        x1, y1 = int(d.rect.left/SCALE_FACTOR), int(d.rect.top-SCALE_FACTOR)
        x2, y2 = int(d.rect.right), int(d.rect.bottom)

        cv2.rectangle(img_result, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=(255,0,0), lineType=cv2.LINE_AA)

        shape = predictor(img, d.rect)
        shape = face_utils.shape_to_np(shape)

        for i, p in enumerate(shape):
            cv2.circle(img_result, center=tuple((p / SCALE_FACTOR).astype(int)), radius=5, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            cv2.putText(img_result, str(i), tuple((p / SCALE_FACTOR).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

    out.write(img_result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()

