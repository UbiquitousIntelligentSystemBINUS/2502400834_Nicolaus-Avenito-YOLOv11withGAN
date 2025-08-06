import os
import json
from pathlib import Path
from tqdm import tqdm

def convert_coco_to_yolo(coco_json_path, images_dir, output_labels_dir):
    output_labels_dir = Path(output_labels_dir)
    output_labels_dir.mkdir(parents=True, exist_ok=True)

    with open(coco_json_path) as f:
        coco = json.load(f)
    
    categories = coco['categories']
    category_map = {cat['id']: idx for idx, cat in enumerate(categories)}


    image_map = {img['id']: img['file_name'] for img in coco['images']}

    annotations_per_image = {}
    for ann in coco['annotations']:
        img_id = ann['image_id']
        annotations_per_image.setdefault(img_id, []).append(ann)

    for img_id, anns in tqdm(annotations_per_image.items(), desc="Converting"):
        file_name = image_map[img_id]
        label_file = output_labels_dir / f"{Path(file_name).stem}.txt"

        with open(label_file, 'w') as f:
            for ann in anns:
                cat_id = ann['category_id']
                class_id = category_map[cat_id]

                x, y, w, h = ann['bbox']
                img_info = next((img for img in coco['images'] if img['id'] == img_id), None)
                if not img_info:
                    continue
                img_w, img_h = img_info['width'], img_info['height']

                # Convert to YOLO format (x_center, y_center, width, height) normalized
                x_center = (x + w / 2) / img_w
                y_center = (y + h / 2) / img_h
                w_norm = w / img_w
                h_norm = h / img_h

                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")

    print(f"\nLabels saved to {output_labels_dir}")

if __name__ == "__main__":
    convert_coco_to_yolo(
        coco_json_path="./annotations/instances_train.json",
        images_dir="./train",
        output_labels_dir="./labels/train"
    )

    convert_coco_to_yolo(
        coco_json_path="./annotations/instances_val.json",
        images_dir="./val",
        output_labels_dir="./labels/val"
    )
