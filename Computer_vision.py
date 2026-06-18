import os
import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

#read the image
image_path=os.path.join('.','images','face.png')
image=cv2.imread(image_path)

H,W,C=image.shape



#1-detect the path model
model_path=os.path.join('.','blazeface_common.task')

options=BaseOptions(model_asset_path=model_path)

#2-put the model in the face detector
base_options=vision.FaceDetectorOptions(base_options=options,min_detection_confidence = 0.5)
#3-create the face detector object, the word with is important to clear the face detector when we not wanted that
with vision.FaceDetector.create_from_options(base_options) as face_detector:
    #4-cover the image not change to rgb cus the mediapipe is clever

    ready_img=mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
                 #5-show the result
    final_result=face_detector.detect(ready_img)

#6 check

if final_result.detections:
    for face in final_result.detections:

        #7- use bounding_box to return origin_x,origin_y,height,width
        box=face.bounding_box

        #8- set padding to increase accuracy
        padding=30
        old_x= box.origin_x
        old_y= box.origin_y
        old_h= box.height
        old_w= box.width

        x1=max(0,old_x-padding)
        y1=max(0,old_y-padding)
       
        x2=min(W,(old_x+old_w)+padding)
        y2=min(H,(old_y+old_h)+padding)


        

        #10- face anonymizer
        face_roi=image[y1:y2,x1:x2]
        blurred_face=cv2.GaussianBlur(face_roi,(99,99),0)
        image[y1:y2,x1:x2]  =  blurred_face
        cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow(' Face Anonymizer',image)
cv2.waitKey(0)  




    



