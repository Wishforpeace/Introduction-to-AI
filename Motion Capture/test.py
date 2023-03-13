import cv2
import mediapipe as mp

# 初始化MediaPipe Pose模型
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 初始化OpenCV摄像头
cap = cv2.VideoCapture(0)

# 不断从摄像头读取帧并处理骨骼动作
while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 将帧转换为RGB格式
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 分析帧中的骨骼动作
    results = pose.process(frame)

    # 将帧转换回BGR格式，并在其中绘制骨骼
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 显示帧
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭摄像头和窗口
cap.release()
cv2.destroyAllWindows()
