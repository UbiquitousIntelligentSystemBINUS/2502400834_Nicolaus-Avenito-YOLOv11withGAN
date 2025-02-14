from ultralytics import YOLO

model = YOLO('yolov10n.yaml') 
yaml = "custom_data.yaml"

model.train(
    data=yaml,
    epochs=100,            
    imgsz=640,            
    batch=4,              
    device=0,             
    workers=4,            
    project="YOLOv10_custom",
    name="run15",
    save=True            
)