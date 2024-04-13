from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('input_videos/Highlight1.mp4', save=True)