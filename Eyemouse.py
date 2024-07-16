import cv2
import mediapipe as mp
import pyautogui
cam= cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)
screen_w, screen_h = pyautogui.size()
#facial recognition
while True:
    _, frame= cam.read()
    frame=cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output= face_mesh.process(rgb_frame)
    points= output.multi_face_landmarks
    frame_h, frame_w,_ = frame.shape
#marking eye points
    if points:
        marks= points[0].landmark
        for id, landmark in enumerate(marks[474:478]):
            x =int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id==1:
                screen_x= int(landmark.x *screen_w)
                screen_y= int(landmark.y * screen_h)
                pyautogui.moveTo (screen_x,screen_y)
        left_eye=[marks[145],marks[159]]
        for landmark in left_eye:
            x= int (landmark.x * frame_w)
            y= int (landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left_eye[0].y - left_eye[1].y) < 0.01:
               pyautogui.click()

    cv2.imshow('Eyemouse', frame)
    cv2.waitKey(1)