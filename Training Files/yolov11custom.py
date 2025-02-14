from ultralytics import YOLO

model = YOLO('yolo11n.yaml')
yaml_path = "custom_data.yaml"

model.train(
    data=yaml_path,
    epochs=100,           
    imgsz=640, 
    batch=4,  
    device=0,
    workers=4,  
    project="YOLOv11_custom", 
    name="run1", 
    save=True      
)