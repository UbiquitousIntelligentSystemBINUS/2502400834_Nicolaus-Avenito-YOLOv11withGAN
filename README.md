Penelitian ini menggunakan dataset publik InsPLAD, yang dapat diakses pada link berikut:
<a href="https://github.com/andreluizbvs/InsPLAD"> Official Github Page </a> || Download link: <a href="https://drive.google.com/drive/folders/1psHiRyl7501YolnCcB8k55rTuAUcR9Ak ">Google Drive</a>

Cara menjalankan program untuk melakukan training:
1. Download Zip file dari Github
2. install requirements yang terdapat pada requirements.txt
3. Buka terminal dan buka folder melalui command cd

Jikalau ingin melakukan training dapat dilakukan dengan menggunakan command berikut:
```python
python Training\ Files/[yoloversion]custom.py
```
Jikalau ingin melakukan evaluasi terhadap model dengan menggunakan model yang sudah di train dapat dilakukan dengan menggunakan command:
```python
python Detect\ Files/[yoloversion]detect.py
```
Weights dari masing masing model yang telah di train dapat ditemukan pada folder result masing-masing model. (Weights menggunakan file type .pt)

Penelitian ini menggunakan dataset dengan struktur sebagai berikut:
```
InsPLAD Detection
├── annotations # Labels untuk file foto
├── train #images untuk training (Augmentasi data secara otomatis ditambahkan pada folder ini
├── val #images untuk validasi (augmentasi data secara otomatis ditambahkan pada folder ini
```

Judul Penelitian (EN):
Power Line Component Detection Using YOLOv11 on Nvidia Jetson Nano

Abstract (EN):
Throughout the years, we grow more and more dependant on electricity, and the need to protect the infrastructure of electricity increases as well. The power transmission lines that we rely on everyday requires plenty of parts to work properly, to ensure that we get our daily need of electricity. This growing need of maintenance sparks researches aimed at optimizing the process, where traditionally it would have been done manually, nowadays it is done through drones, UAVs, and Artificial Intelligence. The focus for this research is to implement a state of the art object detection model, called the YOLO or the You Only Look Once model, to help streamline this process of maintenance. This is later implemented into a single board computer, the Nvidia Jetson Nano, to make it easier to implement, since single board computers are quite small in size. The results show that even through years of development, YOLO hasn’t quite reached the level of real time, it has gotten close, with the average time for detection being below 1 second, with the YOLOv5, YOLOv10, and YOLOv11.

Judul Penelitian (ID):
DETEKSI KOMPONEN TRANSMISI DAYA MENGGUNAKAN ALGORITMA YOLOv11 DAN GAN PADA JETSON NANO

Abstract (ID):
Dari tahun ke tahun, kita semakin bergantung pada listrik, dan kebutuhan untuk melindungi infrastruktur listrik juga secara otomatis meningkat. Saluran transmisi listrik yang kita gunakan setiap hari membutuhkan banyak komponen agar dapat bekerja dengan baik, agar kita bisa mendapatkan listrik setiap harinya. Kebutuhan maintenance yang terus meningkat ini memicu penelitian yang bertujuan untuk mempermudah proses tersebut, di mana secara tradisional dilakukan secara manual, belakangan ini dilakukan melalui drone, UAV, dan Artificial Intelligence (AI). Oleh karena itu, penelitian ini berfokus untuk mengimplementasikan sebuah model pendeteksian objek terbaru, yang disebut model YOLO atau You Only Look Once, untuk membantu mempermudah proses pemeliharaan ini. Hal ini kemudian diimplementasikan ke dalam sebuah single board computer, lebih tepatnya sebuah Nvidia Jetson Nano, agar lebih mudah diimplementasikan di dunia nyata, karena single board computer berukuran cukup kecil. Hasil yang didapat menunjukkan bahwa meskipun melalui pengembangan selama bertahun-tahun, YOLO belum bisa mendeteksi objek secara real time, namun sudah mendekati, dengan rata-rata waktu deteksi di bawah 1 detik, dengan YOLOv5, YOLOv10, dan YOLOv11.

Key Words:
Object Detection, YOLOv11, GAN, Power Transmission Line, Computer Vision
