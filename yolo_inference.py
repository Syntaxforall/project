from ultralytics import YOLO
model=YOLO('yolov8x')
result=model.predict('imgsrc/src.mp4',save=True)
print(result)
print("boxes")
for i in result[0].boxes:
    print(i)