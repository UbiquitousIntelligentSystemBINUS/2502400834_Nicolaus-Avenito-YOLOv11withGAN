from ultralytics import YOLO
import os
import cv2

output_dir = 'yolov3'
os.makedirs(output_dir, exist_ok=True)

model = YOLO('yolov3-tiny.yaml') 


model.train(
    data='custom_data.yaml',  
    epochs=100,                       
    imgsz=640,                         
    batch=4,                           
    device=0,
    workers=4,
    save=True                          
)
