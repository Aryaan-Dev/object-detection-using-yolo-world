from ultralytics import YOLO
import cv2
import supervision as sv

model = YOLO('yolov8m-world.pt')

# Set custom classes for detection as required instead of "car"
model.set_classes(["car"])

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# give the source file ("cars.mp4") or make it '0' to access realtime camera.
cap = cv2.VideoCapture("cars.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

while cap.isOpened():

    ret, img = cap.read()

    if not ret:
        break

    results = model.predict(img)
    detection = sv.Detections.from_ultralytics(results[0])

    annotated_frame = box_annotator.annotate(
        scene=img.copy(),
        detections=detection
    )
    annotated_frame = label_annotator.annotate(
        scene=annotated_frame,
        detections=detection
    )

    out.write(annotated_frame)

    cv2.imshow("Image", annotated_frame)

    # Break the loop if 'c' is pressed
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

# Release resources
out.release()
cap.release()
cv2.destroyAllWindows()
