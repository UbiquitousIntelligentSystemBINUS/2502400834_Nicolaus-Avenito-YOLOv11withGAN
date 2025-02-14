from ultralytics import YOLO
import os
import cv2

output_dir = 'yolov5/run1'
os.makedirs(output_dir, exist_ok=True)

model = YOLO('yolov5n.yaml') 


model.train(
    data='custom_data.yaml',  
    epochs=100,                       
    imgsz=640,                         
    batch=4,                           
    device=0,         
    workers=4,
    save=True                  
)
