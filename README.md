# CCTV Object Tracker

This Python script utilizes the YOLOv5 object detection model to track people in a CCTV footage. It draws bounding boxes around detected persons and tracks their movements in real-time. Additionally, it calculates the number of people within a specified area of interest.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- PyTorch
- YOLOv5 model from Ultralytics

You can install the required packages using pip:
1. pip install opencv-python torch torchvision
2. pip install git+https://github.com/ultralytics/yolov5.git


## Usage

1. Clone the repository or download the script file.
2. Place your CCTV footage in the same directory as the script or specify the correct path to the video file.
3. Run the script using Python:


4. The script will open a window displaying the CCTV footage with bounding boxes around detected persons. It will also show the count of people within a predefined area of interest.

5. Press `Esc` to exit the application.

## Customization

- You can adjust the size and position of the area of interest (`area_1`) by modifying the coordinates in the script.
- Different YOLOv5 models (e.g., `yolov5s`, `yolov5m`, `yolov5l`, `yolov5x`) can be used by changing the model parameter in the `torch.hub.load` function.



