import cv2
from ultralytics import YOLO
import cvzone
import math
from sort import *

cap= cv2.VideoCapture("../videos/cars.mp4")  #for the video

#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = int(cap.get(cv2.CAP_PROP_FPS))
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
#out = cv2.VideoWriter('counted_output.mp4', fourcc, fps, (width, height))


model= YOLO('yolo11n.pt')
model.to('cuda')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
 
mask= cv2.imread("mask.png")

#Tracking
tracker= Sort(max_age=20, min_hits=2,iou_threshold=0.3)

limits = [400, 297, 673, 297]
totalCount = []

while True:
    success, img= cap.read()
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

    imgregion=cv2.bitwise_and(img,mask)
    
    imgGraphics = cv2.imread("graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))
    result= model(imgregion, stream=True,save= True)
    
    detection= np.empty((0,5))
    
    for r in result:
        boxes= r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2= box.xyxy[0]
            x1, y1, x2, y2= int(x1), int(y1), int(x2), int(y2)
            w, h= x2-x1, y2-y1
            
            #confidence score
            conf = math.ceil((box.conf[0]*100))/100  #math.ceil for round figure the confidence score    
            
            #class name
            cls= int(box.cls[0])
            currentclass=classNames[cls]
            
            if currentclass =='car' or currentclass =='truck' or currentclass =='bus' or currentclass =='motorbike' and conf>0.3:
            
                currentarray=np.array([x1,y1,x2,y2, conf])
                detection=np.vstack((detection,currentarray))
    
    resultstracker= tracker.update(detection)
    
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)
    for result in resultstracker:
        x1,y1,x2,y2, id= result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
        cvzone.putTextRect(img, f' {int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)
        
        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        
        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    cv2.putText(img,str(len(totalCount)),(255,100),cv2.FONT_HERSHEY_PLAIN,5,(50,50,255),8)
        
    #out.write(img)  # Save the processed frame
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    
#cap.release()
#out.release()
#cv2.destroyAllWindows()
