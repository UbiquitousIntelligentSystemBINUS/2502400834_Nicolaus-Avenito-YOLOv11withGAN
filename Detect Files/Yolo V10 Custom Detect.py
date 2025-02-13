from ultralytics import YOLO
import os
import cv2

weights_path = 'YOLOv10_custom/run154/weights/best.pt'
images_folder = '../testCase/'
output_folder = '../testCase/yolov10detect/'
os.makedirs(output_folder, exist_ok=True)

model = YOLO(weights_path)
image_extensions = ['jpg', 'jpeg', 'png']
image_paths = [
    os.path.join(images_folder, img) for img in os.listdir(images_folder)
    if img.split('.')[-1].lower() in image_extensions
]

if not image_paths:
    print("No images found in the specified folder.")
else:
    print(f"Found {len(image_paths)} images. Processing...")

for img_path in image_paths:
    img_name = os.path.basename(img_path)
    output_img_path = os.path.join(output_folder, f"detected_{img_name}")

    results = model(img_path, conf=0.25)

    if len(results[0].boxes) > 0:
        print(f"Detections found in {img_name}:")
        print(results[0].boxes) #Debug
    else:
        print(f"No detections found in {img_name}.")
        continue

    annotated_image = results[0].plot()

#Saving
    cv2.imwrite(output_img_path, annotated_image)

    print(f"Processed: {img_name}, results saved to {output_img_path}")

print("Detection complete. Results saved in:", output_folder)